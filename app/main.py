class Dictionary:
    def __init__(self):
        self.capacity = 8
        self.length = 0
        self.hash_table = [[] for _ in range(self.capacity)]

    def __len__(self):
        return self.length

    def __setitem__(self, key, value):
        if self.length >= self.capacity * 2 / 3:
            self.resize(2)
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
            index = (index + 1) % self.capacity

    def resize(self, coefficient):
        old_table_hash = self.hash_table
        self.capacity *= coefficient
        if self.capacity < 8:
            self.capacity = 8
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
        raise KeyError(key)

    def clear(self):
        self.__init__()

    def __delitem__(self, key):
        if 6 < self.length <= self.capacity * (1 / 3):
            self.resize(0.5)
        hash_key = hash(key)
        index = hash(key) % self.capacity
        while self.hash_table[index]:
            if self.hash_table[index][1] == hash_key \
                    and self.hash_table[index][0] == key:
                self.hash_table[index] = []
            index = (index + 1) % self.capacity
        raise KeyError(key)

    def get(self, key):
        self.__getitem__(key)

    def pop(self, key):
        self.__delitem__(key)

    def update(self, other):
        if isinstance(other, Dictionary):
            other_table_hash = other.hash_table
            for element in other_table_hash:
                if len(element) != 0:
                    self.__setitem__(element[0], element[2])
        if isinstance(other, dict):
            for k, v in other.items():
                self.__setitem__(k, v)
        raise TypeError(other)

    def __iter__(self):
        if self.length != 0:
            counter = 0
            while counter <= self.length:
                yield self.hash_table[counter]
