from dataclasses import dataclass
from typing import Hashable, Any


INITIAL_CAPACITY = 8
RESIZE_THRESHOLD = 2 / 3
CAPACITY_MULTIPLIER = 2


@dataclass
class Node:
    key: Hashable
    value: Any


class Dictionary:
    def __init__(self, capacity: int = INITIAL_CAPACITY):
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
                return self.__setitem__(key, value)
            self.size += 1

        self.hash_table[index] = Node(key, value)

    def __getitem__(self, key: Hashable):
        index = self._calculate_index(key)

        if self.hash_table[index] is None:
            raise KeyError(f"Cannot find value for key: {key}")

        return self.hash_table[index].value

    def __delitem__(self, key: Hashable):
        index = self._calculate_index(key)

        if self.hash_table[index] is None:
            raise KeyError(f"Cannot find value for key: {key}")

        self.hash_table[index] = None
        self.size -= 1

    def get(self, key: Hashable, default: Any = None):
        try:
            return self[key]
        except KeyError:
            return default

    def __len__(self):
        return self.size

    def __str__(self):
        return str(self.hash_table)

    def clear(self):
        self.__init__(INITIAL_CAPACITY)

    def pop(self, key: Hashable):
        index = self._calculate_index(key)

        if self.hash_table[index] is None:
            raise KeyError(f"Cannot find value for key: {key}")

        removed = self.hash_table[index].value
        self.hash_table[index] = None
        self.size -= 1
        return removed
