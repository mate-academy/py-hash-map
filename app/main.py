class Dictionary:
    def __init__(self):
        self.items = []
        self.capacity = 8
        self.size = 0
        self.threshold = int(self.capacity * 2 / 3) + 1
        self.hash_table = [[] for _ in range(self.capacity)]

    def __setitem__(self, key, value):
        self.size += 1
        if self.size == self.threshold:
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
            index_item += 1
            if index_item == self.capacity:
                index_item = 0

        if self.hash_table[index_item] == []:
            self.hash_table[index_item] = [key, value]
        elif self.hash_table[index_item][0] == key:
            self.hash_table[index_item][1] = value

    def __getitem__(self, key):
        index_item = hash(key) % self.capacity

        if self.size == 0:
            raise KeyError

        while self.hash_table[index_item][0] != key:
            index_item += 1
            if index_item == self.capacity:
                index_item = 0

        if self.hash_table[index_item][0] == key:
            return self.hash_table[index_item][1]

    def __len__(self):
        return len(self.hash_table) - self.hash_table.count([])
