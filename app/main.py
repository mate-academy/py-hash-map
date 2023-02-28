from typing import Hashable


class Node:
    def __init__(self, key: Hashable, value: object) -> None:
        self.key = key
        self.value = value


class Dictionary:
    def __init__(self, initial_capacity: int = 8) -> None:
        self.initial_capacity = initial_capacity
        self.load_factor = int(self.initial_capacity * (2 / 3))
        self.bucket = [None] * self.initial_capacity
        self.size = 0

    def find_index(self, key: Hashable, i: int = 0) -> int:
        index = (hash(key) + i) % self.initial_capacity
        return (
            index
            if self.bucket[index] is None or self.bucket[index].key == key
            else self.find_index(key, i + 1)
        )

    def __setitem__(self, key: Hashable, value: object) -> None:
        index = self.find_index(key)
        if self.bucket[index] is None:
            self.bucket[index] = Node(key, value)
            self.size += 1
        else:
            self.bucket[index].value = value

        if self.size >= self.load_factor:
            self.resize()

    def __getitem__(self, key: Hashable) -> None:
        index = self.find_index(key)
        if self.bucket[index] is None:
            raise KeyError("Current key does not exist")
        return self.bucket[index].value

    def resize(self) -> None:
        self.initial_capacity *= 2
        self.load_factor = int(self.initial_capacity * (2 / 3))
        old_bucket = self.bucket
        self.bucket = [None] * self.initial_capacity
        self.size = 0

        for node in old_bucket:
            if node is not None:
                self[node.key] = node.value

    def __len__(self) -> int:
        return self.size
