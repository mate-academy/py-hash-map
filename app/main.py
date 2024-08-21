from collections.abc import Hashable
from typing import Any


class Node:
    def __init__(self, key: Hashable, value: Any) -> None:
        self.key = key
        self.value = value
        self.hash = hash(key)
        self.next = None


class Dictionary:
    INITIAL_CAPACITY = 8
    LOAD_FACTOR = 2 / 3

    def __init__(self) -> None:
        self.load_factor = self.LOAD_FACTOR
        self.capacity = self.INITIAL_CAPACITY
        self.size = 0
        self.table = [None] * self.capacity

    def _hash(self, key: Hashable) -> int:
        return hash(key) % self.capacity

    def _resize(self) -> None:
        old_table = self.table
        self.capacity *= 2
        self.table = [None] * self.capacity
        self.size = 0

        for node in old_table:
            while node:
                self.__setitem__(node.key, node.value)
                node = node.next

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.size >= self.capacity * self.load_factor:
            self._resize()

        index = self._hash(key)
        node = self.table[index]

        if node is None:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            while node:
                if node.key == key:
                    node.value = value
                    return
                if node.next is None:
                    break
                node = node.next
            node.next = Node(key, value)
            self.size += 1

    def __getitem__(self, key: Hashable) -> None:
        index = self._hash(key)
        node = self.table[index]

        while node:
            if node.key == key:
                return node.value
            node = node.next

        raise KeyError(f"Key '{key}' not found")

    def __len__(self) -> int:
        return self.size
