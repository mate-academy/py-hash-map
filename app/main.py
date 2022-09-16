class Dictionary:
    def __init__(self, size=8):
        self.storage = [[] for _ in range(size)]
        self.size = size
        self.length = 0
        self.load_factor = 2 / 3

    def __setitem__(self, key, value):
        storage_idx = hash(key) % self.size

        while True:
            if not self.storage[storage_idx]:
                self.length += 1
                self.storage[storage_idx] = [key, value, hash(key)]
                break
            elif self.storage[storage_idx][0] == key and\
                    self.storage[storage_idx][2] == hash(key):
                self.storage[storage_idx][1] = value
                break
            storage_idx = (storage_idx + 1) % self.size

        if self.length >= self.load_factor * self.size:
            self.resize(self.storage)

    def resize(self, storage):
        self.size *= 2
        self.storage = [[] for _ in range(self.size)]
        for item in storage:
            if item:
                self.__setitem__(item[0], item[1])
                self.length -= 1

    def __getitem__(self, key):
        storage_idx = hash(key) % self.size
        while True:
            if not self.storage[storage_idx]:
                raise KeyError
            elif self.storage[storage_idx][0] == key and\
                    self.storage[storage_idx][2] == hash(key):
                return self.storage[storage_idx][1]
            storage_idx = (storage_idx + 1) % self.size

    def __len__(self):
        return self.length

    def clear(self):
        self.storage = [[] for _ in range(self.size)]
        self.length = 0

    def __delitem__(self, key):
        storage_idx = hash(key) % self.size
        while True:
            if not self.storage[storage_idx]:
                raise KeyError
            elif self.storage[storage_idx][0] == key and\
                    self.storage[storage_idx][2] == hash(key):
                value = self.storage[storage_idx][1]
                self.storage[storage_idx] = []
                self.length -= 1
                break
            storage_idx = (storage_idx + 1) % self.size
        return value

    def update(self, _m=None, **kwargs):
        if isinstance(_m, dict):
            for key in _m.keys():
                self.__setitem__(key, _m[key])
        elif _m:
            for item in _m:
                self.__setitem__(item[0], item[1])
        for key, value in kwargs.items():
            self.__setitem__(key, value)

    def pop(self, key, val=None):
        if self.get(key):
            return self.__delitem__(key)
        elif val:
            return val
        else:
            raise KeyError

    def get(self, key, val=None):
        try:
            return self.__getitem__(key)
        except KeyError:
            return val

    def __iter__(self):
        for item in self.storage:
            if not item:
                continue
            for i in item:
                yield i
