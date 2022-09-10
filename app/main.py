class Dictionary:

    def __init__(self):
        self._capacity = 8
        self._threshold = self._capacity * 2 / 3
        self._size = 0
        self._hash_table = [None for _ in range(self._capacity)]

    def __getitem__(self, item):
        index_ = hash(item) % self._capacity

        while self._hash_table[index_] is not None:
            key, value = self._hash_table[index_]
            if key == item:
                return value
            index_ = (index_ + 1) % self._capacity

        raise KeyError(f"Key {item} not found in dictionary")

    def __setitem__(self, key, value):
        index_ = hash(key) % self._capacity

        while self._hash_table[index_] is not None:
            current_key, _ = self._hash_table[index_]
            if key == current_key:
                self._hash_table[index_] = (current_key, value)
                break
            index_ = (index_ + 1) % self._capacity

        if self._hash_table[index_] is None:
            self._hash_table[index_] = (key, value)
            self._size += 1

        if self._size >= self._threshold:
            self._resize()

    def __delitem__(self, key):
        self.pop(key)

    def __len__(self):
        return self._size

    def __iter__(self):
        self._it = 0
        self._array = [element for element in self._hash_table
                       if element is not None]
        return self

    def __next__(self):
        if self._it >= len(self._array):
            raise StopIteration

        node = self._array[self._it]
        self._it += 1

        return node

    def get(self, key, value=None):
        try:
            return self.__getitem__(key)
        except KeyError:
            return value

    def _resize(self):
        old_data = [elements for elements in self._hash_table if elements]
        self._capacity *= 2
        self._threshold = self._capacity * 2 / 3
        self._size = 0
        self._hash_table = [None] * self._capacity

        for key, value in old_data:
            self.__setitem__(key=key, value=value)

    def pop(self, key_pop):
        index_ = hash(key_pop) % self._capacity

        while self._hash_table[index_] is not None:
            key, value = self._hash_table[index_]
            if key == key_pop:
                self._hash_table[index_] = None
                return value
            index_ = (index_ + 1) % self._capacity

        raise KeyError(f"Key {key_pop} not found in dictionary")

    def update(self, key, value):
        self.__setitem__(key, value)

    def clear(self):
        return self._hash_table.clear()
