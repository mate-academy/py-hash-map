class Dictionary:
    LOAD_FACTOR = 2 / 3
    RESIZE = 2
    DEFAULT_CAPACITY = 8

    def __init__(self):
        self.capacity = 8
        self.storage = [[] for _ in range(self.DEFAULT_CAPACITY)]
        self.length = 0

    def resize(self):
        saved_storage = self.storage[:]
        self.length = 0
        self.capacity *= self.RESIZE
        self.storage = [[] for _ in range(self.capacity)]

        for item in saved_storage:
            if len(item) != 0:
                self.__setitem__(item[0], item[1])

    def __setitem__(self, key, value):
        if self.length == int(self.capacity * self.LOAD_FACTOR):
            self.resize()

        hashed_value = hash(key)
        index = hashed_value % self.capacity

        while True:
            if not self.storage[index]:
                self.storage[index] = [key, value, hashed_value]
                self.length += 1
                return
            elif hashed_value == self.storage[index][2] and \
                    key == self.storage[index][0]:
                self.storage[index][1] = value
                return
            elif self.storage[index][2] is True:
                self.storage[index] = [key, value, hashed_value]
                self.length += 1
                return
            index = (index + 1) % self.capacity

    def __getitem__(self, key):
        hashed_value = hash(key)
        index = hashed_value % self.capacity

        if self.length:
            while self.storage[index]:
                if self.storage[index][0] == key \
                        and self.storage[index][2] is True:
                    raise KeyError

                if hashed_value == self.storage[index][2] and \
                        self.storage[index][0] == key:
                    return self.storage[index][1]
                index = (index + 1) % self.capacity

        raise KeyError

    def __len__(self):
        return self.length

    def __delitem__(self, key):
        hashed_value = hash(key)
        index = hashed_value % self.capacity

        while self.storage[index]:
            if hashed_value == self.storage[index][2] and \
                    key == self.storage[index][0]:
                return_value = self.storage[index][1]
                self.storage[index][2] = True
                self.length -= 1
                return return_value
            index = (index + 1) % self.capacity

        raise KeyError

    def get(self, key, default=None):
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    def pop(self, key):
        try:
            return self.__delitem__(key)
        except (KeyError, IndexError):
            raise

    def clear(self):
        self.length = 0
        self.storage = [[] for _ in range(self.DEFAULT_CAPACITY)]

    def __contains__(self, key):
        hashed_value = hash(key)
        index = hashed_value % self.capacity

        if index > self.capacity:
            return False

        try:
            self.__getitem__(key)
        except KeyError:
            return False
        else:
            return True

    def __iter__(self):
        for item in self.storage:
            if len(item) != 0:
                yield item[:-1]

    def update(self, _m=None, **kwargs):
        try:
            if _m is not None:
                for k, v in _m.items():
                    self.__setitem__(k, v)

            for k, v in kwargs.items():
                self.__setitem__(k, v)
        except KeyError:
            raise
