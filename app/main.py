import math


class Dictionary:
    RESIZE = 2
    LOAD_FACTOR = 2 / 3

    def __init__(self, capacity=8):
        self.capacity = capacity
        self.ls = [None for _ in range(self.capacity)]
        self.filled = 0

    def __setitem__(self, key, value):
        if self.filled == math.ceil(self.capacity * self.LOAD_FACTOR):
            self.resize()

        hash_value = hash(key)
        index = hash_value % self.capacity

        if self.ls[index] is None:
            self.ls[index] = [key, hash_value, value]
            self.filled += 1
        else:
            if key == self.ls[index][0]:
                self.ls[index][2] = value
                return
            while True:
                index += 1
                index %= self.capacity
                if self.ls[index] is None:
                    self.filled += 1
                    self.ls[index] = [key, hash_value, value]
                    break

    def __getitem__(self, key):
        hash_value = hash(key)
        index = hash_value % self.capacity
        while self.ls[index] is not None:
            cell_key, hash_key, value = self.ls[index]
            if cell_key == key:
                return value
            index += 1
            index %= self.capacity
        raise KeyError

    def resize(self):
        copy_ls = self.ls[:]
        self.filled = 0
        self.capacity *= self.RESIZE
        self.ls = [None for _ in range(self.capacity)]
        for item in copy_ls:
            if item is not None:
                self[item[0]] = item[2]

    def __len__(self):
        return self.filled
