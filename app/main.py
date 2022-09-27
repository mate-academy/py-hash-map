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


class Dictionary:

    def __init__(self):
        self.capacity = 8
        self.size = 0
        self.threshold = int(self.capacity * 2 / 3)
        self.hash_table = [None for _ in range(self.capacity)]

    def __setitem__(self, key, value):
        if self.size == self.threshold:
            self.resize()
        hash_ = hash(key)
        index = hash_ % self.capacity
        while True:
            if not self.hash_table[index]:
                self.hash_table[index] = [key, hash_, value]
                self.size += 1
                break
            if self.hash_table[index][0] == key \
                    and self.hash_table[index][1] == hash_:
                self.hash_table[index][2] = value
                break
            index = (index + 1) % self.capacity

    def __getitem__(self, key):
        hash_ = hash(key)
        index = hash_ % self.capacity
        while self.hash_table[index]:
            if self.hash_table[index][0] == key \
                    and self.hash_table[index][1] == hash_:
                return self.hash_table[index][2]
            index = (index + 1) % self.capacity
        raise KeyError(key)

    def resize(self):
        self.capacity *= 2
        self.size = 0
        self.threshold = int(self.capacity * 2 / 3)
        temp_table = self.hash_table.copy()
        self.hash_table = [None for _ in range(self.capacity)]
        for item in temp_table:
            if item:
                self.__setitem__(item[0], item[2])

    def __len__(self):
        return self.size

    def clear(self):
        self.hash_table = [None for _ in range(self.capacity)]
        return self

    def get(self, key, value="None"):
        try:
            return self.__getitem__(key)
        except KeyError:
            return value
