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

                if self.base_data[index_][0] == key and\
                        self.base_data[index_][1] == hash(key):
                    self.base_data[index_] = [key, hash(key), value]
                    self.length -= 1
                    a = 1
                index_ = (index_ + 1) % self.capacity
            if a != 1:
                self.base_data[index_] = [key, hash(key), value]
        self.length += 1

    def __getitem__(self, key):
        if self.length != 0:
            index_ = hash(key) % self.capacity
            while self.base_data[index_] is not None\
                    and (index_ < self.capacity):
                if self.base_data[index_][0] == key and \
                        self.base_data[index_][1] == hash(key):
                    return self.base_data[index_][2]

                index_ = (index_ + 1) % self.capacity

        raise KeyError(f"Not Key {key} ")

    def __len__(self):
        return int(self.length)

    def resize(self):
        self.capacity *= 2
        self.threshold = int(self.capacity * (2 / 3))
        data_ = []
        for member in self.base_data:
            if member is not None:
                data_.append(member)

        self.base_data = [
            None for i in range(self.capacity)]
        self.length = 0
        for member in data_:
            self.__setitem__(member[0], member[2])

    def clear(self):
        self.base_data = [
            None for i in range(self.capacity)]

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
    pass
