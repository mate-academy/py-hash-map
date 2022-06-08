class Dictionary:
    def __init__(self):
        self._capacity = 8
        self._storage = [None for _ in range(self._capacity)]
        self._flow = 0

    def __setitem__(self, key_, value_):
        key_hash = hash(key_)
        index = key_hash % self._capacity
        while self._storage[index] is not None:
            if self._storage[index][0] == key_hash:
                self._flow -= 1
                break
            else:
                index = (index + 1) % self._capacity
        self._storage[index] = [key_hash, value_, key_]
        self._flow += 1
        if self._flow > self._capacity * 2 / 3:
            self._refactor()

    def __getitem__(self, key_):
        key_hash = hash(key_)
        index = key_hash % self._capacity
        while self._storage[index] is not None:
            if self._storage[index][0] == key_hash:
                return self._storage[index][1]
            index = (index + 1) % self._capacity

    def __len__(self):
        return self._flow

    def _refactor(self):
        self._capacity *= 2
        self.old_storage = self._storage
        self._storage = [None for _ in range(self._capacity)]
        self._flow = 0
        for element in self.old_storage:
            if element is not None:
                self.__setitem__(element[2], element[1])
