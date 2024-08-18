from __future__ import annotations

from fractions import Fraction
from typing import Any, Iterator

INITIAL_CAPACITY = 8
LOAD_FACTOR = Fraction(2, 3)
CAPACITY_MULTIPLIER = 2


class Dictionary:
    class Node:
        def __init__(self, key: Any, value: Any) -> None:
            self.key = key
            self.value = value

    def __init__(self) -> None:
        self.capacity = INITIAL_CAPACITY
        self.hash_table = [None] * self.capacity
        self.size = 0

    def _calculate_index(self, key: Any) -> int:
        index = hash(key) % self.capacity

        while (
                self.hash_table[index] is not None
                and self.hash_table[index].key != key
        ):
            index = (index + 1) % self.capacity

        return index

    @property
    def threshold(self) -> float:
        return self.capacity * LOAD_FACTOR

    def __setitem__(self, key: Any, value: Any) -> None:
        index = self._calculate_index(key)

        if self.hash_table[index] is None:
            if self.size + 1 >= self.threshold:
                self.resize()
                index = self._calculate_index(key)
            self.size += 1

        self.hash_table[index] = Dictionary.Node(key, value)

    def __getitem__(self, key: Any) -> Any:
        index = self._calculate_index(key)

        if self.hash_table[index] is None:
            raise KeyError(f"Key {key} is not in the dict")

        return self.hash_table[index].value

    def __len__(self) -> int:
        return self.size

    def clear(self) -> None:
        self.__init__()

    def __delitem__(self, key: Any) -> None:
        index = self._calculate_index(key)
        loop_counter = 0

        while self.hash_table[index] is None:
            loop_counter += 1
            index = (index + 1) % self.capacity
            if loop_counter > self.capacity:
                raise KeyError(f"Cannot find value for key: {key}")

        self.hash_table[index] = None
        self.size -= 1

        if (
                self.size < self.threshold // 2
                and self.capacity > INITIAL_CAPACITY
        ):
            self.resize()

    def get(self, key: Any, default: Any = None) -> Any:
        try:
            return self[key]
        except KeyError:
            return default

    def pop(self, key: Any, default: Any = None) -> Any:
        value = self.get(key, default)
        del self[key]
        return value

    def update(self, other: Iterator[Any]) -> None:
        for node in other:
            if node:
                self.__setitem__(node.key, node.value)

    def __iter__(self) -> Iterator[Any]:
        return (node if node else None for node in self.hash_table)

    def resize(self) -> None:
        old_dict = self.hash_table
        if self.size + 1 >= self.threshold:
            self.capacity *= CAPACITY_MULTIPLIER
        elif self.size < self.threshold // 2:
            self.capacity //= CAPACITY_MULTIPLIER

        self.hash_table = [None] * self.capacity
        self.size = 0

        for node in old_dict:
            if node:
                self.__setitem__(node.key, node.value)
