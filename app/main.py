from typing import Any


class Node:
    def __init__(self, key: int, value: Any) -> None:
        self.key = key
        self.value = value


class Dictionary:
    def __init__(self) -> None:
        self.size = 0
        self.capacity = 8
        self.hash_table: list = [None] * self.capacity
        self.load_factor = 0.7

    def _hash(self, key: int) -> int:
        return hash(key) % self.capacity

    def __len__(self) -> int:
        return self.size

    def __setitem__(self, key: int, value: Any) -> None:
        index = self._hash(key)

        while self.hash_table[index] is not None:
            if self.hash_table[index].key == key:
                self.hash_table[index].value = value
                return
            index = (index + 1) % self.capacity

        self.hash_table[index] = Node(key, value)
        self.size += 1

        if self.size / self.capacity >= self.load_factor:
            self._resize()

    def __getitem__(self, key: int) -> int:
        index = self._hash(key)
        while self.hash_table[index] is not None:
            if self.hash_table[index].key == key:
                return self.hash_table[index].value
            index = (index + 1) % self.capacity
        raise KeyError

    def _resize(self) -> None:
        self.capacity *= 2
        new_table: list = [None] * self.capacity

        for node in self.hash_table:
            if node is not None:
                index = self._hash(node.key)
                while new_table[index] is not None:
                    index = (index + 1) % self.capacity
                new_table[index] = Node(node.key, node.value)

        self.hash_table = new_table

    def __delitem__(self, key: int) -> None:
        index = self._hash(key)
        while self.hash_table[index].key != key:
            if self.hash_table[index].key == key:
                self.hash_table[index] = None
            index = (index + 1) % self.capacity
        self.size -= 1
