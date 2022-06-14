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

        if self.hash_table[index_] is None or \
                self.hash_table[index_][0] == key:
            self.hash_table[index_] = (key, value, hash_key)
            self.size += 1
        else:
            while True:
                if index_ == self.capacity:
                    index_ = 0

                if self.hash_table[index_] is None:
                    self.hash_table[index_] = (key, value, hash_key)
                    self.size += 1
                    break

                if self.hash_table[index_][0] == key:
                    self.hash_table[index_] = (key, value, hash_key)
                    self.size += 1
                    break
                index_ += 1

    def __setitem__(self, key, value):
        if self.size == int(self.capacity * self.load_factor):
            self._size_hash_table()

        self.add_hash_table(key, value)

    def __getitem__(self, key):
        hash_key = hash(key)
        index_ = hash_key % self.capacity

        while self.hash_table[index_] is not None:
            if self.hash_table[index_][0] == key:
                return self.hash_table[index_][1]

            index_ = (index_ + 1) % self.capacity

        raise KeyError

    def correct_dict(self):
        return {
            elem[0]: elem[1] for elem in self.hash_table
            if elem is not None
        }

    def __len__(self):
        return len(self.correct_dict())

    def get(self, key):
        return self.correct_dict()[key]

    def values(self, value):
        for key, values in self.correct_dict().items():
            if values == value:
                return key

    def __repr__(self):
        return self.correct_dict()
