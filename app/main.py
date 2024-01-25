from __future__ import annotations
from typing import Hashable, Any


class Dictionary:
    def __init__(self) -> None:
        self.load_factor = 2 / 3
        self.capacity = 8
        self.length = 0
        self.hash_table: list = [None] * 8

    def __len__(self) -> int:
        return self.length

    def __resize(self) -> None:
        self.capacity *= 2
        new_hash_table: list = [None] * self.capacity

        for element in self.hash_table:
            if not element:
                continue
            index = element[1] % self.capacity

            while new_hash_table[index]:
                index = (index + 1) % self.capacity
            new_hash_table[index] = element

        self.hash_table = new_hash_table

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.length > self.load_factor * self.capacity:
            self.__resize()
        index = hash(key) % self.capacity

        while True:
            if not self.hash_table[index]:
                self.hash_table[index] = [key, hash(key), value]
                self.length += 1
                break

            if self.hash_table[index][0] == key:
                self.hash_table[index][2] = value
                break
            index = (index + 1) % self.capacity

    def __getitem__(self, key: Hashable) -> Any:
        index = hash(key) % self.capacity
        element = self.hash_table[index]

        step = 0
        while step < self.length:
            if element and element[0] == key:
                return element[2]
            index = (index + 1) % self.capacity
            step += 1
            element = self.hash_table[index]

        raise KeyError(key)

    def __delitem__(self, key: Hashable) -> None:
        index = hash(key) * self.capacity

        while (self.hash_table[index]
               and self.hash_table[index][0] != key):
            index = (index + 1) % self.capacity

        self.hash_table[index] = None
        self.length -= 1

    def clear(self) -> None:
        self.length = 0
        self.capacity = 8
        self.hash_table = [None] * 8

    def get(self, key: Hashable, value: Any = None) -> Any:
        try:
            return self.__getitem__(key)
        except KeyError:
            return value

    def pop(self, key: Hashable) -> Any:
        value = self.__getitem__(key)
        self.__delitem__(key)
        return value

    def items(self) -> list[tuple]:
        return [
            (element[0], element[2])
            for element in self.hash_table
            if element
        ]

    def update(self, other: Dictionary | dict) -> None:
        for key, value in other.items():
            self.__setitem__(key, value)

    def __iter__(self) -> iter:
        for element in self.hash_table:
            if element:
                yield element[0]
