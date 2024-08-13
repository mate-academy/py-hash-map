from collections.abc import Hashable
from typing import Any


class Dictionary:
    def __init__(
            self,
            initial_capacity: int = 8,
            load_factor: float = 0.75
    ) -> None:
        self.load_factor = load_factor
        self.capacity = initial_capacity
        self.size = 0
        self.table = [[] for _ in range(self.capacity)]

    def _hash(self, key: Hashable) -> int:
        return hash(key) % self.capacity

    def _resize(self) -> None:
        old_table = self.table
        self.capacity *= 2
        self.table = [[] for _ in range(self.capacity)]
        self.size = 0

        for entry in old_table:
            if entry:
                for k, v, h in entry:
                    self.__setitem__(k, v)

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.size >= self.capacity * self.load_factor:
            self._resize()

        index = self._hash(key)

        for i, (k, v, h) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value, h)
                return

        self.table[index].append((key, value, hash(key)))
        self.size += 1

    def __getitem__(self, key: Hashable) -> Any:
        index = self._hash(key)
        if self.table[index] is None:
            raise KeyError(f"Key '{key}' not found")

        for k, v, h in self.table[index]:
            if k == key:
                return v

        raise KeyError(f"Key '{key}' not found")

    def __len__(self) -> int:
        return self.size
