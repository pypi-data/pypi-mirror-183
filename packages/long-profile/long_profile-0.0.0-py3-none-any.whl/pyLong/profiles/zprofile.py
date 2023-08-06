import json
from math import ceil, radians, pi, atan, tan

from matplotlib.lines import Line2D
from matplotlib.axes import Subplot
import pandas as pd
from scipy.interpolate import interp1d
from scipy.optimize import fsolve
from simpledbf import Dbf5
import shapefile
import numpy as np

import visvalingamwyatt as vw
from rdp import rdp

from pyLong.dictionnaries.styles import line_styles, marker_styles
from pyLong.dictionnaries.colors import colors

class zProfile:
    _counter = 0

    def __init__(self):
        zProfile._counter += 1

        self._xz = [(0, 0), (1000, 1000)]

        self._title = "new profile"

        self._label = ""

        self._active = True

        self._visible = True

        self._line = Line2D([], [])

        self._line_style = 'solid'

        self._line_color = 'Black'
        
        self._line_thickness = 1.

        self._marker_style = 'none'
        
        self._marker_color = 'Black'
        
        self._marker_size = 1.

        self._opacity = 1.
        
        self._order = 1
        
    """
    Methods:
    - add_point --> OK
    - clear --> OK
    - copy_style --> OK
    - duplicate --> OK
    - export --> OK
    - export_style --> OK
    - from_dbf --> OK
    - from_shp --> OK
    - from_txt --> OK
    - import_style --> OK
    - interpolate --> OK
    - length --> OK
    - listing --> OK
    - merge --> OK
    - new_point --> OK
    - plot --> OK
    - remove_point --> OK
    - resample --> OK
    - reverse --> OK
    - simplify --> OK
    - solve --> OK
    - summarize --> OK
    - translate --> OK
    - truncate --> OK
    - update --> OK
    """
    
    def add_point(self, point):
        if not isinstance(point, tuple):
            return False
        
        if not len(point) > 1:
            return False
        
        x, z = point[0], point[1]
        if not isinstance(x, (int, float)) or not isinstance(z, (int, float)):
            return False
        
        if x in [x for x, z in self._xz]:
            return False
 
        self._xz.append((x, z))
        self._xz.sort()
        return True
                        
    def clear(self):
        self._line = Line2D([], [])
        
    def copy_style(self, zprofile):
        if not isinstance(zprofile, zProfile):
            return False
        
        self._line_style = zprofile.line_style
        self._line_color = zprofile.line_color
        self._line_thickness = zprofile.line_thickness
        self._marker_style = zprofile.marker_style
        self._marker_color = zprofile.marker_color
        self._marker_size = zprofile.marker_size
        self._opacity = zprofile.opacity
        self._order = zprofile.order
        return True

    def duplicate(self):
        zprofile = zProfile()
        zprofile.copy_style(self)
        
        zprofile.title += " duplicated"
        zprofile.label = self._label
        
        zprofile.xz = list(self._xz)
        
        return zprofile
    
    def export(self, filename, delimiter="\t", separator=".", decimals=3):
        if not isinstance(filename, str) or not isinstance(decimals, int):
            return False
        
        if delimiter not in ["\t", " ", ";", ","] or separator not in [".", ","]:
            return False
        
        if delimiter == separator:
            return False
        
        if not len(filename) > 0:
            return False
        
        x = np.array(self.x)
        z = np.array(self.z)
        
        xz = np.array([x, z]).T
        xz = pd.DataFrame(xz) 
        
        try:
            xz.to_csv(filename,
                      sep = delimiter,
                      float_format = f"%.{decimals}f",
                      decimal = separator,
                      index = False,
                      header = ['X','Z'])
            return True
        except:
            return False
    
    def export_style(self, filename):
        style = {'line_style': self._line_style,
                 'line_color': self._line_color,
                 'line_thickness': self._line_thickness,
                 'marker_style': self._marker_style,
                 'marker_color': self._marker_color,
                 'marker_size': self._marker_size,
                 'visible': self._visible,
                 'opacity': self._opacity,
                 'order': self._order}

        if not isinstance(filename, str):
            return False
        
        if not len(filename) > 0:
            return False
        
        with open(filename, 'w') as file:
            json.dump(style, file, indent=0)
            return True

    def from_dbf(self, filename, X_field='dist', Z_field='Z'):
        if not isinstance(X_field, str) or not isinstance(Z_field, str):
            return False
        
        try:
            dbf = Dbf5(filename)
            
        except:
            return False
        
        data = dbf.to_dataframe()
        
        if data.shape[0] < 2 or data.shape[1] < 2:
            return False
        
        if X_field not in list(data.columns) or Z_field not in list(data.columns):
            return False
        
        if data.loc[:, X_field].dtype not in ['float64', 'int64'] or \
           data.loc[:, Z_field].dtype not in ['float64', 'int64']:
            return False
        
        data = data.dropna()
        
        i = list(data.columns).index(X_field)
        x = list(data.values[:, i])
        
        i = list(data.columns).index(Z_field)
        z = list(data.values[:, i])
        
        xz = [(x, z) for x, z in zip(x, z)]
        
        xz.sort()
        x = [x for x, z in xz]
        dx = np.array(x[1:]) - np.array(x[:-1])
        dx = list(dx)
        
        if 0 in dx:
            return False
        
        self._xz = xz
        return True        

    def from_shp(self, filename):
        try:
            sf = shapefile.Reader(filename)
            
        except:
            return False
        
        shapes = sf.shapes()
        
        if len(shapes) < 1:
            return False
        
        shape = shapes[0]
        
        if shape.shapeType != 13:
            return False
        
        dist = [0]
        for i, (x,y) in enumerate(shape.points):
            if i != 0:
                d = ((x - shape.points[i-1][0])**2 + (y - shape.points[i-1][1])**2)**0.5
                dist.append(d + dist[i-1])
                
        xz = [(x, z) for x, z in zip(dist, shape.z)]
        
        xz.sort()
        x = [x for x, z in xz]
        dx = np.array(x[1:]) - np.array(x[:-1])
        dx = list(dx)
        
        if 0 in dx:
            return False
        
        self._xz = xz
        return True  

    def from_txt(self, filename, X_field='X', Z_field='Z', delimiter="\t", decimal="."):
        if not isinstance(X_field, str) or not isinstance(Z_field, str):
            return False
        
        if delimiter not in [" ", "\t", ";", ","] or decimal not in [".", ","] or delimiter == decimal:
            return False
        
        try:
            data = pd.read_csv(filename,
                               delimiter=delimiter,
                               decimal=decimal,
                               skiprows=0,
                               encoding="utf-8")
            
        except:
            return False
        
        if data.shape[0] < 2 or data.shape[1] < 2:
            return False
        
        if X_field not in list(data.columns) or Z_field not in list(data.columns):
            return False
        
        if data.loc[:, X_field].dtype not in ['float64', 'int64'] or \
           data.loc[:, Z_field].dtype not in ['float64', 'int64']:
            return False
        
        data = data.dropna()
        
        i = list(data.columns).index(X_field)
        x = list(data.values[:, i])
        
        i = list(data.columns).index(Z_field)
        z = list(data.values[:, i])
        
        xz = [(x, z) for x, z in zip(x, z)]
        
        xz.sort()
        x = [x for x, z in xz]
        dx = np.array(x[1:]) - np.array(x[:-1])
        dx = list(dx)
        
        if 0 in dx:
            return False
        
        self._xz = xz
        return True  
                    
    def import_style(self, filename):
        if not isinstance(filename, str):
            return False
        
        if not len(filename) > 0:
            return False
        
        with open(filename, 'r') as file:
            try:
                style = json.load(file)
            except json.JSONDecodeError:
                return False

        if isinstance(style, dict):
            if 'line_style' in style.keys():
                self.line_style = style['line_style']
            if 'line_color' in style.keys():
                self.line_color = style['line_color']
            if 'line_thickness' in style.keys():
                self.line_thickness = style['line_thickness']
            if 'marker_style' in style.keys():
                self.marker_style = style['marker_style']
            if 'marker_color' in style.keys():
                self.marker_color = style['marker_color']
            if 'line_thickness' in style.keys():
                self.marker_size = style['marker_size']
            if 'visible' in style.keys():
                self.visible = style['visible']
            if 'opacity' in style.keys():
                self.opacity = style['opacity']
            if 'order' in style.keys():
                self.order = style['order']
            return True
        else:
            return False

    def interpolate(self, x):
        if isinstance(x, (int, float)):
            if min(self.x) <= x <= max(self.x):
                Xs = self.x
                Xs.append(x)
                Xs.sort()
                i = Xs.index(x)

                if x == Xs[0]:
                    return float(self.z[0])
                elif x == Xs[-1]:
                    return float(self.z[-1])
                else:
                    f = interp1d(self.x[i-1:i+1], self.z[i-1:i+1], kind='linear')
                    return float(f(x))
                
    def length(self, dim='2D'):
        if not isinstance(dim, str):
            return
        
        if dim.upper() not in ['2D', '3D']:
            return
        
        if dim.upper() == '2D':
            return self._xz[-1][0] - self._xz[0][0]
        else:
            dist = 0
            for i in range(1, len(self._xz)):
                dist += ((self.x[i] - self.x[i-1])**2 + (self.z[i] - self.z[i-1])**2)**0.5
            return float(dist)
                
    def listing(self, decimals=3):
        if isinstance(decimals, int):
            for i, (x, z) in enumerate(self._xz):
                print(f"vertice {i}: x = {round(x, decimals)} m ; z = {round(z, decimals)} m")
                
    def merge(self, zprofile):
        if not isinstance(zprofile, zProfile):
            return

        merged_zprofile = self.duplicate()
        merged_zprofile.title += " merged"

        for (x, z) in zprofile.xz:
            merged_zprofile.add_point((x, z))

        return merged_zprofile
            
    def new_point(self, i, **kwargs):
        if not isinstance(i, int):
            return None, None
        
        if not 0 <= i < len(self._xz):
            return None, None
        
        if 'method' not in kwargs.keys():
            return None, None
        
        if kwargs['method'] not in ['dX + dZ', 'slope + X', 'slope + dX', 'slope + Z', 'slope + dZ']:
            return None, None
        
        if kwargs['method'] == 'dX + dZ':
            if 'dX' not in kwargs.keys() or 'dZ' not in kwargs.keys():
                return None, None
            
            if not isinstance(kwargs['dX'], (int, float)) or not isinstance(kwargs['dZ'], (int, float)):
                return None, None
            
            dX = kwargs['dX']
            dZ = kwargs['dZ']
            
            return self.x[i] + dX, self.z[i] + dZ
        
        elif kwargs['method'] == 'slope + X':
            if 'slope' not in kwargs.keys() or 'X' not in kwargs.keys() or 'slope_unit' not in kwargs.keys():
                return None, None
            
            if kwargs['slope_unit'] not in ['radian', 'degree', 'percent']:
                return None, None
            
            if not isinstance(kwargs['slope'], (int, float)) or not isinstance(kwargs['X'], (int, float)):
                return None, None
            
            slope = kwargs['slope']
            X = kwargs['X']
            slope_unit = kwargs['slope_unit']
            
            if slope_unit == 'radian':
                if not -pi/2 < slope < pi/2:
                    return None, None
                else:
                    angle = slope
            elif slope_unit == 'degree':
                if not -90 < slope < 90:
                    return None, None
                else:
                    angle = radians(slope)
            else:
                angle = atan(slope)
                
            f = lambda x: tan(angle) * (x - self.x[i]) + self.z[i]
            
            return X, f(X)
        
        elif kwargs['method'] == 'slope + dX':
            if 'slope' not in kwargs.keys() or 'dX' not in kwargs.keys() or 'slope_unit' not in kwargs.keys():
                return None, None
            
            if kwargs['slope_unit'] not in ['radian', 'degree', 'percent']:
                return None, None
            
            if not isinstance(kwargs['slope'], (int, float)) or not isinstance(kwargs['dX'], (int, float)):
                return None, None
            
            slope = kwargs['slope']
            dX = kwargs['dX']
            slope_unit = kwargs['slope_unit']
            
            if slope_unit == 'radian':
                if not -pi/2 < slope < pi/2:
                    return None, None
                else:
                    angle = slope
            elif slope_unit == 'degree':
                if not -90 < slope < 90:
                    return None, None
                else:
                    angle = radians(slope)
            else:
                angle = atan(slope)
                
            f = lambda x: tan(angle) * (x - self.x[i]) + self.z[i]
            
            return self.x[i] + dX, f(self.x[i] + dX)
        
        elif kwargs['method'] == 'slope + Z':
            if 'slope' not in kwargs.keys() or 'Z' not in kwargs.keys() or 'slope_unit' not in kwargs.keys():
                return None, None
            
            if kwargs['slope_unit'] not in ['radian', 'degree', 'percent']:
                return None, None
            
            if not isinstance(kwargs['slope'], (int, float)) or not isinstance(kwargs['Z'], (int, float)):
                return None, None
            
            slope = kwargs['slope']
            Z = kwargs['Z']
            slope_unit = kwargs['slope_unit']
            
            if slope_unit == 'radian':
                if not -pi/2 < slope < pi/2:
                    return None, None
                else:
                    angle = slope
            elif slope_unit == 'degree':
                if not -90 < slope < 90:
                    return None, None
                else:
                    angle = radians(slope)
            else:
                angle = atan(slope)
                
            f = lambda x: tan(angle) * (x - self.x[i]) + self.z[i]
            
            return self.x[i] + (Z - self.z[i]) / tan(angle) , Z
        
        elif kwargs['method'] == 'slope + dZ':
            if 'slope' not in kwargs.keys() or 'dZ' not in kwargs.keys() or 'slope_unit' not in kwargs.keys():
                return None, None
            
            if kwargs['slope_unit'] not in ['radian', 'degree', 'percent']:
                return None, None
            
            if not isinstance(kwargs['slope'], (int, float)) or not isinstance(kwargs['dZ'], (int, float)):
                return None, None
            
            slope = kwargs['slope']
            dZ = kwargs['dZ']
            slope_unit = kwargs['slope_unit']
            
            if slope_unit == 'radian':
                if not -pi/2 < slope < pi/2:
                    return None, None
                else:
                    angle = slope
            elif slope_unit == 'degree':
                if not -90 < slope < 90:
                    return None, None
                else:
                    angle = radians(slope)
            else:
                angle = atan(slope)
                
            f = lambda x: tan(angle) * (x - self.x[i]) + self.z[i]
            
            return self.x[i] + dZ / tan(angle) , self.z[i] + dZ
        
    def plot(self, ax):
        if isinstance(ax, Subplot):
            self.clear()
            self.update()

            ax.add_line(self._line)            
        
    def remove_point(self, i):
        if not isinstance(i, int):
            return False
        
        if  not 0 <= i < len(self._xz):
            return False
        
        self._xz.pop(i)
        return True
                
    def resample(self, dx):
        if not isinstance(dx, (int, float)):
            return
        
        if dx <= 0:
            return
        
        x = [x for x, z in self._xz]
        
        resampled_zprofile = zProfile()
        resampled_zprofile.xz = list(self._xz)
        
        for i in range(1, len(x)):
            if (x[i] - x[i-1]) / dx > 1:
                n = ceil((x[i] - x[i-1]) / dx)
                
                for value in np.linspace(x[i-1], x[i], n+1):
                    value = float(value)
                    resampled_zprofile.add_point((value, self.interpolate(value)))
                    
        return resampled_zprofile

    def reverse(self, zprofile):
        if not isinstance(zprofile, zProfile):
            return False

        reversed_zprofile = self.duplicate()
        reversed_zprofile.title += " reversed"
        
        x_start = zprofile.xz[0][0]
        x_end = zprofile.xz[-1][0]

        xz = [(-x + x_end + x_start, z) for (x, z) in self._xz]

        xz.sort()
        reversed_zprofile.xz = xz
        
        return reversed_zprofile
    
    def simplify(self, **kwargs):
        def f(xz):
            zprofile = zProfile()
            zprofile.xz = xz
            
            dz = []
            for x, z in self._xz:
                dz.append(abs(z - zprofile.interpolate(x)))
                
            n_input = len(self._xz)
            L_input = self.length(dim='3D')
            n_output = len(xz)
            L_output = zprofile.length(dim='3D')
            n_removed = n_input - n_output
            dL = L_input - L_output
            
            dz = np.array(dz)
            if len(dz[dz != 0]) > 0:                
                max_error = np.max(dz[dz != 0.])
                min_error = np.min(dz[dz != 0.])
                mean_error = np.mean(dz[dz != 0.])
                std_error = np.std(dz[dz != 0.])
            else:                   
                max_error = 0.
                min_error = 0.
                mean_error = 0.
                std_error = 0.
                   
            return {'input vertices': n_input,
                    'input 3D length': L_input,
                    'output vertices': n_output,
                    'output 3D length': L_output,
                    'removed vertices': n_removed,
                    '3D length delta': dL,
                    'max |dz|': max_error,
                    'min |dz|': min_error,
                    'mean |dz|': mean_error,
                    'std |dz|': std_error}
        
        if 'method' not in kwargs.keys():
            return None, None
        
        if kwargs['method'] not in ['vw', 'rdp']:
            return None, None
        
        if kwargs['method'] == 'vw':
            xz = np.array([np.array(self.x), np.array(self.z)]).T
            simplifier = vw.Simplifier(xz)
            
            if 'ratio' in kwargs.keys():
                if not isinstance(kwargs['ratio'], (int, float)):
                    return None, None
                elif not 0. < kwargs['ratio'] <= 1.:
                    return None, None
                else:
                    xzs = simplifier.simplify(ratio=kwargs['ratio'])
                        
                    x = list(xzs[:,0])
                    z = list(xzs[:,1])
                    
                    xz = [(x, z) for x, z in zip(x, z)]
                    
                    if len(xz) == 0:
                        xz = [self._xz[0], self._xz[-1]]
                    
                    if xz[0][0] != self.x[0]:
                        xz.insert(0, self.xz[0])
                    
                    if xz[-1][0] != self.x[-1]:
                        xz.append(self.xz[-1])
                    
                    return xz, f(xz)
                
            elif 'number' in kwargs.keys():
                if not isinstance(kwargs['number'], int):
                    return None, None
                elif not  1 < kwargs['number'] <= len(self.x):
                    return None, None
                else:
                    xzs = simplifier.simplify(number=kwargs['number']-1)
                        
                    x = list(xzs[:,0])
                    z = list(xzs[:,1])
                    
                    xz = [(x, z) for x, z in zip(x, z)]
                    
                    if len(xz) == 0:
                        xz = [self._xz[0], self._xz[-1]]
                    
                    if xz[0][0] != self.x[0]:
                        xz.insert(0, self.xz[0])
                    
                    if xz[-1][0] != self.x[-1]:
                        xz.append(self.xz[-1])
                    
                    return xz, f(xz)
                
            elif 'threshold' in kwargs.keys():
                if not isinstance(kwargs['threshold'], (int, float)):
                    return None, None
                elif not 0 <= kwargs['threshold']:
                    return None, None
                else:
                    xzs = simplifier.simplify(threshold=kwargs['threshold'])
                        
                    x = list(xzs[:,0])
                    z = list(xzs[:,1])
                    
                    xz = [(x, z) for x, z in zip(x, z)]
                    
                    if len(xz) == 0:
                        xz = [self._xz[0], self._xz[-1]]
                    
                    if xz[0][0] != self.x[0]:
                        xz.insert(0, self._xz[0])
                    
                    if xz[-1][0] != self.x[-1]:
                        xz.append(self._xz[-1])
                        
                    return xz, f(xz)
            else:
                return None, None
        
        else:
            if 'epsilon' not in kwargs.keys() or 'algo' not in kwargs.keys():
                return None, None
            
            if not isinstance(kwargs['epsilon'], (int, float)):
                return None, None
            
            if not 0 <= kwargs['epsilon']:
                return None, None
            
            if kwargs['algo'] not in ['iter', 'rec']:
                return None, None
            
            if kwargs['algo'] == 'iter':
                xzs = rdp(self.xz, epsilon=kwargs['epsilon'], algo='iter')
                
                xz = [(x, z) for x, z in xzs]
                
                if len(xz) == 0:
                    xz = [self._xz[0], self._xz[-1]]
                
                if xz[0][0] != self.x[0]:
                    xz.insert(0, self.xz[0])

                if xz[-1][0] != self.x[-1]:
                    xz.append(self.xz[-1])

                return xz, f(xz)
                
            else:
                xzs = rdp(self.xz, epsilon=kwargs['epsilon'], algo='rec')
                
                xz = [(x, z) for x, z in xzs]
                
                if len(xz) == 0:
                    xz = [self._xz[0], self._xz[-1]]
                
                if xz[0][0] != self.x[0]:
                    xz.insert(0, self.xz[0])

                if xz[-1][0] != self.x[-1]:
                    xz.append(self.xz[-1])

                return xz, f(xz)
        
    def solve(self, z, x0):
        if not isinstance(z, (int, float)) or not isinstance(x0, (int, float)):
            return
        
        if min(self.x) <= x0 <= max(self.x):
            f = interp1d(self.x, self.z, kind='cubic')
            F = lambda x: float(f(x) - z)
            
            try:
                return float(fsolve(F, x0))
            
            except:
                return
            
    def summarize(self, decimals=3):
        if isinstance(decimals, int):
            if decimals > 3:
                decimals = 3
        
            print("+---------------------------------+")
            print("|", f"{self._title[0:31]}".center(31), "|")
            print("|", f"{len(self._xz)} vertices".center(31) , "|")
            print("+=================================+")
            print("|", "2D length".center(13), "|", f"{round(self.length('2D'), decimals)} m".center(15), "|")
            print("+---------------+-----------------+")
            print("|", "3D length".center(13), "|", f"{round(self.length('3D'), decimals)} m".center(15), "|")
            print("+---------------+-----------------+")
            print("|", "z min".center(13), "|", f"{round(self.z_min, decimals)} m".center(15), "|")
            print("+---------------+-----------------+")
            print("|", "z max".center(13), "|", f"{round(self.z_max, decimals)} m".center(15), "|")
            print("+---------------+-----------------+")
            print("|", "dz".center(13), "|", f"{round(sum(self.dz), decimals)} m".center(15), "|")
            print("+---------------+-----------------+")
            print("|", "dz > 0".center(13), "|", f"{round(sum([dz for dz in self.dz if dz > 0]), decimals)} m".center(15), "|")
            print("+---------------+-----------------+")
            print("|", "dz < 0".center(13), "|", f"{round(sum([dz for dz in self.dz if dz < 0]), decimals)} m".center(15), "|")
            print("+---------------+-----------------+")
        
    def translate(self, dx=0, dz=0):
        translated_zprofile = self.duplicate()
        translated_zprofile.title += " translated"
        
        xz = translated_zprofile.xz
        
        if not isinstance(dx, (int, float)) or not isinstance(dz, (int, float)):
            return
                
        xz = [(x + dx, z + dz) for x, z in xz]
        
        translated_zprofile.xz = xz
        
        return translated_zprofile
        
    def truncate(self, **kwargs):
        truncated_zprofile = self.duplicate()
        truncated_zprofile.title += " truncated"

        if 'indexes' in kwargs.keys():
            if not isinstance(kwargs['indexes'], tuple):
                return
            
            if not 1 < len(kwargs['indexes']):
                return
            
            indexes = kwargs['indexes']
            
            if not isinstance(indexes[0], int) or not isinstance(indexes[1], int):
                return
            
            i_start = indexes[0]
            i_end = indexes[1]
            
            if not 0 <= i_start < i_end < len(self._xz):
                return
            
            truncated_zprofile.xz = self._xz[i_start:i_end+1]
            
            return truncated_zprofile                
                
        elif 'distances' in kwargs.keys():            
            if not isinstance(kwargs['distances'], tuple):
                return
            
            if not 1 < len(kwargs['distances']):
                return
            
            distances = kwargs['distances']

            if not isinstance(distances[0], (int, float)) or not isinstance(distances[1], (int, float)):
                return

            x_start = distances[0]
            x_end = distances[1]

            if not self.x[0] <= x_start < x_end <= self.x[-1]:
                return

            truncated_zprofile.add_point((x_start, truncated_zprofile.interpolate(x_start)))
            truncated_zprofile.add_point((x_end, truncated_zprofile.interpolate(x_end)))

            i_start = truncated_zprofile.x.index(x_start)
            i_end = truncated_zprofile.x.index(x_end)

            xz = truncated_zprofile.xz[i_start:i_end+1]
            truncated_zprofile.xz = xz

            return truncated_zprofile
        
        else:
            return
                
    def update(self):
        x = [x for x, z in self._xz]
        z = [z for x, z in self._xz]

        self._line.set_data(x, z)

        if self.active and self.visible:
            self._line.set_label(self._label)
        else:
            self._line.set_label("")

        self._line.set_linestyle(line_styles[self._line_style])
        
        self._line.set_color(colors[self._line_color])
        
        self._line.set_linewidth(self._line_thickness)

        self._line.set_marker(marker_styles[self._marker_style])
        
        self._line.set_markeredgecolor(colors[self._marker_color])
        
        self._line.set_markerfacecolor(colors[self._marker_color])
        
        self._line.set_markersize(self._marker_size)

        self._line.set_alpha(self._opacity)
        
        self._line.set_zorder(self._order)

        self._line.set_visible(self._active and self._visible)

    @property
    def xz(self):
        return list(self._xz)

    @xz.setter
    def xz(self, xz):
        if isinstance(xz, list):
            if len(xz) > 1:
                valid = True
                for x, z in xz:
                    if not (isinstance(x, (int, float)) and isinstance(z, (int, float))):
                        valid = False
                        break
                if valid:
                    xz.sort()
                    self._xz = xz

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str):
            self._title = title

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, label):
        if isinstance(label, str):
            self._label = label

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, active):
        if isinstance(active, bool):
            self._active = active

    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, visible):
        if isinstance(visible, bool):
            self._visible = visible

    @property
    def line(self):
        return self._line

    @property
    def line_style(self):
        return self._line_style

    @line_style.setter
    def line_style(self, style):
        if style in line_styles.keys():
            self._line_style = style

    @property
    def line_color(self):
        return self._line_color

    @line_color.setter
    def line_color(self, color):
        if color in colors.keys():
            self._line_color = color

    @property
    def line_thickness(self):
        return self._line_thickness

    @line_thickness.setter
    def line_thickness(self, thickness):
        if isinstance(thickness, (int, float)):
            if 0 <= thickness < 100:
                self._line_thickness = thickness

    @property
    def marker_style(self):
        return self._marker_style

    @marker_style.setter
    def marker_style(self, style):
        if style in marker_styles.keys():
            self._marker_style = style

    @property
    def marker_color(self):
        return self._marker_color

    @marker_color.setter
    def marker_color(self, color):
        if color in colors.keys():
            self._marker_color = color

    @property
    def marker_size(self):
        return self._marker_size

    @marker_size.setter
    def marker_size(self, size):
        if isinstance(size, (int, float)):
            if 0 <= size < 100:
                self._marker_size = size 

    @property
    def opacity(self):
        return self._opacity

    @opacity.setter
    def opacity(self, opacity):
        if isinstance(opacity, (int, float)):
            if 0 <= opacity <= 1:
                self._opacity = opacity
    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, order):
        if isinstance(order, int):
            if 0 < order < 100:
                self._order = order

    @property
    def x(self):
        return [x for x, z in self._xz]
    
    @property
    def z_min(self):
        return min(self.z)
    
    @property
    def z_max(self):
        return max(self.z)

    @property
    def z(self):
        return [z for x, z in self._xz]
    
    @property
    def dz(self):
        dz = []
        for i in range(1, len(self._xz)):
            dz.append(self.z[i] - self.z[i-1])
        return dz

    def __repr__(self):
        return f"{self._title}"

    def __del__(self):
        zProfile._counter -= 1

    def __getstate__(self):
        attributes = dict(self.__dict__)
        attributes["_line"] = Line2D([], [])

        return attributes