from __future__ import annotations

from math import floor
from typing import Any, Hashable


class Dictionary:
    def __init__(self,
                 capacity: int = 8,
                 load_factor: float = 2 / 3
                 ) -> None:
        self.capacity = capacity
        self.load_factor = load_factor
        self.size = 0
        self.hash_table = [None] * self.capacity

    @property
    def current_max_size(self) -> int:
        return floor(self.load_factor * self.capacity)

    def __len__(self) -> int:
        return self.size

    def get_index_for_key(self,
                          key: Hashable
                          ) -> Any:
        index = hash(key) % self.capacity
        while (self.hash_table[index] is not None
               and self.hash_table[index][0] != key):
            index = (index + 1) % self.capacity
        return index

    def resize(self) -> None:
        old_table = self.hash_table
        self.size = 0
        self.capacity *= 2
        self.hash_table = [None] * self.capacity
        for element in old_table:
            if element is not None:
                key, hash_key, value = element
                index = self.get_index_for_key(key)
                self.size += 1
                self.hash_table[index] = (key, hash_key, value)

    def clear(self) -> None:
        self.hash_table = [None] * self.capacity
        self.size = 0

    def get(self,
            key: Hashable,
            value: Any = None
            ) -> Any:
        for index in range(len(self.hash_table)):
            if (self.hash_table[index] is not None
                    and self.hash_table[index][0] == key):
                return self.hash_table[index][2]
        return value

    def pop(self,
            key: Hashable,
            value: Any = None
            ) -> Any:
        for index in range(len(self.hash_table)):
            if (self.hash_table[index] is not None
                    and self.hash_table[index][0] == key):
                return self.hash_table[index][2]
        return value

    def update(self,
               other: Dictionary
               ) -> None:
        for index in range(len(other.hash_table)):
            if other.hash_table[index] is not None:
                key, hash_key, value = other.hash_table[index]
                self.__setitem__(key, value)

    def __delitem__(self,
                    key: Hashable
                    ) -> None:
        for index in range(len(self.hash_table)):
            if (self.hash_table[index] is not None
                    and self.hash_table[index][0] == key):
                self.hash_table[index] = None
                self.length -= 1
                break

    def __setitem__(self,
                    key: Hashable,
                    value: Any
                    ) -> None:
        index = self.get_index_for_key(key)
        if self.hash_table[index] is None:
            if int(self.capacity * self.load_factor) <= self.size:
                self.resize()
                index = self.get_index_for_key(key)
            self.size += 1
        self.hash_table[index] = (key, hash(key), value)

    def __getitem__(self,
                    key: Hashable
                    ) -> Any:
        index = self.get_index_for_key(key)
        if self.hash_table[index] is None:
            raise KeyError
        return self.hash_table[index][2]
