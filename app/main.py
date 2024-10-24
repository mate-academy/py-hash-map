from typing import Any


class Node:
    def __init__(self, key: Any, value: Any, hash_value: int) -> None:
        self.key = key
        self.value = value
        self.hash = hash_value
        self.next = None


class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.size = 0
        self.load_factor = 0.7
        self.table = [None] * self.capacity

    def __setitem__(self, key: Any, value: Any) -> None:
        current_index = self._hash_index(key)
        current = self.table[current_index]
        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next

        new_node = Node(key, value, hash(key))
        new_node.next = self.table[current_index]
        self.table[current_index] = new_node
        self.size += 1

        if self.size / self.capacity > self.load_factor:
            self._resize()

    def __getitem__(self, key: Any) -> None:
        current_index = self._hash_index(key)
        current = self.table[current_index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError(f"Key '{key}' is not found")

    def __len__(self) -> int:
        return self.size

    def _hash_index(self, key: Any) -> int:
        return hash(key) % self.capacity

    def _resize(self) -> None:
        new_capacity = self.capacity * 2
        new_table = [None] * new_capacity

        for node in self.table:
            while node is not None:
                current_index = hash(node.key) % new_capacity
                new_node = Node(node.key, node.value, node.hash)
                new_node.next = new_table[current_index]
                new_table[current_index] = new_node
                node = node.next

        self.table = new_table
        self.capacity = new_capacity
