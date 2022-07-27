class Dictionary:

    def __init__(self):
        self.capacity = 8
        self.threshold = 5
        self.length = 0
        self.dict = [[] for _ in range(self.capacity)]

    def __setitem__(self, key, value):
        self.key = key
        self.value = value
        hash_ = hash(self.key)
        index_ = hash_ % self.capacity
        while self.dict[index_]:
            if self.dict[index_][0] == key:
                self.dict[index_] = [self.key, self.value, hash_]
                self.length -= 1
                break
            index_ = (index_ + 1) % self.capacity
        self.dict[index_] = [self.key, self.value, hash_]
        self.length += 1
        if self.length == self.threshold:
            self.resize()

    def __getitem__(self, key):
        index_ = hash(key) % self.capacity
        while self.dict[index_]:
            if self.dict[index_][0] == key:
                return self.dict[index_][1]
            index_ = (index_ + 1) % self.capacity
        raise KeyError

    def resize(self):
        self.capacity *= 2
        self.threshold = int(self.capacity * (2 / 3))
        all_items = [item for item in self.dict if item]
        self.dict = [[] for _ in range(self.capacity)]
        self.length = 0
        for item in all_items:
            self.__setitem__(item[0], item[1])

    def __len__(self):
        return self.length
