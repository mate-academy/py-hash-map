class Point:
    def __init__(self, point_x: int, point_y: int) -> None:
        self._point_x = point_x
        self._point_y = point_y

    def __eq__(self, other: int) -> bool:
        if not isinstance(other, Point):
            return False
        return self.point_x == other.point_x and self.point_y == other.point_y

    def __hash__(self) -> int:
        # Change the implementation of the hash to debug your code.
        # For example, you can return self.x + self.y as a hash
        # which is NOT a best practice, but you will be able to predict
        # a hash value by coordinates of the point and its index
        # in the hashtable as well
        return hash((self.point_x, self.point_y))

    @property
    def point_x(self) -> int:
        return self._point_x

    @property
    def point_y(self) -> int:
        return self._point_y
