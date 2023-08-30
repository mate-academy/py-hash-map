from __future__ import annotations
from typing import Any, Hashable


class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.load_factor = 0.67
        self.length = 0
        self.hash_table = [None] * self.capacity

    def __len__(self) -> int:
        return self.length

    def __setitem__(self, key: Hashable, value: Any) -> None:
        index = self.__index(key)
        if self.hash_table[index] is None:
            self.length += 1
        self.hash_table[index] = (key, value, hash(key))
        if self.length > self.capacity * self.load_factor:
            self.__resize()

    def __resize(self) -> None:
        cells = [cell for cell in self.hash_table if cell]
        self.capacity *= 2
        self.length = 0
        self.hash_table = [None] * self.capacity
        for cell in cells:
            self[cell[0]] = cell[1]

    def __getitem__(self, key: Hashable) -> Any:
        index = self.__index(key)
        if self.hash_table[index]:
            if self.hash_table[index][0] == key:
                return self.hash_table[index][1]
        raise KeyError

    def __index(self, key: Hashable) -> int:
        index = hash(key) % self.capacity
        while self.hash_table[index] and self.hash_table[index][0] != key:
            index = (index + 1) % self.capacity
        return index

    def clear(self) -> None:
        self.hash_table = [None] * self.capacity
        self.length = 0

    def __delitem__(self, key: Hashable) -> None:
        index = self.__index(key)
        if self.hash_table[index]:
            self.hash_table[index] = None
            self.length -= 1

    def get(self, key: Hashable, value: Any = None) -> Any:
        try:
            return self[key]
        except KeyError:
            return value

    def pop(self, key: Hashable, value: Any = None) -> Any:
        try:
            item = self[key]
            del self[key]
            return item
        except KeyError:
            if not value:
                raise
            return value

    def __iter__(self) -> iter:
        for cell in self.hash_table:
            if cell:
                yield cell[0]

    def items(self) -> tuple:
        for cell in self.hash_table:
            if cell:
                yield cell[:2]

    def values(self) -> Any:
        for cell in self.hash_table:
            if cell:
                yield cell[1]

    def __str__(self) -> str:
        return str([cell for cell in self.items()])

    def update(self, dict_: Dictionary) -> None:
        for key, value in dict_.items():
            self[key] = value
