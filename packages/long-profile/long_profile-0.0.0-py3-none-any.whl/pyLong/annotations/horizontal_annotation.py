import json

from matplotlib.text import Text as mpl_Text
from matplotlib.text import Annotation as mpl_Annotation

from pyLong.dictionnaries.styles import line_styles
from pyLong.dictionnaries.colors import colors
from pyLong.lists.arrows import arrow_styles
from pyLong.lists.fonts import font_styles, font_weights
from pyLong.annotations.annotation import Annotation
from pyLong.profiles.zprofile import zProfile


class HorizontalAnnotation(Annotation):
    _counter = 0

    def __init__(self):
        HorizontalAnnotation._counter += 1

        Annotation.__init__(self)

        self._position = (300., 700., 500.)

        self._title = "new horizontal annotation"

        self._text = ""
        
        self._vertical_shift = 0.
        
        self._arrow = mpl_Annotation("",
                                     xy=(0, 0),
                                     xytext=(0, 0),
                                     xycoords='data',
                                     arrowprops=dict(arrowstyle='->'))

        self._annotation = mpl_Text(0,
                                    0,
                                    "",
                                    horizontalalignment='center',
                                    verticalalignment='center')

        self._font_size = 9.

        self._font_color = "Black"

        self._font_style = "normal"

        self._font_weight = "normal"

        self._arrow_style = "-|>"

        self._arrow_line_style = "solid"
        
        self._arrow_thickness = 1.

        self._arrow_color = "Black"

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
        self._arrow = mpl_Annotation("",
                                     xy=(0, 0),
                                     xytext=(0, 0),
                                     xycoords='data',
                                     arrowprops=dict(arrowstyle='->'))

        self._annotation = mpl_Text(0,
                                    0,
                                    "",
                                    horizontalalignment='center',
                                    verticalalignment='center')

    def copy_style(self, annotation):
        if isinstance(annotation, HorizontalAnnotation):
            self._font_size = annotation.font_size
            self._font_color = annotation.font_color
            self._font_style = annotation.font_style
            self._font_weight = annotation.font_weight
            self._vertical_shift = annotation.vertical_shift
            self._arrow_style = annotation.arrow_style
            self._line_style = annotation.line_style
            self._arrow_color = annotation.arrow_color
            self._arrow_thickness = annotation.arrow_thickness
            self._opacity = annotation.opacity
            self._order = annotation.order

    def duplicate(self):
        annotation = HorizontalAnnotation()
        annotation.copy_style(self)

        annotation.title = self._title + " duplicated"
        annotation.text = self._text

        annotation.position = self._position

        return annotation

    def export_style(self, filename):
        style = {'font_size': self._font_size,
                 'font_color': self._font_color,
                 'font_style': self._font_style,
                 'font_weight': self._font_weight,
                 'vertical_shift': self._vertical_shift,
                 'arrow_style': self._arrow_style,
                 'line_style': self._line_style,
                 'arrow_color': self.arrow_color,
                 'arrow_thickness': self.arrow_thickness,
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
                    if 'vertical_shift' in style.keys():
                        self.vertical_shift = style['vertical_shift']
                    if 'arrow_style' in style.keys():
                        self.arrow_style = style['arrow_style']
                    if 'line_style' in style.keys():
                        self.line_style = style['line_style']
                    if 'arrow_color' in style.keys():
                        self.arrow_color = style['arrow_color']
                    if 'arrow_thickness' in style.keys():
                        self.arrow_thickness = style['arrow_thickness']
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
        ax.add_artist(self._arrow)

    def reverse(self, profile):
        if isinstance(profile, zProfile):
            x_mean = (min(profile.x) + max(profile.x)) / 2
            x_start = 2 * x_mean - self.x_start
            x_end = 2 * x_mean - self.x_end

            self.x_start, self.x_end = x_end, x_start

    def update(self):
        self._arrow.arrow_patch.set_arrowstyle(self._arrow_style)
        self._arrow.arrow_patch.set_linestyle(line_styles[self._arrow_line_style])
        self._arrow.arrow_patch.set_linewidth(self._arrow_thickness)
        self._arrow.arrow_patch.set_color(colors[self._arrow_color])
        self._arrow.arrow_patch.set_alpha(self._opacity)
        self._arrow.arrow_patch.set_zorder(self._order)        
        self._arrow.xy = (self._position[0], self._position[2])
        self._arrow.set_x(self._position[1])
        self._arrow.set_y(self._position[2])
        self._arrow.set_alpha(self._opacity)
        self._arrow.set_zorder(self._order)
        self._arrow.set_visible(self._visible)
        
        self._annotation.set_text(self._text)
        self._annotation.set_x(self._x_mean)
        self._annotation.set_y(self._position[2] + self._vertical_shift)
        self._annotation.set_fontsize(self._font_size)
        self._annotation.set_color(colors[self._font_color])
        self._annotation.set_fontweight(self._font_weight)
        self._annotation.set_fontstyle(self._font_style)
        self._annotation.set_alpha(self._opacity)
        self._annotation.set_zorder(self._order)
        self._annotation.set_visible(self._visible)

    @property
    def _x_mean(self):
        return (self._position[0] + self._position[1]) / 2

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        if isinstance(position, tuple):
            if len(position) > 2:
                valid = True
                for value in position:
                    if not isinstance(value, (int, float)):
                        valid = False
                        break
                if valid:
                    self._position = position[0:3]

    @property
    def x_start(self):
        return self._position[0]

    @x_start.setter
    def x_start(self, x):
        if isinstance(x, (int, float)):
            self._position = (x, self.x_end, self.y)

    @property
    def x_end(self):
        return self._position[1]

    @x_end.setter
    def x_end(self, x):
        if isinstance(x, (int, float)):
            self._position = (self.x_start, x, self.y)

    @property
    def y(self):
        return self._position[2]

    @y.setter
    def y(self, y):
        if isinstance(y, (int, float)):
            self._position = (self.x_start, self.x_end, y)

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        if isinstance(text, str):
            self._text = text
            
    @property
    def vertical_shift(self):
        return self._vertical_shift

    @vertical_shift.setter
    def vertical_shift(self, shift):
        if isinstance(shift, (int, float)):
            self._vertical_shift = shift

    @property
    def arrow(self):
        return self._arrow
    
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

    @property
    def arrow_style(self):
        return self._arrow_style

    @arrow_style.setter
    def arrow_style(self, style):
        if style in arrow_styles:
            self._arrow_style = style

    @property
    def arrow_line_style(self):
        return self._arrow_line_style

    @arrow_line_style.setter
    def arrow_line_style(self, style):
        if style in line_styles.keys():
            self._arrow_line_style = style
            
    @property
    def arrow_thickness(self):
        return self._arrow_thickness

    @arrow_thickness.setter
    def arrow_thickness(self, thickness):
        if isinstance(thickness, (int, float)):
            if 0 <= thickness:
                self._arrow_thickness = thickness

    @property
    def arrow_color(self):
        return self._arrow_color

    @arrow_color.setter
    def arrow_color(self, color):
        if color in colors.keys():
            self._arrow_color = color

    def __repr__(self):
        return f"{self._title}"

    def __del__(self):
        HorizontalAnnotation._counter -= 1

    def __getstate__(self):
        attributes = dict(self.__dict__)
        attributes["_arrow"] = mpl_Annotation("",
                                              xy=(0, 0),
                                              xytext=(0, 0),
                                              xycoords='data',
                                              arrowprops=dict(arrowstyle='->'))

        attributes["_annotation"] = mpl_Text(0,
                                             0,
                                             "",
                                             horizontalalignment='center',
                                             verticalalignment='bottom')

        return attributes