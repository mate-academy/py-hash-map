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
        n = 0
        while True:
            if len(self.hash_table[n]) > 0:
                if self.hash_table[n][0] == item:
                    return self.hash_table[n][1]
            n += 1
            if n >= len(self.hash_table):
                raise KeyError

    def __len__(self):
        return self.items.__len__()

    def hashing(self, hash_, value, key_):
        n = hash_
        while True:
            if len(self.hash_table[n]) == 0:
                self.hash_table[n] = [key_, value, hash_]
                # n += 1
                break
            elif self.hash_table[n][0] == key_:
                for element in self.items:
                    if element[0] == key_:
                        self.items.remove(element)
                        break
                self.hash_table[n] = [key_, value, hash_]
                break
            if n == self.capacity - 1:
                for res_index in range(self.capacity):
                    if not self.hash_table[res_index]:
                        self.hash_table[res_index] = [key_, value, hash_]
                        break
            n += 1
            if n >= len(self.hash_table):
                break
