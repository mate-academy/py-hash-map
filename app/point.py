class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return self._x + self._y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
