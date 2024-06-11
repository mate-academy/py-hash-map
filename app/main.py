from dataclasses import dataclass
from typing import Hashable, Any


@dataclass
class Node:
    key: Hashable
    hash_: int
    value: Any


class Dictionary:
    LOAD_FACTOR = 2 / 3
    DEFAULT_CAPACITY = 8

    def __init__(self) -> None:
        self.capacity = self.DEFAULT_CAPACITY
        self.length = 0
        self.hash_table = [None] * self.capacity

    def _max_load(self) -> float:
        return self.capacity * self.LOAD_FACTOR

    def _get_index(self, key: Hashable) -> int:
        hash_ = hash(key)
        index = hash_ % self.capacity

        while (self.hash_table[index] is not None
               and self.hash_table[index].key != key):
            index += 1
            index = index % self.capacity

        return index

    def _resize(self) -> None:
        self.length = 0
        old_hash_table = self.hash_table
        self.capacity *= 2
        self.hash_table = [None] * self.capacity

        for node in old_hash_table:
            if node is not None:
                self.__setitem__(node.key, node.value)

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.length > self._max_load():
            self._resize()
            index = self._get_index(key)
            if self.hash_table[index] is None:
                self.length += 1
            self.hash_table[index] = Node(key, hash(key), value)
            return

        index = self._get_index(key)
        if self.hash_table[index] is None:
            self.length += 1
        self.hash_table[index] = Node(key, hash(key), value)

    def __getitem__(self, key: Hashable) -> None:
        index = self._get_index(key)
        if self.hash_table[index] is None:
            raise KeyError("Key not found")
        return self.hash_table[index].value

    def __len__(self) -> int:
        return self.length

    def __delitem__(self, key: Hashable) -> None:
        index = self._get_index(key)
        if self.hash_table[index] is None:
            raise KeyError("Key not found")
        self.hash_table[index] = None
