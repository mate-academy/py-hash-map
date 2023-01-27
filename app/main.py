class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.threshold = int(self.capacity * 2 / 3)
        self.resize_multiplier = 2
        self.size = 0
        self.hash_table = [[] for _ in range(self.capacity)]

    def __len__(self) -> int:
        return self.size

    def _get_index_and_hash(self, key):
        index = hash(key) % self.capacity
        hash_of_item = hash(key)
        return hash_of_item, index

    def __setitem__(self, key, value):
        if self.size > self.threshold:
            self._resize()
        hash_of_item, index = self._get_index_and_hash(key)
        node = [key, hash_of_item, value]
        while True:
            if not self.hash_table[index]:
                self.hash_table[index] = node
                self.size += 1
                break
            if self.hash_table[index][0] == key and \
                    self.hash_table[index][1] == hash_of_item:
                self.hash_table[index][2] = value
                break
            index = (index + 1) % self.capacity

    def _resize(self):
        self.capacity *= self.resize_multiplier
        self.threshold = int(self.capacity * 2 / 3)
        old_hash_list = self.hash_table
        self.size = 0
        self.hash_table = [[] for _ in range(self.capacity)]
        for item in old_hash_list:
            if item:
                self.__setitem__(item[0], item[2])

    def __getitem__(self, key):
        hash_of_item, index = self._get_index_and_hash(key)
        while self.hash_table[index]:
            if self.hash_table[index][0] == key and \
                    self.hash_table[index][1] == hash_of_item:
                return self.hash_table[index][2]
            index = (index + 1) % self.capacity
        raise KeyError
