class Dictionary:
    def __init__(self):
        self.length = 0
        self.capacity = 8
        self.hash_table = [[] for _ in range(self.capacity)]

    def __len__(self):
        return self.length

    def __setitem__(self, key, value):
        if len(self) + 1 > self.capacity * 2 / 3:
            self._resize()
        index = hash(key) % self.capacity
        while True:
            if len(self.hash_table[index]) > 0:
                if hash(key) == self.hash_table[index][0] \
                        and key == self.hash_table[index][1]:
                    self.hash_table[index] = [hash(key), key, value]
                    break
                index = (index + 1) % self.capacity
            else:
                self.hash_table[index] = [hash(key), key, value]
                self.length += 1
                break

    def __getitem__(self, key):
        index = hash(key) % self.capacity
        i = 0
        while i <= self.capacity:
            if len(self.hash_table[index]) > 0:
                if self.hash_table[index][0] == hash(key) \
                        and self.hash_table[index][1] == key:
                    return self.hash_table[index][2]
                index = (index + 1) % self.capacity
            i += 1
        raise KeyError

    def _resize(self):
        previous_list = []
        for item in self.hash_table:
            if len(item) > 0:
                previous_list.append(item)
        self.capacity *= 2
        self.hash_table = [[] for _ in range(self.capacity)]
        for item in previous_list:
            index = hash(item[1]) % self.capacity
            while True:
                if len(self.hash_table[index]) > 0:
                    index = (index + 1) % self.capacity
                else:
                    self.hash_table[index] = [hash(item[1]), item[1], item[2]]
                    break
