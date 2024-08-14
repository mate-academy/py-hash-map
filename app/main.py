from dataclasses import dataclass
from typing import Hashable, Any


INITIAL_CAPACITY = 8
RESIZE_THRESHOLD = 2/3
CAPACITY_MULTIPLIER = 2


@dataclass
class Node:
    key: Hashable
    value: Any


class Dictionary:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.hash_table: list[Node | None] = [None] * self.capacity

    def _calculate_index(self, key):
        index = hash(key) % self.capacity

        while (
            self.hash_table[index] is not None and
            self.hash_table[index].key != key
        ):
            index = (index + 1) % self.capacity

        return index

    @property
    def current_max_size(self):
        return self.capacity * RESIZE_THRESHOLD

    def resize(self):
        old_hash_table = self.hash_table

        self.__init__(self.capacity * CAPACITY_MULTIPLIER)

        for node in old_hash_table:
            if node is not None:
                self.__setitem__(node.key, node.value)

    def __setitem__(self, key, value):
        index = self._calculate_index(key)

        if self.hash_table[index] is None:
            if self.size + 1 >= self.current_max_size:
                self.resize()
                return self.__setitem__(key,value)
            self.size += 1

        self.hash_table[index] = Node(key, value)
