class Annotation:
    def __init__(self):
        self._title = ""

        self._visible = True

        self._opacity = 1.

        self._order = 1

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str):
            self._title = title

    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, visible):
        if isinstance(visible, bool):
            self._visible = visible

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
            if 0 < order:
                self._order = order