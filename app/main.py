from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Any, Hashable


CAPACITY = 8
LOAD_FACTOR = Fraction(2, 3)
CAPACITY_MULTIPLIER = 2


@dataclass
class Node:
    key: Hashable
    k_hash: int
    value: Any


class Dictionary:
    def __init__(self, capacity: int = CAPACITY) -> None:
        self.capacity = capacity
        self.hashtable: list[Node | None] = [None] * self.capacity
        self.size = 0
        self.keys = []

    def get_index(self, key: Hashable) -> int:
        index = hash(key) % self.capacity

        while (
            self.hashtable[index] is not None
            and self.hashtable[index].key != key
        ):
            index = (index + 1) % self.capacity

        return index

    @property
    def resize_threshold(self) -> Fraction:
        return self.capacity * LOAD_FACTOR

    def __getitem__(self, key: Hashable) -> Any:
        index = self.get_index(key)

        if self.hashtable[index] is None:
            raise KeyError(f"{key}")

        return self.hashtable[index].value

    def resize(self) -> None:
        old_hash_table = self.hashtable
        self.__init__(self.capacity * CAPACITY_MULTIPLIER)

        for node in old_hash_table:
            if node is not None:
                self.__setitem__(node.key, node.value)

    def __setitem__(self, key: Hashable, value: Any) -> None:
        index = self.get_index(key)

        if self.hashtable[index] is None:
            if self.size + 1 >= self.resize_threshold:
                self.resize()
                return self.__setitem__(key, value)
            self.size += 1
            self.keys.append(key)

        self.hashtable[index] = Node(key, hash(key), value)

    def __len__(self) -> int:
        return self.size

    def __delitem__(self, key: Hashable) -> None:
        index = self.get_index(key)

        if self.hashtable[index] is None:
            raise KeyError(f"{key}")

        self.hashtable[index] = None
        self.keys.remove(key)
        self.size -= 1

    def clear(self) -> None:
        for i in range(len(self.hashtable)):
            if self.hashtable[i] is not None:
                self.hashtable[i] = None
        self.keys = []

    def get(self, key: Hashable, default: Any = None) -> Any:
        index = self.get_index(key)

        if self.hashtable[index] is None:
            return default

        return self.hashtable[index]

    def pop(self, key: Hashable, default: Any = None) -> Any:
        index = self.get_index(key)
        node = self.hashtable[index]

        if node is None:
            if default is not None:
                return default
            raise KeyError(f"{key}")

        self.hashtable[index] = None
        self.keys.remove(key)
        self.size -= 1

        return node.value

    def update(self, other: Dictionary) -> None:
        if isinstance(other, Dictionary):
            for node in other:
                if node is not None:
                    self.__setitem__(node.key, node.value)
        else:
            raise TypeError(
                f"{other} is {type(other).__name__}, not a Dictionary"
            )

    def __iter__(self) -> Dictionary:
        self.current_key = 0
        return self

    def __next__(self) -> Node:
        while self.current_key < len(self.keys):
            index = self.get_index(
                self.keys[self.current_key]
            )
            self.current_key += 1
            return self.hashtable[index]
        raise StopIteration()
