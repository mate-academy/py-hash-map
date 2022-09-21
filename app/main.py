class Dictionary:
    def __init__(self):
        self.capacity = 8
        self.length = 0
        self.load = int(self.capacity * 2 / 3)
        self.table = [[] for _ in range(self.capacity)]

    def __setitem__(self, key, value):
        hashed_key = hash(key)
        index = hashed_key % self.capacity
        while True:
            if self.table[index] == []:
                self.table[index] = [key, value, hashed_key]
                self.length += 1
                break
            if self.table[index][2] == hashed_key\
                    and self.table[index][0] == key:
                self.table[index][1] = value
                break
            index = (index + 1) % self.capacity
        if self.length == self.load:
            self.resize()

    def resize(self):
        self.capacity *= 2
        self.length = 0
        self.load = int(self.capacity * 2 / 3)
        prep_table = self.table
        self.table = [[] for _ in range(self.capacity)]
        for element in prep_table:
            if len(element):
                self.__setitem__(element[0], element[1])

    def __len__(self):
        return self.length

    def __getitem__(self, key):
        index = hash(key) % self.capacity
        element = self.table[index]
        list_actual_keys = [_[0] for _ in self.table if _ != []]
        if key not in list_actual_keys:
            raise KeyError
        while True:
            if element[2] == hash(key) and element[0] == key:
                return element[1]
            index = (index + 1) % self.capacity
            element = self.table[index]

    def clear(self):
        self.capacity = 8
        self.length = 0
        self.load = int(self.capacity * 2 / 3)
        self.table = [[] for _ in range(self.capacity)]

    def __delitem__(self, key):
        list_actual_keys = [_[0] for _ in self.table if _ != []]
        if key not in list_actual_keys:
            raise KeyError
        index = hash(key) % self.capacity
        element = self.table[index]
        while True:
            if element[2] == hash(key) and element[0] == key:
                self.table[index] = []
                self.length -= 1
                break
            index = (index + 1) % self.capacity
            element = self.table[index]

    def get(self, key, value=None):
        list_actual_keys = [_[0] for _ in self.table if _ != []]
        if key not in list_actual_keys:
            return value
        if key in list_actual_keys:
            return self.__getitem__(key)

    def pop(self, __key, default=None):
        list_actual_keys = [_[0] for _ in self.table if _ != []]
        if __key in list_actual_keys:
            result = self.__getitem__(__key)
            self.__delitem__(__key)
            return result
        if __key not in list_actual_keys and default is not None:
            return default
        if __key not in list_actual_keys and default is None:
            raise KeyError
