import json

from matplotlib.patches import Rectangle as mpl_Rectangle

from pyLong.dictionnaries.styles import line_styles
from pyLong.dictionnaries.colors import colors
from pyLong.lists.hatches import hatch_styles
from pyLong.annotations.annotation import Annotation
from pyLong.profiles.zprofile import zProfile


class Rectangle(Annotation):
    _counter = 0

    def __init__(self):
        Rectangle._counter += 1

        Annotation.__init__(self)

        self._xy = (500., 500.)

        self._title = "new rectangle"

        self._label = ""
        
        self._width = 100.

        self._height = 100.
        
        self._rotation = 0.

        self._rectangle = mpl_Rectangle((0, 0), 0, 0, rotation_point='center')

        self._line_style = "solid"

        self._line_color = "Black"

        self._line_thickness = 1.

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
        self._rectangle = mpl_Rectangle((0, 0), 0, 0, rotation_point='center')

    def copy_style(self, annotation):
        if isinstance(annotation, Rectangle):
            self._line_style = annotation.line_style
            self._line_color = annotation.line_color
            self._line_thickness = annotation.line_thickness
            self._hatch_style = annotation.hatch_style
            self._hatch_density = annotation.hatch_density
            self._fill_color = annotation.fill_color

    def duplicate(self):
        annotation = Rectangle()
        annotation.copy_style(self)

        annotation.title = self._title + " duplicated"
        annotation.label = self._label

        annotation.xy = self._xy
        annotation.width = self._width
        annotation.height = self._height

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

        ax.add_patch(self._rectangle)

    def reverse(self, profile):
        if isinstance(profile, zProfile):
            x_mean = (min(profile.x) + max(profile.x)) / 2
            self.x = 2 * x_mean - self.x - self.width

    def update(self):
        self._rectangle.set_xy((self.x - self.width/2, self.y - self.height/2))
        self._rectangle.set_width(self._width)
        self._rectangle.set_height(self._height)

        if self._visible:
            self._rectangle.set_label(self._label)
        else:
            self._rectangle.set_label("")

        self._rectangle.set_linestyle(line_styles[self._line_style])
        self._rectangle.set_linewidth(self._line_thickness)
        self._rectangle.set_edgecolor(colors[self._line_color])
        self._rectangle.set_facecolor(colors[self._fill_color])
        self._rectangle.set_hatch(self._hatch_density * self._hatch_style)
        self._rectangle.set_angle(self._rotation)
        self._rectangle.set_alpha(self._opacity)
        self._rectangle.set_zorder(self._order)
        self._rectangle.set_visible(self._visible)

    @property
    def xy(self):
        return self._xy

    @xy.setter
    def xy(self, xy):
        if isinstance(xy, tuple):
            if len(xy) > 1:
                valid = True
                for value in xy:
                    if not isinstance(value, (int, float)):
                        valid = False
                        break
                if valid:
                    self._xy = xy[0:2]

    @property
    def x(self):
        return self._xy[0]

    @x.setter
    def x(self, x):
        if isinstance(x, (int, float)):
            self._xy = (x, self._xy[1])

    @property
    def y(self):
        return self._xy[1]

    @y.setter
    def y(self, y):
        if isinstance(y, (int, float)):
            self._xy = (self._xy[0], y)

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, label):
        if isinstance(label, str):
            self._label = label
            
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if isinstance(width, (int, float)):
            if 0 <= width:
                self._width = width
                
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if isinstance(height, (int, float)):
            if 0 <= height:
                self._height = height
                
    @property
    def rotation(self):
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        if isinstance(rotation, (int, float)):
            if 0 <= rotation <= 360:
                self._rotation = rotation  

    @property
    def rectangle(self):
        return self._rectangle

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
            if 0 <= thickness:
                self._line_thickness = thickness

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
        Rectangle._counter -= 1   

    def __getstate__(self):
        attributes = dict(self.__dict__)
        attributes["_rectangle"] = mpl_Rectangle((0, 0), 0, 0, rotation_point='center')

        return attributes