class Dictionary:
    def __init__(self):
        self.capacity = 8
        self.storage = [[] for _ in range(self.capacity)]
        self.length = 0
        self.t_hold = int(self.capacity * (2 / 3))

    def resize(self):
        self.capacity *= 2
        self.t_hold = int(self.capacity * (2 / 3))
        temp_store = self.storage
        self.storage = [[] for _ in range(self.capacity)]
        self.length = 0
        for elem in temp_store:
            if elem:
                self.__setitem__(elem[0], elem[2])

    def __setitem__(self, key, value):
        if self.length >= self.t_hold:
            self.resize()
        hash_ = hash(key)
        index_ = hash_ % self.capacity
        while self.storage[index_]:
            if self.storage[index_][0] == key and \
                    self.storage[index_][1] == hash_:
                self.storage[index_] = key, hash_, value
                self.length -= 1
                break
            index_ = (index_ + 1) % self.capacity
        self.storage[index_] = key, hash_, value
        self.length += 1

    def __getitem__(self, key):
        hash_ = hash(key)
        index_ = hash_ % self.capacity
        while self.storage[index_]:
            if self.storage[index_][0] == key and \
                    self.storage[index_][1] == hash_:
                return self.storage[index_][2]
            index_ = (index_ + 1) % self.capacity
        raise KeyError(f'Key {key} dont exist')

    def __len__(self):
        return self.length
