from math import ceil


class Dictionary:
    def __init__(self):
        self.len = 8
        self.list = [None for _ in range(self.len)]
        self.counter = 0

    def __setitem__(self, key, value):
        capacity = ceil((2 * self.len) / 3)

        if capacity == self.counter:
            self.resize()

        element_cell = hash(key) % self.len

        for _ in self.list:
            if self.list[element_cell % self.len] is None or\
                    self.list[element_cell % self.len] == key:
                self.list[element_cell % self.len] = [key, hash(key), value]
                self.counter += 1
                break
            else:
                if element_cell == self.len:
                    element_cell = 0
                else:
                    element_cell += 1

    def __getitem__(self, key):
        for lst in self.list:
            if lst is not None:
                if key == lst[0]:
                    return lst[2]

    def __len__(self):
        return self.counter

    def resize(self):
        self.len *= 2

        main_list = self.list.copy()
        self.list = [None for _ in range(self.len)]

        for item in main_list:
            if item is not None:
                element_cell = hash(item[0]) % self.len
                self.list[element_cell % self.len] = item
