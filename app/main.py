from dataclasses import dataclass
from typing import Hashable, Any


INITIAL_CAPACITY = 8
RESIZE_THRESHOLD = 0.62
CAPACITY_MULTIPLIER = 2


@dataclass
class Node:
    key: Hashable
    value: Any


class Dictionary:
    def __init__(
            self,
            capacity:
            int = INITIAL_CAPACITY
    ) -> None:
        self.capacity = capacity
        self.size = 0
        self.hash_table: list[Node | None] = [None] * self.capacity

    def _calculate_index(
            self,
            key: Hashable
    ) -> int:
        index = hash(key) % self.capacity
        while (
            self.hash_table[index] is not None
            and self.hash_table[index].key != key
        ):
            index = (index + 1) % self.capacity
        return index

    def _resize(self) -> None:
        old_hash_table = self.hash_table
        self.capacity *= CAPACITY_MULTIPLIER
        self.hash_table = [None] * self.capacity
        self.size = 0

        for node in old_hash_table:
            if node is not None:
                self.__setitem__(node.key, node.value)

    def __setitem__(
            self,
            key: Hashable,
            value: Any
    ) -> None:
        if self.size >= self.capacity * RESIZE_THRESHOLD:
            self._resize()

        index = self._calculate_index(key)
        if self.hash_table[index] is None:
            self.size += 1
        self.hash_table[index] = Node(key, value)

    def __getitem__(
            self,
            key: Hashable
    ) -> Any:
        index = self._calculate_index(key)
        if self.hash_table[index] is None:
            raise KeyError(f"Key {key} not found.")
        return self.hash_table[index].value

    def __delitem__(
            self,
            key: Hashable
    ) -> None:
        index = self._calculate_index(key)
        if self.hash_table[index] is None:
            raise KeyError(f"Key {key} not found.")
        self.hash_table[index] = None
        self.size -= 1

    def get(
            self,
            key: Hashable,
            default: Any = None
    ) -> Any:
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        return str([node for node in self.hash_table if node is not None])

    def clear(self) -> None:
        self.hash_table = [None] * self.capacity
        self.size = 0
