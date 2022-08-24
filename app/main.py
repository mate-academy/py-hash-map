class Dictionary:
    def __init__(self):
        self.capacity = 8
        self.load = 5
        self.hash_table = [None] * 8

    def __setitem__(self, key, value):
        if self.load == len(self):
            backup_hash_table = self.hash_table
            self.capacity *= 2
            self.hash_table = [None] * self.capacity
            self.load = self.capacity * 2 // 3
            for element in \
                    [elem for elem in backup_hash_table if elem is not None]:
                self.__setitem__(element[0], element[2])
            self.__setitem__(key, value)
            return
        hash_key = hash(key)
        index = hash_key % self.capacity
        while self.hash_table[index] is not None:
            if self.hash_table[index][0] == key:
                break
            index = (index + 1) % self.capacity
        self.hash_table[index] = (key, hash_key, value)
        return

    def __getitem__(self, key):
        hash_key = hash(key)
        index = hash_key % self.capacity
        while self.hash_table[index] is not None:
            if self.hash_table[index][0] == key:
                return self.hash_table[index][2]
            index = (index + 1) % self.capacity
        raise KeyError(f"No Key {key} in dict!")

    def __len__(self):
        return len(
            [element for element in self.hash_table if element is not None]
        )
