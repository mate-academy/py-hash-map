class Dictionary:
    def __init__(self):
        self.capacity = 8
        self.load_factor = 2 / 3
        self.size = 0
        self.hash_table = [None for _ in range(self.capacity)]

    def _size_hash_table(self):
        self.capacity *= 2
        self.size = 0
        new_hash_table = [elem for elem in self.hash_table if elem]
        self.hash_table = [None for _ in range(self.capacity)]
        for elem in new_hash_table:
            if elem:
                self.add_hash_table(elem[0], elem[1])

    def add_hash_table(self, key, value):
        hash_key = hash(key)
        index_ = hash_key % self.capacity

        while True:
            if self.hash_table[index_] is None:
                self.hash_table[index_] = (key, value, hash_key)
                self.size += 1
                break

            elif self.hash_table[index_][0] == key and \
                    self.hash_table[index_][2] == hash_key:
                self.hash_table[index_] = (key, value, hash_key)
                break

            index_ = (index_ + 1) % self.capacity

    def __setitem__(self, key, value):
        if self.size == int(self.capacity * self.load_factor):
            self._size_hash_table()

        self.add_hash_table(key, value)

    def __getitem__(self, key):
        hash_key = hash(key)
        index_ = hash_key % self.capacity

        while self.hash_table[index_] is not None:
            if self.hash_table[index_][0] == key and \
                    self.hash_table[index_][2] == hash_key:
                return self.hash_table[index_][1]

            index_ = (index_ + 1) % self.capacity

        raise KeyError

    def __len__(self):
        return self.size

    def get(self, key, default=None):
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    def clear(self):
        for elem in self.hash_table:
            if elem:
                elem = None
        self.size = 0

    def __repr__(self):
        return f"{self.hash_table}"

    def __delitem__(self, key):
        hash_key = hash(key)
        index_ = hash_key % self.capacity

        while self.hash_table[index_] is not None:
            if self.hash_table[index_][0] == key and \
                    self.hash_table[index_][2] == hash_key:
                self.hash_table.pop(index_)
                self.size -= 1
                return self.hash_table[index_][0]

            index_ = (index_ + 1) % self.capacity

        raise KeyError
