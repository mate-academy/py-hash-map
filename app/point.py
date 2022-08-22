from app.main import Dictionary


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        # Change the implementation of the hash to debug your code.
        # For example, you can return self.x + self.y as a hash
        # which is NOT a best practice, but you will be able to predict
        # a hash value by coordinates of the point and its index
        # in the hashtable as well
        return self.x + self.y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


point_1 = Point(1, 2)
point_2 = Point(2, 3)
point_3 = Point(4, 5)
point_4 = Point(4, 5)
point_5 = Point(5, 4)
point_6 = Point(4, 4)
point_7 = Point(4, 4)

dic = Dictionary()
dic[point_1.x] = point_1.y
dic[point_2.x] = point_2.y
dic[point_3.x] = point_3.y
dic[point_4.x] = point_4.y
dic[point_5.x] = point_5.y
dic[point_6.x] = point_6.y

print(dic.__dict__)
