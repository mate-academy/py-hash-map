from __future__ import annotations
from typing import Any, Hashable

INITIAL_CAPACITY = 8
LOAD_FACTOR = 2 / 3
RESIZE_FACTOR = 2


class Node:
    def __init__(self, key: Hashable, value: Any) -> None:
        self.key = key
        self.value = value
        self.hash_key = hash(key)


class Dictionary:

    def __init__(self, **kwargs: Any) -> None:
        self._length = 0
        self._dict_keys: list = []
        self._dict_values: list = []
        self._capacity: int = INITIAL_CAPACITY
        self._hash_table: list = [None] * self._capacity
        for key, value in kwargs.items():
            self.__setitem__(key, value)

    def __str__(self) -> str:
        items = []
        for node in self._hash_table:
            if node is not None:
                items.append(f"'{node.key}': {node.value}")
        return "{" + ", ".join(items) + "}"

    def __setitem__(self, key: Hashable, value: Any) -> None:
        node = Node(key, value)
        index = node.hash_key % self._capacity

        while (self._hash_table[index] is not None
               and self._hash_table[index].key != key):
            index = (index + 1) % self._capacity

        if self._hash_table[index] is None:
            self._length += 1

        self._hash_table[index] = node

        if self._length / self._capacity >= LOAD_FACTOR:
            self._resize()

    def __getitem__(self, key: Hashable) -> Any:
        key_hash = hash(key)
        index = key_hash % self._capacity

        while (self._hash_table[index] is not None
               and self._hash_table[index].key != key):
            index = (index + 1) % self._capacity

        if self._hash_table[index] is None:
            raise KeyError(key)

        return self._hash_table[index].value

    def __len__(self) -> int:
        return self._length

    def __delitem__(self, key: Hashable) -> None:
        key_hash = hash(key)
        index = key_hash % self._capacity

        while (self._hash_table[index] is not None
               and self._hash_table[index].key != key):
            index = (index + 1) % self._capacity

        if self._hash_table[index] is None:
            raise KeyError(key)

        self._hash_table[index] = None
        self._length -= 1

    def keys(self) -> Any:
        for i in range(len(self._hash_table)):
            if self._hash_table[i] is not None:
                self._dict_keys.append(self._hash_table[i].key)
        return self._dict_keys

    def values(self) -> Any:
        for i in range(len(self._hash_table)):
            if self._hash_table[i] is not None:
                self._dict_values.append(self._hash_table[i].value)
        return self._dict_values

    def items(self) -> list:
        return [(self.hash_table[i].key, self._hash_table[i].value) for i in
                range(len(self._hash_table)) if
                self._hash_table[i] is not None]

    def clear(self) -> None:
        self.hash_table = []
        self._dict_keys = []
        self._dict_values = []
        self._length = 0

    def get(self, key: Hashable) -> Any:
        return self.__getitem__(key)

    def pop(self, _key: Any) -> Any:
        if self._hash_table[hash(_key) % self._capacity] is None:
            raise KeyError(_key)
        key_value = self._hash_table[hash(_key) % self._capacity].value
        self.__delitem__(_key)
        return key_value

    def update(self, new_dict: Dictionary) -> None:
        for key, value in new_dict.items():
            self[key] = value

    def __iter__(self) -> Any:
        for i in range(len(self._hash_table)):
            if self._hash_table[i] is not None:
                yield self._hash_table[i]

    def _resize(self) -> None:
        self._capacity *= RESIZE_FACTOR
        new_table = [None] * self._capacity

        for node in self._hash_table:
            if node is not None:
                index = node.hash_key % self._capacity

                while (new_table[index] is not None
                       and new_table[index].key != node.key):
                    index = (index + 1) % self._capacity

                new_table[index] = node

        self._hash_table = new_table
