from copy import deepcopy


class Dictionary:
    def __init__(self):
        self.capacity = 8
        self.threshold = int(self.capacity * 2 / 3)
        self.table = [[] for _ in range(self.capacity)]
        self.length = 0

    def __getitem__(self, key):
        hash_key = hash(key)
        get_ind = hash_key % self.capacity

        while True:
            if not self.table[get_ind]:
                raise KeyError

            try:
                if self.table[get_ind][0] == key and \
                        self.table[get_ind][2] == hash_key:
                    return self.table[get_ind][1]
            except IndexError:
                raise KeyError
            get_ind = (get_ind + 1) % self.capacity

    def __setitem__(self, key, value):
        if self.length == self.threshold:
            self.upgrade_table()

        hash_key = hash(key)
        ind = hash_key % self.capacity

        while True:
            if not self.table[ind]:
                self.table[ind] = [key, value, hash_key]
                self.length += 1
                break

            if hash_key == self.table[ind][2] and \
                    key == self.table[ind][0]:
                self.table[ind][1] = value
                break

            ind = (ind + 1) % self.capacity

    def upgrade_table(self):
        copy_table = deepcopy(self.table)
        self.length = 0
        self.capacity *= 2
        self.threshold = int(self.capacity * 2 / 3)
        self.table = [[] for _ in range(self.capacity)]
        for element in copy_table:
            if element:
                self.__setitem__(element[0], element[1])

    def __len__(self):
        return self.length

    def get(self, key):
        return self.__getitem__(key)

    def clear(self):
        self.capacity = 8
        self.threshold = int(self.capacity * 2 / 3)
        self.length = 0
        self.table = [[] for _ in range(self.capacity)]
