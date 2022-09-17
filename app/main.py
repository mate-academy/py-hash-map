class Dictionary:
    def __init__(self):
        self.capacity = 8
        self.length = 0
        self.hash_table = [[] for _ in range(self.capacity)]

    def __len__(self):
        return self.length

    def __setitem__(self, key, value):
        if self.length >= self.capacity * 2 / 3:
            self.resize()
        hash_key = hash(key)
        index = hash_key % self.capacity
        while True:
            if not self.hash_table[index]:
                self.hash_table[index] = [key, hash_key, value]
                self.length += 1
                break
            if self.hash_table[index][0] == key and \
                    self.hash_table[index][1] == hash_key:
                self.hash_table[index][2] = value
                break
            if self.hash_table[index][0] is None:
                self.hash_table[index] = [key, hash_key, value]
                self.length += 1
                break
            index = (index + 1) % self.capacity

    def resize(self):
        old_table_hash = self.hash_table
        self.capacity *= 2
        self.length = 0
        self.hash_table = [[] for _ in range(self.capacity)]
        for element in old_table_hash:
            if len(element) != 0:
                self.__setitem__(element[0], element[2])

    def __getitem__(self, key):
        hash_key = hash(key)
        index = hash(key) % self.capacity
        while self.hash_table[index]:
            if self.hash_table[index][1] == hash_key \
                    and self.hash_table[index][0] == key:
                return self.hash_table[index][2]
            index = (index + 1) % self.capacity
        raise KeyError(f"{key} not in dictionary")

    def get(self, key, value=None):
        try:
            return self.__getitem__(key)
        except KeyError:
            return value

    def clear(self):
        self.__init__()

    def __delitem__(self, key):
        hash_key = hash(key)
        index = hash(key) % self.capacity
        while self.hash_table[index]:
            if self.hash_table[index][1] == hash_key \
                    and self.hash_table[index][0] == key:
                self.hash_table[index][0] = None
                self.length -= 1
                return self
            index = (index + 1) % self.capacity
        raise KeyError(f"{key} not in dictionary")

    def pop(self, key, default=None):
        hash_key = hash(key)
        index = hash(key) % self.capacity
        while self.hash_table[index]:
            if self.hash_table[index][1] == hash_key \
                    and self.hash_table[index][0] == key:
                value = self.hash_table[index][2]
                self.hash_table[index] = []
                self.length -= 1
                return value
            index = (index + 1) % self.capacity
        if default is not None:
            return default
        raise KeyError

    def update(self, other=None, **kwargs):
        if kwargs is not None:
            for k, v in kwargs.items():
                self.__setitem__(k, v)
        if isinstance(other, Dictionary):
            other_table_hash = other.hash_table
            for element in other_table_hash:
                if len(element) != 0:
                    self.__setitem__(element[0], element[2])
            return self
        if isinstance(other, dict):
            for k, v in other.items():
                self.__setitem__(k, v)
            return self
        if isinstance(other, list):
            for element in other:
                if len(element) == 2:
                    self.__setitem__(element[0], element[1])
                else:
                    raise ValueError
            return self
        if other is None:
            return self
        raise TypeError

    def __iter__(self):
        if self.length != 0:
            counter = 0
            while counter <= self.length:
                yield self.hash_table[counter]

    def __repr__(self):
        for element in self.hash_table:
            if len(element) != 0:
                print(element[0], element[2])
