from dataclasses import dataclass
from typing import Hashable, Any


@dataclass
class Node:
    key: Hashable
    hash_: int
    value: Any


class Dictionary:
    INITIAL_CAPACITY = 8
    LOAD_FACTOR = 2 / 3

    def __init__(self, capacity: int = INITIAL_CAPACITY):
        self.capacity = capacity
        self.length = 0
        self._hash_table: list[None | Node] = [None] * capacity

    def _get_index(self, key: Hashable) -> int:
        hash_ = hash(key)
        index = hash_ % self.capacity

        while self._hash_table[index] is not None and self._hash_table[index].key != key:
            index = + 1
            index = index % self.capacity

        return index

    def __setitem__(self, key: Hashable, value: Any):
        index = self._get_index(key)
        new_node = Node(key=key, hash_=hash(key), value=value)

        if self.length >= self.capacity * self.LOAD_FACTOR:
            self._resize()

        self._hash_table[index] = new_node
        self.length += 1


    def __getitem__(self, key: Hashable) -> Any:
        index = self._get_index(key)
        node = self._hash_table[index]

        if node is None or node.key != key:
            raise KeyError("No such key")

        return node.value


    def __len__(self) -> int:
        return self.length