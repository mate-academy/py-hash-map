class Dictionary:
    def __init__(self):
        self.capacity = 8
        self.size = 0
        self.threshold = int(self.capacity * 2 / 3)
        self.hash_table = [[] for _ in range(self.capacity)]

    def __setitem__(self, key, value):
        if self.size == self.threshold:
            self.change_size()
        self.add_to_hash_table(key, value)

    def change_size(self):
        self.size = 0
        self.capacity *= 2
        self.threshold = int(self.capacity * 2 / 3) + 1
        old_hash_table = self.hash_table
        self.hash_table = [[] for _ in range(self.capacity)]
        for item in old_hash_table:
            if item != []:
                self.__setitem__(item[0], item[1])

    def add_to_hash_table(self, key, value):
        index_item = hash(key) % self.capacity

        while self.hash_table[index_item] != [] \
                and self.hash_table[index_item][0] != key:
            index_item = (index_item + 1) % self.capacity

        if self.hash_table[index_item] == []:
            self.size += 1
            self.hash_table[index_item] = [key, value]
        elif self.hash_table[index_item][0] == key \
                and hash(self.hash_table[index_item][0]) == hash(key):
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
