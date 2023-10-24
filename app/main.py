from typing import Any, Hashable


class Dictionary:

    def __init__(
            self,
            capacity: int = 8,
            load_factor: float = 2 / 3
    ) -> None:
        self.size = 0
        self.capacity = capacity
        self.load_factor = load_factor
        self.hash_table = [None] * self.capacity

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.size > self.capacity * self.load_factor:
            self._resize()
        index = self.__hash(key)
        if not self.hash_table[index]:
            self.size += 1
            self.hash_table[index] = [key, hash(key), value]
        if self.hash_table[index][0] == key:
            self.hash_table[index][2] = value

    def __getitem__(self, key: Hashable) -> Any:
        index = self.__hash(key)
        if not self.hash_table[index]:
            raise KeyError(key)
        return self.hash_table[index][2]

    def __len__(self) -> int:
        return self.size

    def _resize(self) -> None:
        self.capacity *= 2
        old_hash_table = self.hash_table
        self.hash_table = [None] * self.capacity
        self.size = 0
        for node in old_hash_table:
            if node:
                self.__setitem__(node[0], node[2])

    def __hash(self, key: Hashable) -> int:
        index = hash(key) % self.capacity
        while (self.hash_table[index]
               and self.hash_table[index][0] != key):
            index = (index + 1) % self.capacity
        return index
