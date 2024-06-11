from dataclasses import dataclass
from typing import Hashable, Any
from app.point import Point


@dataclass
class Node:
    key: Hashable
    hash_: int
    value: Any


class Dictionary:
    CAPACITY = 8
    LOAD_FACTOR = 0.75

    def __init__(self, capacity: int = CAPACITY):
        self.length = 0
        self.capacity = capacity
        self.resize = int(self.capacity * self.LOAD_FACTOR)
        self.hash_table = [] * self.capacity

    def _get_index(self, key: Hashable):
        hash_ = hash(key)
        return hash_ % len(self.hash_table)

    def __setitem__(self, key, value):
        index = self._get_index(key)
        self.hash_table[index] = value

    def __getitem__(self, key):
        index = self._get_index(key)
        node = self.hash_table[index]
        return node

    def __len__(self):
        if not self.hash_table:
            return 0
        return self.length

    def clear(self):
        self.hash_table.clear()
        self.length = 0


#   point = Point(3, 3)
#   print(point.x == point.y)

dict