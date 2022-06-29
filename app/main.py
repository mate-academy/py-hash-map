class Dictionary:
    def __init__(self):
        self.capacity = 8
        self.threshold = int(self.capacity * (2 / 3))
        self.hash_table = [None for _ in range(self.capacity)]
        self.length = 0

    def __setitem__(self, key, value):
        if self.threshold == self.length:
            tmp = self.resize()
            for node in self.hash_table:
                if node:
                    self.fill_hash_table(node[0], node[2], self.capacity, tmp)
            self.hash_table = tmp
        if self.fill_hash_table(key, value, self.capacity, self.hash_table):
            self.length += 1

    @staticmethod
    def fill_hash_table(key, value, capacity, hash_table):
        len_flag = True
        hash_ = hash(key)
        index_ = hash_ % capacity
        while hash_table[index_]:
            if hash_table[index_][1] == hash_ and hash_table[index_][0] == key:
                len_flag = False
                break
            index_ += 1
            if index_ == capacity:
                index_ = 0
        hash_table[index_] = (key, hash_, value)
        return len_flag

    def resize(self):
        self.capacity *= 2
        self.threshold = int(self.capacity * (2 / 3))
        tmp = [None for _ in range(self.capacity)]
        return tmp

    def __getitem__(self, key):
        hash_ = hash(key)
        index_ = hash_ % self.capacity
        while self.hash_table[index_]:
            if self.hash_table[index_][1] == hash_ \
               and self.hash_table[index_][0] == key:
                return self.hash_table[index_][2]
            index_ += 1
            if index_ == self.capacity:
                index_ = 0
        if not self.hash_table[index_]:
            raise KeyError(key)

    def __len__(self):
        return self.length

    # def clear(self):
    #     pass
    #
    # def __delitem__(self, key):
    #     pass
    #
    # def get(self, key, default=None):
    #     pass
    #
    # def pop(self):
    #     pass
    #
    # def update(self):
    #     pass
    #
    # def __iter__(self):
    #     pass
