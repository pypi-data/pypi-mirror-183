import enum
import json

from matplotlib.patches import Polygon as mpl_Polygon
import numpy as np

from pyLong.dictionnaries.styles import line_styles
from pyLong.dictionnaries.colors import colors
from pyLong.lists.hatches import hatch_styles
from pyLong.annotations.annotation import Annotation
from pyLong.profiles.zprofile import zProfile


class Polygon(Annotation):
    _counter = 0

    def __init__(self):
        Polygon._counter += 1

        Annotation.__init__(self)

        self._xy = [(200, 200), (800, 200), (500, 800)]

        self._title = "new polygon"

        self._label = ""

        self._polygon = mpl_Polygon(np.random.rand(3, 2), closed=True)

        self._line_style = "solid"
        
        self._line_thickness = 1.

        self._line_color = "Black"

        self._hatch_style = "/"

        self._hatch_density = 1

        self._fill_color = "None"

    """
    Methods:
    - clear
    - copy_style
    - duplicate
    - export_style
    - import_style
    - plot
    - reverse
    - update
    """

    def clear(self):
        self._polygon = mpl_Polygon(np.random.rand(3, 2), closed=True)

    def copy_style(self, annotation):
        if isinstance(annotation, Polygon):
            self._line_style = annotation.line_style
            self._line_color = annotation.line_color
            self._line_thickness = annotation.line_thickness
            self._hatch_style = annotation.hatch_style
            self._hatch_density = annotation.hatch_density
            self._fill_color = annotation.fill_color

    def duplicate(self):
        annotation = Polygon()
        annotation.copy_style(self)

        annotation.title = self._title + " duplicate"
        annotation.label = self._label

        annotation.xy = self._xy

        return annotation 

    def export_style(self, filename):
        style = {'line_style': self._line_style,
                 'line_color': self._line_color,
                 'line_thickness': self._line_thickness,
                 'hatch_style': self._hatch_style,
                 'hatch_density': self._hatch_density,
                 'fill_color': self._fill_color,
                 'visible': self._visible,
                 'opacity': self._opacity,
                 'order': self._order}

        if isinstance(filename, str):
            if len(filename) > 0:
                with open(filename, 'w') as file:
                    json.dump(style, file, indent=0)

    def import_style(self, filename):
        if isinstance(filename, str):
            if len(filename) > 0:
                with open(filename, 'r') as file:
                    try:
                        style = json.load(file)
                    except json.JSONDecodeError:
                        return

                if isinstance(style, dict):
                    if 'line_style' in style.keys():
                        self.line_style = style['line_style']
                    if 'line_color' in style.keys():
                        self.line_color = style['line_color']
                    if 'line_thickness' in style.keys():
                        self.line_thickness = style['line_thickness']
                    if 'hatch_style' in style.keys():
                        self.hatch_style = style['hatch_style']
                    if 'hatch_density' in style.keys():
                        self.hatch_density = style['hatch_density']
                    if 'fill_color' in style.keys():
                        self.fill_color = style['fill_color']
                    if 'visible' in style.keys():
                        self.visible = style['visible']
                    if 'opacity' in style.keys():
                        self.opacity = style['opacity']
                    if 'order' in style.keys():
                        self.order = style['order']

    def plot(self, ax):
        self.clear()
        self.update()

        ax.add_patch(self._polygon)

    def reverse(self, profile):
        if isinstance(profile, zProfile):
            x_mean = (min(profile.x) + max(profile.x)) / 2
            xy = self.xy
            for i in range(len(xy)):
                xy[i] = (2 * x_mean - xy[i][0], xy[i][1])

            self.xy = xy

    def update(self):
        xy = np.zeros((len(self._xy), 2))
        for i, (x, y) in enumerate(self._xy):
            xy[i, 0], xy[i, 1] = x, y

        self._polygon.set_xy(xy)

        if self._visible:
            self._polygon.set_label(self._label)
        else:
            self._polygon.set_label("")

        self._polygon.set_linestyle(line_styles[self._line_style])
        self._polygon.set_linewidth(self._line_thickness)
        self._polygon.set_edgecolor(colors[self._line_color])
        self._polygon.set_facecolor(colors[self._fill_color])
        self._polygon.set_hatch(self._hatch_density * self._hatch_style)
        self._polygon.set_alpha(self._opacity)
        self._polygon.set_zorder(self._order)
        self._polygon.set_visible(self._visible)  

    @property
    def xy(self):
        return list(self._xy)

    @xy.setter
    def xy(self, xy):
        valid = False
        if isinstance(xy, list):
            for item in xy:
                if isinstance(item, tuple):
                    if len(item) == 2:
                        if isinstance(item[0], (int, float)) and isinstance(item[1], (int, float)):
                            valid = True

        if valid:
            self._xy = xy

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, label):
        if isinstance(label, str):
            self._label = label

    @property
    def polygon(self):
        return self._polygon

    @property
    def line_style(self):
        return self._line_style

    @line_style.setter
    def line_style(self, style):
        if style in line_styles.keys():
            self._line_style = style

    @property
    def line_thickness(self):
        return self._line_thickness

    @line_thickness.setter
    def line_thickness(self, thickness):
        if isinstance(thickness, (int, float)):
            if 0 <= thickness:
                self._line_thickness = thickness
            
    @property
    def line_color(self):
        return self._line_color

    @line_color.setter
    def line_color(self, color):
        if color in colors.keys():
            self._line_color = color

    @property
    def hatch_style(self):
        return self._hatch_style

    @hatch_style.setter
    def hatch_style(self, style):
        if style in hatch_styles:
            self._hatch_style = style

    @property
    def hatch_density(self):
        return self._hatch_density

    @hatch_density.setter
    def hatch_density(self, density):
        if isinstance(density, int):
            if 0 < density:
                self._hatch_density = density

    @property
    def fill_color(self):
        return self._fill_color

    @fill_color.setter
    def fill_color(self, color):
        if color in colors.keys():
            self._fill_color = color

    def __repr__(self):
        return f"{self._title}"

    def __del__(self):
        Polygon._counter -= 1   

    def __getstate__(self):
        attributes = dict(self.__dict__)
        attributes["_polygon"] = mpl_Polygon(np.random.rand(3, 2), closed=True)

        return attributes        