from typing import Any
from app.main import Dictionary


class Point:
    def __init__(self, x: float, y: float) -> None:
        self._x = x
        self._y = y

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        # Change the implementation of the hash to debug your code.
        # For example, you can return self.x + self.y as a hash
        # which is NOT a best practice, but you will be able to predict
        # a hash value by coordinates of the point and its index
        # in the hashtable as well
        return hash((self.x + self.y))

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y


# point = Point(2, 1)
# point2 = Point(1, 2)
# point3 = Point(0, 3)
# dictionary = Dictionary()
# dictionary["point"] = "ApointA" #1+
# dictionary[point] = "point" #2
# dictionary[point2] = "bbb" #3 +
# dictionary["point5"] = 798978 #4
# dictionary["point3"] = 5523 #5
# dictionary["point4"] = "66666" #6

# dictionary["point3"] = "AAAAAAAAA"
# dictionary["point4"] = "FFFFFF"

#
# print(dictionary["point"])
# print(dictionary[point])
# print(dictionary[point2])
# print(dictionary["point5"])
# print(dictionary["point3"])
# print(dictionary["point4"])
#
# print(dictionary)
#
# print(dictionary.__dict__)

# def resize_bucket():
#     items = [(f"Element {i}", i) for i in range(1000)]
#     dictionary = Dictionary()
#     for key, value in items:
#         dictionary[key] = value
#
#     for key, value in items:
#         assert dictionary[key] == value
# resize_bucket()