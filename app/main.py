from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Hashable


class Dictionary:
    _DEFAULT_INITIAL_CAPACITY = 8
    _DEFAULT_LOAD_FACTOR = 2 / 3
    _DEFAULT_CAPACITY_MULTIPLIER = 2

    @dataclass
    class Node:
        key: Hashable
        value: Any

    def __init__(
            self,
            initial_capacity: int = _DEFAULT_INITIAL_CAPACITY,
            load_factor: float = _DEFAULT_LOAD_FACTOR,
            capacity_multiplier: int | float = _DEFAULT_CAPACITY_MULTIPLIER
    ) -> None:
        self._capacity = initial_capacity
        self._load_factor = load_factor
        self._threshold = int(initial_capacity * load_factor)
        self._capacity_multiplier = capacity_multiplier
        self._size = 0
        self._hash_table: list[Dictionary.Node | None] = (
                [None] * self._capacity
        )

    def _calculate_index(self, key: Hashable) -> int:
        index = hash(key) % self._capacity

        while (
                self._hash_table[index] is not None
                and self._hash_table[index].key != key
        ):
            index = (index + 1) % self._capacity

        return index

    def __getitem__(self, key: Hashable) -> Any:
        item: Dictionary.Node | None = (
            self._hash_table[self._calculate_index(key)]
        )

        if not item:
            raise KeyError(f"'{key}'")

        return item.value

    def __setitem__(self, key: Hashable, value: Any) -> None:
        index = self._calculate_index(key)

        if not self._hash_table[index]:
            if self._size + 1 >= self._threshold:
                self._resize_hash_table()
                return self.__setitem__(key, value)
            self._hash_table[index] = Dictionary.Node(key, value)
            self._size += 1
        else:
            self._hash_table[index].value = value

    def __delitem__(self, key: Hashable) -> None:
        index = self._calculate_index(key)

        if not self._hash_table[index]:
            raise KeyError(f"'{key}'")

        self._hash_table[index] = None
        self._size -= 1

    def __iter__(self) -> Dictionary:
        self._current_iteration = 0
        return self

    def __next__(self) -> (Hashable, Any):
        while self._current_iteration < self._capacity:
            item = self._hash_table[self._current_iteration]
            self._current_iteration += 1
            if item:
                return item.key, item.value

        raise StopIteration

    def __len__(self) -> int:
        return self._size

    def __str__(self) -> str:
        return str(self._hash_table)

    def _resize_hash_table(self) -> None:
        previous_hash_table = self._hash_table

        self.__init__(
            self._capacity * self._capacity_multiplier,
            self._load_factor,
            self._capacity_multiplier
        )

        for node in previous_hash_table:
            if node:
                self[node.key] = node.value

    def clear(self) -> None:
        self._size = 0
        self._hash_table = [None] * self._capacity

    def get(self, key: Hashable, default_value: Any = None) -> Any:
        try:
            return self[key]
        except KeyError:
            return default_value

    def pop(self, key: Hashable, default_value: Any = None) -> Any:
        try:
            item = self[key]
            del self[key]
            return item.value
        except KeyError:
            return default_value

    def keys(self) -> list[Hashable]:
        return [
            item.key
            for item in self._hash_table
            if isinstance(item, Dictionary.Node)
        ]

    def values(self) -> list[Any]:
        return [
            item.value
            for item in self._hash_table
            if isinstance(item, Dictionary.Node)
        ]

    def items(self) -> list[tuple[Hashable, Any]]:
        return [
            (item.key, item.value)
            for item in self._hash_table
            if isinstance(item, Dictionary.Node)
        ]

    def update(self, other: Dictionary = None) -> None:
        if other:
            for key, value in other.items():
                self[key] = value
