import json

from matplotlib.text import Text as mpl_Text

from pyLong.dictionnaries.colors import colors
from pyLong.lists.fonts import font_styles, font_weights
from pyLong.annotations.annotation import Annotation
from pyLong.profiles.zprofile import zProfile

class Text(Annotation):
    _counter = 0

    def __init__(self):
        Text._counter += 1

        Annotation.__init__(self)

        self._xy = (500., 500.)

        self._title = "new text"

        self._text = ""
        
        self._rotation = 0.

        self._annotation = mpl_Text(0,
                                    0,
                                    "",
                                    rotation=0,
                                    rotation_mode="anchor",
                                    horizontalalignment="left",
                                    verticalalignment="baseline")

        self._font_size = 9.

        self._font_color = "Black"

        self._font_style = "normal"

        self._font_weight = "normal"

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
         self._annotation = mpl_Text(0,
                                    0,
                                    "",
                                    rotation=0,
                                    rotation_mode="anchor",
                                    horizontalalignment="left",
                                    verticalalignment="baseline")

    def copy_style(self, annotation):
        if isinstance(annotation, Text):
            self._font_size = annotation.font_size
            self._font_color = annotation.font_color
            self._font_style = annotation.font_style
            self._font_weight = annotation.font_weight
            self._rotation = annotation.rotation
            self._opacity = annotation.opacity
            self._order = annotation.order

    def duplicate(self):
        annotation = Text()
        annotation.copy_style(self)

        annotation.title = self._title + " duplicated"
        annotation.text = self._text

        annotation.xy = self._xy

        return annotation

    def export_style(self, filename):
        style = {'font_size': self._font_size,
                 'font_color': self._font_color,
                 'font_style': self._font_style,
                 'font_weight': self._font_weight,
                 'rotation': self._rotation,
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
                    if 'font_size' in style.keys():
                        self.font_size = style['font_size']
                    if 'font_color' in style.keys():
                        self.font_color = style['font_color']
                    if 'font_style' in style.keys():
                        self.font_style = style['font_style']
                    if 'font_weight' in style.keys():
                        self.font_weight = style['font_weight']
                    if 'rotation' in style.keys():
                        self.rotation = style['rotation']
                    if 'visible' in style.keys():
                        self.visible = style['visible']
                    if 'opacity' in style.keys():
                        self.opacity = style['opacity']
                    if 'order' in style.keys():
                        self.order = style['order']
            
    def plot(self, ax):
        self.clear()
        self.update()

        ax.add_artist(self._annotation)

    def reverse(self, profile):
        if isinstance(profile, zProfile):
            x_mean = (min(profile.x) + max(profile.x)) / 2
            self.x = 2 * x_mean - self.x

    def update(self):
        self._annotation.set_text(self._text)
        self._annotation.set_x(self._xy[0])
        self._annotation.set_y(self._xy[1])
        self._annotation.set_fontsize(self._font_size)
        self._annotation.set_fontstyle(self._font_style)
        self._annotation.set_color(colors[self._font_color])
        self._annotation.set_fontweight(self._font_weight)
        self._annotation.set_rotation(self._rotation)
        self._annotation.set_alpha(self._opacity)
        self._annotation.set_zorder(self._order)
        self._annotation.set_visible(self._visible)

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
        if isinstance(z, (int, float)):
            self._xy = (self._xy[0], y)

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        if isinstance(text, str):
            self._text = text
            
    @property
    def rotation(self):
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        if isinstance(rotation, (int, float)):
            if 0 <= rotation <= 360:
                self._rotation = rotation

    @property
    def annotation(self):
        return self._annotation

    @property
    def font_size(self):
        return self._font_size

    @font_size.setter
    def font_size(self, size):
        if isinstance(size, (int, float)):
            if 0 <= size:
                self._font_size = size

    @property
    def font_color(self):
        return self._font_color

    @font_color.setter
    def font_color(self, color):
        if color in colors.keys():
            self._font_color = color

    @property
    def font_style(self):
        return self._font_style

    @font_style.setter
    def font_style(self, style):
        if style in font_styles:
            self._font_style = style

    @property
    def font_weight(self):
        return self._font_weight

    @font_weight.setter
    def font_weight(self, weight):
        if weight in font_weights:
            self._font_weight = weight 

    def __repr__(self):
        return f"{self._title}"

    def __del__(self):
        Text._counter -= 1

    def __getstate__(self):
        attributes = dict(self.__dict__)
        attributes["_annotation"] = mpl_Text(0,
                                             0,
                                             "",
                                             rotation=0,
                                             rotation_mode="anchor",
                                             horizontalalignment="left",
                                             verticalalignment="baseline")

        return attributes