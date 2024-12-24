from __future__ import annotations
from typing import Hashable, Any, TypeAlias, Iterator
from dataclasses import dataclass

Key: TypeAlias = Hashable
Value: TypeAlias = Any

INITIAL_CAPACITY = 8
RESIZE_THRESHOLD = 2 / 3


@dataclass
class Node:
    key: Key
    value: Value


class Dictionary:
    def __init__(self, capacity: int = INITIAL_CAPACITY) -> None:
        self._capacity = capacity
        self._hash_table: list[Node | None] = [None] * self._capacity
        self._size = 0
        self._keys = []

    def _calculate_index(self, key: Key) -> int:
        index = hash(key) % self._capacity
        while (
                self._hash_table[index] is not None
                and self._hash_table[index].key != key
        ):
            index = (index + 1) % self._capacity
        return index

    @property
    def _current_max_size(self) -> float:
        return self._capacity * RESIZE_THRESHOLD

    def _resize(self) -> None:
        old_hash_table = self._hash_table
        new_capacity = self._capacity * 2
        self.__init__(new_capacity)

        for node in old_hash_table:
            if node is not None:
                self.__setitem__(node.key, node.value)

    def __setitem__(self, key: Key, value: Value) -> None:
        if self._size + 1 >= self._current_max_size:
            self._resize()

        index = self._calculate_index(key)

        if self._hash_table[index] is None:
            self._size += 1

        self._hash_table[index] = Node(key, value)

    def __getitem__(self, key: Key) -> Value:
        index = self._calculate_index(key)
        if self._hash_table[index] is None:
            raise KeyError(f"Cannot find value for key: {key}")
        return self._hash_table[index].value

    def __delitem__(self, key: Key) -> None:
        index = self._calculate_index(key)
        if self._hash_table[index] is None:
            raise KeyError(f"Cannot find value for key: {key}")
        self._hash_table[index] = None
        self._size -= 1

    def __len__(self) -> int:
        return self._size

    def clear(self) -> None:
        self.__init__()

    def get(self, key: Key, default: Value = None) -> Value:
        try:
            return self[key]
        except KeyError:
            return default

    def pop(self, key: Key, default: Value = None) -> Value:
        try:
            index = self._calculate_index(key)
            pop_item = self._hash_table[index].value
            self.__delitem__(key)
            return pop_item
        except KeyError:
            return default

    def __iter__(self) -> Iterator:
        for node in self._hash_table:
            if node is not None:
                yield node.key

    def __str__(self) -> str:
        return f"Dictionary({self._size} items)"
