class Dictionary:
    def __init__(self):
        self.hash_table = [[] for _ in range(8)]
        self.capacity = 8
        self.length = 0

    def __setitem__(self, key, value):
        self._resize()
        self.length += 1
        hash_ = hash(key)
        index = hash_ % self.capacity
        while self.hash_table[index]:
            if self.hash_table[index][0] == hash_ and \
                    self.hash_table[index][1] == key:
                self.hash_table[index] = [hash_, key, value]
                self.length -= 1
                break

            index = (index + 1) % self.capacity

        self.hash_table[index] = [hash_, key, value]

    def __getitem__(self, key):
        hash_ = hash(key)
        index = hash_ % self.capacity
        while self.hash_table[index]:
            if self.hash_table[index][1] == key and\
                    self.hash_table[index][0] == hash_:
                return self.hash_table[index][2]
            index = (index + 1) % self.capacity
        raise KeyError

    def __len__(self):
        return self.length

    def _resize(self):
        size_to_resize = round((self.capacity / 3) * 2)
        if len(self) >= size_to_resize:
            self.length = 0
            temp_list = self.hash_table.copy()
            self.capacity *= 2
            self.hash_table = [[] for _ in range(self.capacity)]

            for el in temp_list:
                if el:
                    self[el[1]] = el[2]
