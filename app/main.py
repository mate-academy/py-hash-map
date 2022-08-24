class Dictionary:

    def __init__(self):
        self.capacity = 8
        self.threshold = int(self.capacity * (2 / 3))
        self.length = 0
        self.base_data = [None for i in range(self.capacity)]

    def __setitem__(self, key, value):
        a = 0
        if self.length >= self.threshold:
            self.resize()

        index_ = int(hash(key) % self.capacity)
        if self.base_data[index_] is None:
            self.base_data[index_] = [key, hash(key), value]

        elif self.base_data[index_][0] == key:
            self.base_data[index_] = [key, hash(key), value]
            self.length -= 1
        else:

            while self.base_data[index_] is not None:

                if self.base_data[index_][0] == key:
                    self.base_data[index_] = [key, hash(key), value]
                    self.length -= 1
                    a = 1
                if index_ == self.capacity - 1:
                    index_ = -1

                index_ += 1
            if a != 1:
                self.base_data[index_] = [key, hash(key), value]
        self.length += 1

    def __getitem__(self, key):
        if self.length != 0:
            index_ = hash(key) % self.capacity

            while (self.base_data[index_] is not None) or (index_ < self.length):
                if self.base_data[index_][0] == key:
                    return self.base_data[index_][2]

                index_ += 1

            raise KeyError(f"Not Key {key} ")
        else:
            raise KeyError(f"Not Key {key} ")

    def __len__(self):
        return int(self.length)

    def resize(self):
        self.capacity *= 2
        self.threshold = int(self.capacity * (2 / 3))
        data_ = []
        for num in self.base_data:
            if num is not None:
                data_.append(num)

        self.base_data = [None for i in range(self.capacity)]
        self.length = 0
        for number in data_:
            self.__setitem__(number[0], number[2])

    def clear(self):
        self.base_data = [None for i in range(self.capacity)]

    def __delitem__(self, item):
        for i in range(self.length):
            if self.base_data[i][2] == item:
                self.base_data[i] = None

    def pop(self, key):
        for i in range(self.length):
            if self.base_data[i][0] == key:
                self.base_data[i] = None

    def get(self, key):
        self.__getitem__(key)

    def update(self, key, value):
        self.__setitem__(key, value)

    def __iter__(self):
        if self.length != 0:
            counter = 0
            while counter <= self.length:
                yield self.base_data[counter]


if __name__ == "__main__":
    d = Dictionary()
    d.__setitem__("[1, 2, 3]", "y")
    d.__setitem__("j", "i")
    d.__setitem__("j", "123")
    d.__setitem__("k", "l")
    d.__setitem__("hello", "y")
    d.__setitem__("[3, 4]", "y")
    d.__setitem__("j", "y")
    d.__setitem__("1234", "y")
    print(d.__getitem__("j"))
    print(d.__getitem__("k"))
    print(d.__getitem__("j"))
    print(d.__getitem__("b"))
    print(d.__getitem__("1234"))
    print(d.__getitem__("[1, 2, 3]"))
    print(d.__len__())
    d.__iter__()
    d.update("1", "one")
    d.get("1")
    d.pop("1")
    d.__delitem__("y")
    d.clear()
