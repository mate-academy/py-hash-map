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
        return self.hash_table[self.find_item(key)][2]

    def __len__(self):
        return len(
            [element for element in self.hash_table if element is not None]
        )

    def clear(self):
        for i in range(len(self.hash_table)):
            self.hash_table[i] = None

    def __delitem__(self, key):
        self.hash_table[self.find_item(key)] = None

    def get(self, key):
        return self.__getitem__(key)

    def pop(self, key):
        i = self.find_item(key)
        result = self.hash_table[i][2]
        self.__delitem__(self.hash_table[i][0])
        return result

    def update(self, items: list):
        self.__setitem__(items[0], items[1])

    def __iter__(self):
        self.iter_i = 0
        return self

    def __next__(self):
        if self.iter_i < self.__len__():
            table = [elem for elem in self.hash_table if elem is not None]
            result = table[self.iter_i][2]
            self.iter_i += 1
            return result
        raise StopIteration

    def find_item(self, key):
        hash_key = hash(key)
        index = hash_key % self.capacity
        while self.hash_table[index] is not None:
            if self.hash_table[index][0] == key:
                return index
            index = (index + 1) % self.capacity
        raise KeyError(f"No Key {key} in dict!")


dict_ = Dictionary()
dict_[1] = 2
dict_[2] = 3
print(len(dict_))
dict_.clear()
print(len(dict_))
