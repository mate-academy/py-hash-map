from typing import Any


class Dictionary:

    class Node:
        def __init__(self, key: Any, value: Any) -> None:
            self.key = key
            self.value = value
            self.hash = hash(key)

    def __init__(self) -> None:
        self.capacity = 8
        self.size = 0
        self.load_factor = 2 / 3
        self.hash_table = [[] for _ in range(self.capacity)]

    def __len__(self) -> int:
        return self.size

    def index(self, key: Any) -> int:
        return hash(key) % self.capacity

    def resize(self) -> None:
        new_capacity = self.capacity * 2
        new_hash_table = [[] for _ in range(new_capacity)]

        for bucket in self.hash_table:
            for node in bucket:
                index = node.hash % new_capacity
                new_hash_table[index].append(node)

        self.hash_table = new_hash_table
        self.capacity = new_capacity

    def __setitem__(self, key: Any, value: Any) -> None:
        if self.size / self.capacity > self.load_factor:
            self.resize()

        index = self.index(key)
        for node in self.hash_table[index]:
            if node.key == key:
                node.value = value
                return

        self.hash_table[index].append(self.Node(key, value))
        self.size += 1

    def __getitem__(self, key: Any) -> Any:
        index = self.index(key)

        for node in self.hash_table[index]:
            if node.key == key:
                return node.value

        raise KeyError(f"Key '{key}' not found.")
