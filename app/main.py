from app.point import Point


class Dictionary:
    def __init__(self):
        self.initial_capacity = 8
        self.storage = [[] for _ in range(self.initial_capacity)]
        self.length = 0
        self.load_factor = 2 / 3
        self.resize = 2

    def is_resize(self):
        return True if self.length == int(self.initial_capacity * self.load_factor) else False

    def check_resize(self):
        save_storage = self.storage[:]
        re_size = int(self.initial_capacity * self.load_factor)
        if self.length == re_size:
            self.length = 0
            self.initial_capacity *= self.resize
            self.storage = [[] for _ in range(self.initial_capacity)]
        for sub_list in save_storage:
            for el in sub_list:
                self.__setitem__(el[0], el[1])

    def __setitem__(self, key, value):
        if self.is_resize():
            self.check_resize()

        index = hash(key) % self.initial_capacity
        for ele in self.storage[index]:
            if key == ele[0]:
                ele[1] = value
                break
        else:
            self.storage[index].append([key, value])
            self.length += 1

    def __getitem__(self, key):
        index = hash(key) % self.initial_capacity
        for ele in self.storage[index]:
            if ele[0] == key:
                return ele[1]
        raise KeyError

    def __delitem__(self, key):
        index = hash(key) % self.initial_capacity
        for sub_lst in self.storage[index]:
            if key == sub_lst[0]:
                self.storage[index].remove(sub_lst)
                self.length -= 1
                return
        raise KeyError

    def __len__(self):
        return self.length

    def __contains__(self, key):
        index = hash(key) % self.initial_capacity
        for el in self.storage[index]:
            if el[0] == key:
                return True
        return False

    def __iter__(self):
        for sub_list in self.storage:
            if not sub_list:
                continue
            for key in sub_list:
                yield key[0]

    def get(self, key):
        try:
            return self.__getitem__(key)
        except KeyError:
            raise KeyError

    def pop(self, key):
        try:
            return self.__delitem__(key)
        except KeyError:
            raise KeyError

    def clear(self):
        for el in range(len(self.storage)):
            self.storage[el] = []
        self.length = 0

    def update(self, upd_lst):
        try:
            return self.__setitem__(upd_lst[0], upd_lst[1])
        except KeyError:
            raise KeyError
