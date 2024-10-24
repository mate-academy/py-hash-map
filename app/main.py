from typing import Any


class Dictionary:

    class Node:
        def __init__(self, key: Any, value: Any) -> None:
            self.key = key
            self.value = value
            self.hash = hash(key)

    def __init__(self) -> None:
        self.capacity = 8
        self.load_factor = 2 / 3
        self.size = 0
        self.table = [[] for _ in range(self.capacity)]

    def __len__(self) -> int:
        return self.size

    def index(self, key: Any) -> int:
        return hash(key) % self.capacity

    def resize(self) -> None:
        new_capacity = self.capacity * 2
        new_table = [[] for _ in range(new_capacity)]

        for bucket in self.table:
            for node in bucket:
                new_idx = hash(node.key) % new_capacity
                new_table[new_idx].append(node)

        self.capacity = new_capacity
        self.table = new_table

    def __setitem__(self, key: Any, value: Any) -> None:
        if self.size >= self.capacity * self.load_factor:
            self.resize()

        index = self.index(key)
        for node in self.table[index]:
            if node.key == key:
                node.value = value
                return

        self.table[index].append(self.Node(key, value))
        self.size += 1

        if self.size / self.capacity > self.load_factor:
            self.resize()

    def __getitem__(self, key: Any) -> Any:
        index = self.index(key)

        for node in self.table[index]:
            if node.key == key:
                return node.value

        raise KeyError(f"Key '{key}' not found.")
