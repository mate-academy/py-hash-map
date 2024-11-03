from dataclasses import dataclass
from typing import Hashable, Any


@dataclass
class Node:
    key: Hashable
    value: any
    hash_value: int


class Dictionary:
    INITIAL_CAPACITY = 8
    THRESHOLD = 2 / 3
    CAPACITY_MULTIPLIER = 2

    def __init__(self, capacity: int = INITIAL_CAPACITY) -> None:
        self.capacity = capacity
        self.size = 0
        self.hash_table = [None] * self.capacity
        self.container = [[] for _ in range(self.capacity)]

    def value_table_index(self, key: Hashable) -> int:
        return hash(key) % self.capacity

    def resize(self) -> None:
        new_capacity = self.capacity * self.CAPACITY_MULTIPLIER
        new_container = [[] for _ in range(new_capacity)]

        for bucket in self.container:
            for node in bucket:
                new_index = node.hash_value % new_capacity
                new_container[new_index].append(node)

        self.capacity = new_capacity
        self.container = new_container

    def __setitem__(self, key: Hashable, value: Any) -> None:
        node = Node(key, value, hash(key))
        index = self.value_table_index(key)
        if self.hash_table[index] is None:
            self.size += 1
        self.hash_table[index] = node
        if self.THRESHOLD * self.capacity <= self.size:
            self.resize()

    def __getitem__(self, key: Hashable) -> Any:
        index = self.value_table_index(key)
        if self.hash_table[index] is not None:
            return self.hash_table[index].value
        raise KeyError

    def __len__(self) -> int:
        return self.size
