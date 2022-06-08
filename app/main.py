class Dictionary:

    def __init__(self):
        self.__capacity = 8
        self.__threshold = 2 / 3
        self.__resize_step = 2
        self.__cells = 0
        self.__hash_table = [None for _ in range(self.__capacity)]

    def __setitem__(self, key, value):
        if self.__cells > self.__capacity * self.__threshold:
            self.__hash_table_resize()
        cell_hash = hash(key)
        index = cell_hash % self.__capacity

        while self.__hash_table[index] is not None:
            if self.__hash_table[index][2] == cell_hash:
                if self.__hash_table[index][0] == key:
                    break
            index += 1
            if index >= self.__capacity - 1:
                index = 0
        else:
            self.__cells += 1

        self.__hash_table[index] = (key, value, cell_hash)

    def __getitem__(self, key_):
        cell_hash = hash(key_)
        index = cell_hash % self.__capacity
        while self.__hash_table[index] is not None:
            key, value, c_hash = self.__hash_table[index]
            if c_hash == cell_hash:
                if key == key_:
                    return value
            index += 1
            if index >= self.__capacity - 1:
                index = 0
        raise KeyError(f"Key: {key_} not found.")

    def __len__(self):
        return self.__cells

    def clear(self):
        self.__cells = 0
        self.__hash_table = [None for _ in range(self.__capacity)]

    def __delitem__(self, key):
        if self[key]:
            index = hash(key) % self.__capacity
            self.__hash_table[index] = None
            self.__cells -= 1
        else:
            raise KeyError(f"Key: {key} not found.")

    def get(self, key, default=None):
        if self[key] is not None:
            return self[key]
        return default

    def pop(self, key, default=None):
        if self[key] is not None:
            self.__delitem__(key)
        else:
            if default is not None:
                return default
            else:
                raise KeyError(f"Key: {key} not found.")
        return self.__getitem__(key)

    def __hash_table_resize(self):
        hash_table = self.__hash_table
        self.__capacity *= self.__resize_step
        self.__hash_table = [None for _ in range(self.__capacity)]
        self.__cells = 0
        for cell in hash_table:
            if cell is not None:
                self.__setitem__(cell[0], cell[1])
