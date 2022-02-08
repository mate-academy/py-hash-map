class Dictionary:
    LOAD_FACTOR = 2 / 3
    RESIZE = 2

    def __init__(self):
        self.initial_capacity = 8
        self.storage = [[] for _ in range(self.initial_capacity)]
        self.length = 0

    def resize(self):
        saved_storage = self.storage[:]
        load = int(self.initial_capacity * self.LOAD_FACTOR)

        if load == self.length:
            self.length = 0
            self.initial_capacity *= self.RESIZE
            self.storage = [[] for _ in range(self.initial_capacity)]
        for item in saved_storage:
            if len(item) != 0:
                self.__setitem__(item[0], item[1])

    def __setitem__(self, key, value):
        if self.length == int(self.initial_capacity * self.LOAD_FACTOR):
            self.resize()

        hashed_value = hash(key)

        index = hashed_value % self.initial_capacity

        if len(self.storage[index]) != 0:
            if key == self.storage[index][0] and\
                    hashed_value == self.storage[index][2]:
                self.storage[index][1] = value
            else:
                while True:
                    index += 1
                    if index == self.initial_capacity:
                        index = 0
                        continue
                    elif len(self.storage[index]) == 0:
                        self.length += 1
                        self.storage[index] = [key, value, hashed_value]
                        break
        else:
            self.storage[index] = [key, value, hashed_value]
            self.length += 1

    def __getitem__(self, key):
        hashed_value = hash(key)
        index = hashed_value % self.initial_capacity

        if key == self.storage[index][0] and\
                hashed_value == self.storage[index][2]:
            return self.storage[index][1]
        else:
            counter = 0
            while counter <= self.initial_capacity:
                index += 1
                if index == self.initial_capacity:
                    index = 0
                    continue
                if key == self.storage[index][0] and\
                        hashed_value == self.storage[index][2]:
                    return self.storage[index][1]
                counter += 1
            raise KeyError

    def __len__(self):
        return self.length

    def __delitem__(self, key):
        hashed_value = hash(key)
        index = hashed_value % self.initial_capacity

        for _ in self.storage[index]:
            if key == self.storage[index][0] and\
                    hashed_value == self.storage[index][2]:
                self.storage[index] = []
                self.length -= 1
                return
            else:
                counter = 0
                while counter <= self.initial_capacity:
                    index += 1
                    if index == self.initial_capacity:
                        index = 0
                        continue
                    if key == self.storage[index][0] and\
                            hashed_value == self.storage[index][2]:
                        self.storage[index] = []
                        self.length -= 1
                        return
                    counter += 1
        raise KeyError

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
        self.storage = [[] for _ in range(self.initial_capacity)]

    def __contains__(self, key):
        hashed_value = hash(key)
        index = hashed_value % self.initial_capacity

        if hashed_value > self.initial_capacity:
            return False

        if key == self.storage[index][0] and\
                hashed_value == self.storage[index][2]:
            return True
        else:
            counter = 0
            while counter <= self.initial_capacity:
                index += 1
                if index == self.initial_capacity:
                    index = 0
                    continue
                if key == self.storage[index][0] and\
                        hashed_value == self.storage[index][2]:
                    return True
                counter += 1
        return False

    def __iter__(self):
        for item in self.storage:
            if len(item) != 0:
                yield item[:-1]

    def update(self, upd_data):
        return self.__setitem__(upd_data[0], upd_data[1])
