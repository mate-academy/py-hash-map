from typing import Any
from typing import Hashable


class Node:
    def __init__(self, key: Hashable, hash_value: int, value: Any) -> None:
        self.key = key
        self.hash_value = hash_value
        self.value = value
        self.next = None


class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.load_factor = 2 / 3
        self.size = 0
        self.table = [None] * self.capacity

    def __setitem__(self, key: Hashable, value: Any) -> None:
        hash_value = hash(key)
        index = hash_value % self.capacity

        if self.table[index] is None:
            self.table[index] = Node(key, hash_value, value)
            self.size += 1
        else:
            current = self.table[index]
            while current.next:
                if current.key == key:
                    current.value = value
                    return
                current = current.next

            if current.key == key:
                current.value = value
            else:
                current.next = Node(key, hash_value, value)
                self.size += 1

        if self.size / self.capacity > self.load_factor:
            self._resize()

    def __getitem__(self, key: Hashable) -> Any:
        hash_value = hash(key)
        index = hash_value % self.capacity

        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next

        raise KeyError(f"Key '{key}' not found in the dictionary")

    def __len__(self) -> int:
        return self.size

    def _resize(self) -> None:
        new_capacity = self.capacity * 2
        new_table = [None] * new_capacity

        for node in self.table:
            while node:
                new_index = node.hash_value % new_capacity
                if new_table[new_index] is None:
                    new_table[new_index] = Node(node.key, node.hash_value,
                                                node.value)
                else:
                    current = new_table[new_index]
                    while current.next:
                        current = current.next
                    current.next = Node(node.key, node.hash_value, node.value)

                node = node.next

        self.table = new_table
        self.capacity = new_capacity
