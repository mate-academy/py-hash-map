from dataclasses import dataclass
from typing import Hashable, Any
from fractions import Fraction

CAPACITY = 8
INCREASE_MULTIPLIER = 2
LOAD_FACTOR = Fraction(2, 3)


@dataclass
class Node:
    key: Hashable
    value: Any


class Dictionary:
    def __init__(self, capacity: int = 8) -> None:
        self.capacity = capacity
        self.size = 0
        self.buckets: list[Node] = [None] * self.capacity

    def calculate_index(self, key: Hashable) -> int:
        index = hash(key) % self.capacity
        while (
            self.buckets[index] is not None
            and self.buckets[index].key != key
        ):
            index = (index + 1) % self.capacity
        return index

    def __setitem__(self, key: Hashable, value: Any) -> None:
        index = self.calculate_index(key)
        if self.buckets[index] is None:
            self.size += 1
        self.buckets[index] = Node(key, value)

        if self.size >= self.max_size:
            self.resize()

    def resize(self) -> None:
        old_buckets = self.buckets
        self.capacity *= INCREASE_MULTIPLIER
        self.buckets = [None] * self.capacity
        self.size = 0

        for node in old_buckets:
            if node is not None:
                self[node.key] = node.value

    @property
    def max_size(self) -> int:
        return int(self.capacity * LOAD_FACTOR)

    def __getitem__(self, key: Hashable) -> Any:
        index = self.calculate_index(key)

        if self.buckets[index] is None:
            raise KeyError(f"Can't find element with key {key}")

        return self.buckets[index].value

    def __len__(self) -> int:
        return self.size

    def __delitem__(self, key):
        index = self.calculate_index(key)

        if self.buckets[index] is None:
            raise KeyError(f"Can't find element with key {key}")

        self.buckets[index] = None
        self.size -= 1

