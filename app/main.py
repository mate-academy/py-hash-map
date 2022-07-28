class Dictionary:
    def __init__(self):
        self.items = []
        self.capacity = 8
        self.size = 0
        self.threshold = int(self.capacity * 2 / 3)
        self.hash_table = [[] for _ in range(self.capacity)]

    def __setitem__(self, key, value):
        if self.size == self.threshold:
            self.size = 0
            self.capacity *= 2
            self.threshold = int(self.capacity * 2 / 3) + 1
            self.hash_table = [[] for _ in range(self.capacity)]
            for key_, value_ in self.items:
                self.add_to_hash_table(key_, value_)
        self.items.append([key, value])
        self.add_to_hash_table(key, value)

    def add_to_hash_table(self, key, value):
        index_item = hash(key) % self.capacity

        while self.hash_table[index_item] != [] \
                and self.hash_table[index_item][0] != key:
            index_item = (index_item + 1) % self.capacity

        if self.hash_table[index_item] == []:
            self.size += 1
            self.hash_table[index_item] = [key, value]
        elif self.hash_table[index_item][0] == key:
            self.hash_table[index_item][1] = value

    def __getitem__(self, key):
        index_item = hash(key) % self.capacity

        if self.size == 0:
            raise KeyError

        while self.hash_table[index_item][0] != key:
            index_item = (index_item + 1) % self.capacity

        if self.hash_table[index_item][0] == key \
                and hash(self.hash_table[index_item][0]) == hash(key):
            return self.hash_table[index_item][1]

    def __len__(self):
        return self.size
