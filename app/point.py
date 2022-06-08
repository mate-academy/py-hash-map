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


if __name__ == "__main__":
    d = Dictionary()
    print(d)

    a = Point(2, 3)
    b = Point(3, 2)

    d[a] = "Point(2, 3)"

    d[b] = "Point(3, 2)"

    for el in d:
        print(el)

    print(d)
    print("key:", a, "value:", d[a])

    d[a] = 123

    print(d)
    print("key:", a, "value:", d[a])
    print("id:", id(d))

    d1 = Dictionary()

    d1[a] = 222
    d1[b] = 333
    d1["c"] = 444

    d.update(d1)
    print("after update", d)

    del d[a]
    print("after del", d)

    d.clear()
    print(d)
    print("id:", id(d))
