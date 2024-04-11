from __future__ import annotations
from typing import Any, Hashable


class Dictionary:

    def __init__(self) -> None:

        self.length = 0
        self.capacity = 8
        self.load_factor = 2 / 3
        self.hash_table = [None] * self.capacity

    def threshold(self) -> None:
        return (
            self.hash_table.count(None)
            <= self.capacity * (1 - self.load_factor)
        )

    def resize(self) -> None:

        old_hash_table = self.hash_table.copy()
        self.capacity = self.capacity * 2
        self.hash_table = [None] * self.capacity

        for elem in old_hash_table:
            if elem is not None:
                self.set_element(elem[0], elem[2])

    def find_item_hash_index(self, key: Hashable) -> int:

        item_index = hash(key) % self.capacity

        if self.hash_table[item_index] is None:
            raise KeyError
        if self.hash_table[item_index][0] == key:
            return item_index
        for item_index, elem in enumerate(self.hash_table):
            if elem is not None and elem[0] == key:
                return item_index
        raise KeyError

    def set_element(self, key: Hashable, value: Any) -> bool:

        key_hash = hash(key)
        hash_table_index = key_hash % self.capacity
        while True:
            if (
                self.hash_table[hash_table_index] is None
                or self.hash_table[hash_table_index][0] == key
            ):
                is_new_element = self.hash_table[hash_table_index] is None
                self.hash_table[hash_table_index] = (key, key_hash, value)
                return is_new_element
            hash_table_index = (hash_table_index + 1) % self.capacity

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.threshold():
            self.resize()
        self.length += self.set_element(key, value)

    def __getitem__(self, key: Hashable) -> Any:
        hash_index = self.find_item_hash_index(key)
        return self.hash_table[hash_index][2]

    def __len__(self) -> int:
        return self.length

    def clear(self) -> None:
        self.hash_table = [None] * self.capacity

    def __delitem__(self, key: Hashable) -> None:
        try:
            hash_index = self.find_item_hash_index(key)
        except KeyError:
            return
        self.hash_table[hash_index] = None
        self.length -= 1

    def pop(self, key: Hashable) -> Any:

        value = self.__getitem__(key)
        self.__delitem__(key)
        return value

    def get(self, key: Hashable, default_value: Any = None) -> Any:
        try:
            return self.__getitem__(key)
        except KeyError:
            return default_value

    def update(self, other: Dictionary) -> Any:
        for elem in other.hash_table:
            if elem is not None:
                self.__setitem__(elem[0], elem[2])

    def __iter__(self) -> Dictionary:
        self.current = 0
        return self

    def __next__(self) -> Hashable:
        while self.current < self.capacity:
            if self.hash_table[self.current] is not None:
                return_value = self.hash_table[self.current][0]
                self.current += 1
                return return_value
            self.current += 1
        raise StopIteration

    def __repr__(self) -> str:
        items = []
        for elem in self.hash_table:
            if elem is not None:
                items.append(f"{elem[0]}: {elem[2]}")
        return "{" + ", ".join(items) + "}"
