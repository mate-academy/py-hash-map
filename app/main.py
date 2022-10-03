class Dictionary:
    def __init__(self):
        self.capacity = 8
        self.threshhold = int(self.capacity * 2 / 3)
        self.length = 0
        self.hash_table = [[] for _ in range(self.capacity)]

    def __setitem__(self, key, value):
        key_hash = hash(key)
        index = key_hash % self.capacity
        if self.length == self.threshhold:
            self.resize()
        while True:
            if not self.hash_table[index]:
                self.hash_table[index] = [key, value, key_hash]
                self.length += 1
                break
            if self.hash_table[index][0] == key and \
                    self.hash_table[index][2] == key_hash:
                self.hash_table[index][1] = value
                break
            index = (index + 1) % self.capacity

    def __getitem__(self, key):
        key_hash = hash(key)
        get_index = key_hash % self.capacity
        cell = self.hash_table[get_index]
        while True:
            if not cell:
                raise KeyError
            try:
                if cell[0] == key and cell[2] == key_hash:
                    return cell[1]
            except IndexError:
                raise KeyError
            get_index = (get_index + 1) % self.capacity
            cell = self.hash_table[get_index]

    def __len__(self):
        return self.length

    def resize(self):
        old_table = self.hash_table.copy()
        self.length = 0
        self.capacity *= 2
        self.threshhold = int(self.capacity * 2 / 3)
        self.hash_table = [[] for _ in range(self.capacity)]
        for element in old_table:
            if element:
                self.__setitem__(element[0], element[1])

    def clear(self):
        self.hash_table.clear()

    def get(self, key):
        return self.__getitem__(key)
