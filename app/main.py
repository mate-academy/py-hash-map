from typing import Any


class Node:
    def __init__(self, key: Any, value: Any, next_node: Any = None) -> None:
        self.key = key
        self.value = value
        self.next = next_node


class Dictionary:
    def __init__(
            self, initial_capacity: int = 8,
            load_factor: float = 2 / 3
    ) -> None:
        self.capacity = initial_capacity
        self.load_factor = load_factor
        self.size = 0
        self.table = [None] * self.capacity

    def __setitem__(self, key: Any, value: Any) -> None:
        index = self._hash_function(key) % self.capacity
        node = self.table[index]

        while node:
            if node.key == key:
                node.value = value
                return
            node = node.next

        new_node = Node(key, value, self.table[index])
        self.table[index] = new_node
        self.size += 1

        if self.size >= self.capacity * self.load_factor:
            self._resize()

    def __getitem__(self, key: Any) -> Any:
        index = self._hash_function(key) % self.capacity
        node = self.table[index]

        while node:
            if node.key == key:
                return node.value
            node = node.next

        raise KeyError(f"Key {key} not found")

    def __delitem__(self, key: Any) -> None:
        index = self._hash_function(key) % self.capacity
        node = self.table[index]
        prev_node = None

        while node:
            if node.key == key:
                if prev_node:
                    prev_node.next = node.next
                else:
                    self.table[index] = node.next
                self.size -= 1
                return
            prev_node = node
            node = node.next

        raise KeyError(f"Key {key} not found")

    def __len__(self) -> int:
        return self.size

    def _hash_function(self, key: Any) -> int:
        return hash(key)

    def _resize(self) -> None:
        new_capacity = self.capacity * 2
        new_table = [None] * new_capacity
        old_table = self.table
        self.table = new_table
        self.capacity = new_capacity
        self.size = 0

        for node in old_table:
            while node:
                self[node.key] = node.value
                node = node.next

    def clear(self) -> None:
        self.table = [None] * self.capacity
        self.size = 0

    def get(self, key: Any, default: Any = None) -> Any:
        try:
            return self[key]
        except KeyError:
            return default

    def pop(self, key: Any, default: Any = None) -> Any:
        try:
            value = self[key]
            del self[key]
            return value
        except KeyError:
            return default
