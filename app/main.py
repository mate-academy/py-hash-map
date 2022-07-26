class Dictionary:
    def __init__(self):
        self.items = []
        self.capacity = 8
        self.hash_table = [[] for _ in range(self.capacity)]

    def __setitem__(self, key, value):
        self.items.append([key, value])
        threshold = int((self.capacity * 2 / 3))
        size = len(self.items)
        if size == threshold:
            self.capacity *= 2
            self.hash_table = [[] for _ in range(self.capacity)]
            for element in self.items:
                self.hashing(hash(element[0]) % self.capacity,
                             element[1],
                             element[0])
            return

        hash_ = hash(key) % self.capacity
        self.hashing(hash_, value, key)

    def __getitem__(self, item):
        for element in self.hash_table:
            if len(element) > 0 and element[0] == item:
                return element[-1]
            if element == item:
                return item
        raise KeyError

    def __len__(self):
        return len(self.items)

    def hashing(self, hash_, value, key_):
        for index in range(hash_, self.capacity):
            if len(self.hash_table[index]) == 0:
                self.hash_table[index] = [key_, value]
                break
            elif self.hash_table[index][0] == key_:
                for element in self.items:
                    if element[0] == key_:
                        self.items.remove(element)
                        break
                self.hash_table[index] = [key_, value]
                break
            if index == self.capacity - 1:
                for r in range(self.capacity):
                    if not self.hash_table[r]:
                        self.hash_table[r] = [key_, value]
                        break
