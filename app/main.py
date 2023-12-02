from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.load_factor = 0.75
        self.size = 0
        self.table = [None] * self.capacity

    def __setitem__(self, key: Any, value: Any) -> None:
        index = hash(key) % self.capacity
        while self.table[index] is not None and self.table[index][0] != key:
            index = (index + 1) % self.capacity
        if self.table[index] is None:
            self.size += 1
        self.table[index] = (key, value)
        if self.size >= self.capacity * self.load_factor:
            self._resize()

    def _resize(self) -> None:
        self.capacity *= 2
        new_table = [None] * self.capacity
        for item in self.table:
            if item is not None:
                key, value = item
                index = hash(key) % self.capacity
                while new_table[index] is not None:
                    index = (index + 1) % self.capacity
                new_table[index] = (key, value)
        self.table = new_table

    def __getitem__(self, key: Any) -> None:
        index = hash(key) % self.capacity
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.capacity
        raise KeyError(key)

    def __len__(self) -> int:
        return self.size
