class Dictionary:
    def __init__(self):
        self.capacity = 8
        self.load = 5
        self.hash_table = [None] * 8
        self.length = 0

    def __setitem__(self, key, value):
        if self.load == len(self):
            self.update_hash_table(self.capacity * 2)
            self.__setitem__(key, value)
            return
        hash_key = hash(key)
        index = hash_key % self.capacity
        update_key = False
        while self.hash_table[index] is not None:
            if self.hash_table[index][1] == hash_key and \
                    self.hash_table[index][0] == key:
                update_key = True
                break
            index = (index + 1) % self.capacity
        self.hash_table[index] = (key, hash_key, value)
        self.length += 1 if not update_key else 0

    def update_hash_table(self, capacity):
        backup_hash_table = self.hash_table
        self.length = 0
        self.capacity = capacity
        self.hash_table = [None] * self.capacity
        self.load = self.capacity * 2 // 3
        for element in \
                [elem for elem in backup_hash_table if elem is not None]:
            self.__setitem__(element[0], element[2])

    def __getitem__(self, key):
        return self.hash_table[self.find_item(key)][2]

    def __len__(self):
        return self.length

    def clear(self):
        self.hash_table = [None] * 8
        self.capacity = 8
        self.load = 5
        self.length = 0

    def __delitem__(self, key):
        self.hash_table[self.find_item(key)] = None
        self.update_hash_table(self.capacity)

    def get(self, key, value=None):
        try:
            result = self.__getitem__(key)
        except KeyError:
            result = value
        return result

    def pop(self, key, value=None):
        try:
            i = self.find_item(key)
        except KeyError:
            if value is not None:
                return value
            raise
        result = self.hash_table[i][2]
        self.__delitem__(self.hash_table[i][0])
        return result

    def update(self, *args, **kwargs):
        for arg in args:
            if isinstance(arg, dict):
                for key, value in arg.items():
                    self.__setitem__(key, value)
            else:
                key, value = arg
                self.__setitem__(key, value)
        for key, value in kwargs.items():
            self.__setitem__(key, value)

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
