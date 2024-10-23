from typing import Hashable, Any


class Node:
    def __init__(self, key: Hashable, value: Any) -> None:
        self.key = key
        self.value = value
        self.hash = hash(key)


class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.load_factor = 2 / 3
        self.length = 0
        self.hash_table: list[None | list[Node]] = [None] * self.capacity

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.length / self.capacity >= self.load_factor:
            self.resize()

        idx = hash(key) % self.capacity

        if self.hash_table[idx] is None:
            self.hash_table[idx] = []

        for node in self.hash_table[idx]:
            if node.key == key:
                node.value = value
                return

        self.hash_table[idx].append(Node(key, value))
        self.length += 1

    def __getitem__(self, key: Hashable) -> Any:
        idx = hash(key) % self.capacity

        if self.hash_table[idx]:
            for node in self.hash_table[idx]:
                if node.key == key:
                    return node.value
        raise KeyError(key)

    def __len__(self) -> int:
        return self.length

    def resize(self) -> None:
        self.capacity *= 2
        old_hash_table = self.hash_table

        self.hash_table = [None] * self.capacity
        self.length = 0

        for item in old_hash_table:
            if item:
                for node in item:
                    self.__setitem__(node.key, node.value)
