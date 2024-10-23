from typing import Any


class Node:
    def __init__(self, key: Any, value: Any) -> None:
        self.key = key
        self.value = value
        self.hash = hash(key)


class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.load_factor = 2 / 3
        self.size = 0
        self.table = [[] for _ in range(self.capacity)]

    def __len__(self) -> int:
        return self.size

    def _hash(self, key: Any) -> int:
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
        idx = self._hash(key)
        bucket = self.table[idx]

        for node in bucket:
            if node.key == key:
                node.value = value
                return

        new_node = Node(key, value)
        bucket.append(new_node)
        self.size += 1

        if self.size / self.capacity > self.load_factor:
            self.resize()

    def __getitem__(self, key: Any) -> Any:
        idx = self._hash(key)
        bucket = self.table[idx]

        for node in bucket:
            if node.key == key:
                return node.value

        raise KeyError(f"Key {key} not found.")
