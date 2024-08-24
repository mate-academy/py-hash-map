from dataclasses import dataclass
from typing import Hashable, Any
from fractions import Fraction


class Dictionary:
    CAPACITY = 8
    INCREASE_MULTIPLIER = 2
    LOAD_FACTOR = Fraction(2, 3)

    @dataclass
    class Node:
        key: Hashable
        value: Any
        hash = hash(key)

    def __init__(self) -> None:
        self.capacity = self.CAPACITY
        self.size = 0
        self.buckets = [None] * self.capacity

    def calculate_index(self, key: Hashable) -> int:
        index = hash(key) % self.capacity
        while (
            self.buckets[index] is not None
            and self.buckets[index].key != key
        ):
            index = (index + 1) % self.capacity
        return index

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.size >= self.max_size:
            self.resize()

        index = self.calculate_index(key)
        if self.buckets[index] is None:
            self.size += 1
        self.buckets[index] = self.Node(key, value)

    def resize(self) -> None:
        old_buckets = self.buckets
        self.capacity *= self.INCREASE_MULTIPLIER
        self.buckets = [None] * self.capacity
        self.size = 0

        for node in old_buckets:
            if node is not None:
                self[node.key] = node.value

    @property
    def max_size(self) -> int:
        return int(self.capacity * self.LOAD_FACTOR)

    def __getitem__(self, key: Hashable) -> Any:
        index = self.calculate_index(key)

        if self.buckets[index] is None:
            raise KeyError(f"Can't find element with key {key}")

        return self.buckets[index].value

    def __len__(self) -> int:
        return self.size

    def __delitem__(self, key: Hashable) -> None:
        index = self.calculate_index(key)

        if self.buckets[index] is None:
            raise KeyError(f"Can't find element with key {key}")

        self.buckets[index] = None
        self.size -= 1
