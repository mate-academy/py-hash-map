from __future__ import annotations
from typing import Hashable, Any


class Node:
    def __init__(
            self,
            key: Hashable,
            value: Any,
            hash_val: int = None
    ) -> None:
        self.key = key
        self.value = value
        self.hash = hash(key) if hash_val is None else hash_val


class Dictionary:
    def __init__(self, capacity: int = 8, load_factor: int = 2 / 3) -> None:
        self.capacity = capacity
        self.load_factor = load_factor
        self.size = 0
        self.table = [[] for _ in range(self.capacity)]

    def __setitem__(self, key: Hashable, value: Any) -> None:
        hash_val = hash(key)
        store = self.table[hash_val % self.capacity]
        for node in store:
            if node.key == key:
                node.value = value
                return
        store.append(Node(key, value, hash_val))
        self.size += 1
        if self.size >= self.capacity * self.load_factor:
            self.resize()

    def resize(self) -> None:
        self.capacity *= 2
        new_table = [[] for _ in range(self.capacity)]

        for store in self.table:

            for node in store:
                new_table[node.hash % self.capacity].append(node)
        self.table = new_table

    def __getitem__(self, key: Hashable) -> Any:
        hash_val = hash(key)
        store = self.table[hash_val % self.capacity]
        for node in store:
            if node.key == key:
                return node.value
        raise KeyError(key)

    def __len__(self) -> int:
        return self.size

    def __delitem__(self, key: Hashable) -> None:
        hash_val = hash(key)
        store = self.table[hash_val % self.capacity]
        for i, node in enumerate(store):
            if node.key == key:
                del store[i]
                self.size -= 1
                return
        raise KeyError(key)

    def clear(self) -> None:
        self.size = 0
        self.table = [[] for _ in range(self.capacity)]

    def get(self, key: Hashable, default: Any = None) -> Any:
        try:
            return self[key]
        except KeyError:
            return default

    def pop(self, key: Hashable, default: Any = None) -> Any:
        try:
            value = self[key]
            del self[key]
            return value
        except KeyError:
            return default

    def update(self, other: dict or Dictionary) -> None:
        for key, value in other.items():
            self[key] = value

    def __iter__(self) -> None:
        for store in self.table:
            for node in store:
                yield node.key
