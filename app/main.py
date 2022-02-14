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
            index = (index + 1) % self.capacity

    def __getitem__(self, key):
        hashed_value = hash(key)
        index = hashed_value % self.capacity

        for _ in range(self.capacity):
            if len(self.storage[index]) != 0:
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

        for _ in self.storage[index]:
            if hashed_value == self.storage[index][2] and \
                    key == self.storage[index][0]:
                return_index = self.storage[index][1]
                self.storage[index] = []
                self.length -= 1
                return return_index
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

        for _ in range(self.capacity):
            if len(self.storage[index]) != 0:
                if hashed_value == self.storage[index][2] and \
                        self.storage[index][0] == key:
                    return True
            index = (index + 1) % self.capacity
        return False

    def __iter__(self):
        for item in self.storage:
            if len(item) != 0:
                yield item[:-1]

    def update(self, upd_data):
        return self.__setitem__(upd_data[0], upd_data[1])


if __name__ == "__main__":
    d = Dictionary()

    d[1] = 'one'
    d[2] = 'two'
    d[3] = 'three'
    d[11] = '3'
    print(d.__dict__)

    print(d.__getitem__(11))
