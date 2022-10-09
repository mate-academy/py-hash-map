class Dictionary:
    def __init__(self):
        self.capacity = 8
        self.size = 0
        self.threshold = int(self.capacity * 2 / 3)
        self.hash_table = self.make_hash_table()

    def make_hash_table(self):
        return [[] for _ in range(self.capacity)]

    def __len__(self):
        return self.size

    def __getitem__(self, key):
        hash_key = hash(key)
        hash_index = hash_key % self.capacity
        while True:
            try:
                if (
                        self.hash_table[hash_index][0] == key
                        and self.hash_table[hash_index][1] == hash_key
                ):
                    return self.hash_table[hash_index][2]
            except IndexError:
                raise KeyError
            hash_index = (hash_index + 1) % self.capacity

    def resize(self):
        old_hash_table = self.hash_table
        self.size = 0
        self.capacity *= 2
        self.threshold = int(self.capacity * 2 / 3)
        self.hash_table = self.make_hash_table()
        for bucket in old_hash_table:
            if bucket:
                self.__setitem__(bucket[0], bucket[2])

    def __setitem__(self, key, value):
        if self.size == self.threshold:
            self.resize()
        hash_key = hash(key)
        hash_index = hash_key % self.capacity
        while True:
            if not self.hash_table[hash_index]:
                self.hash_table[hash_index] = [key, hash_key, value]
                self.size += 1
                break
            if (
                    self.hash_table[hash_index][0] == key and
                    self.hash_table[hash_index][1] == hash_key
            ):
                self.hash_table[hash_index][2] = value
                break

            hash_index = (hash_index + 1) % self.capacity
