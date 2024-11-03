from dataclasses import dataclass
from typing import Hashable, Any


@dataclass
class Node:
    key: Hashable
    value: any
    key_hash: int


class Dictionary:
    INITIAL_CAPACITY = 8
    THRESHOLD = 2 / 3
    CAPACITY_MULTIPLIER = 2

    def __init__(self, capacity: int = INITIAL_CAPACITY) -> None:
        self.capacity = capacity
        self.size = 0
        self.hash_table = [None] * self.capacity

    def index_change(self, index: int) -> int:
        return (index + 1) % self.capacity

    def calculate_index(self, key: Hashable) -> int:
        key_hash = hash(key)
        index = key_hash % self.capacity
        while (node := self.hash_table[index]) is not None:
            if node.key == key and node.key_hash == key_hash:
                break
            index = self.index_change(index)
        return index

    def resize(self) -> None:
        self.capacity *= self.CAPACITY_MULTIPLIER
        old_hash_table = self.hash_table
        self.hash_table = [None] * self.capacity
        self.size = 0
        for node in old_hash_table:
            if node is not None:
                self[node.key] = node.value

    def __setitem__(self, key: Hashable, value: Any) -> None:
        index = self.calculate_index(key)
        node = self.hash_table[index]
        if node is not None:
            node.value = value
            return
        if self.size + 1 >= self.capacity * self.THRESHOLD:
            self.resize()
            self[key] = value
        else:
            self.hash_table[index] = Node(key, value, hash(key))
            self.size += 1
    def __getitem__(self, key: Hashable) -> Any:
        index = self.calculate_index(key)
        if (node := self.hash_table[index]) is None:
            raise KeyError
        return node.value

    def __len__(self) -> int:
        return self.size
