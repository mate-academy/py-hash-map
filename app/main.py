from __future__ import annotations
from typing import Any


class Dictionary:
    def __init__(self, capacity: int = 8, load_factor: float = 0.67) -> None:
        self.capacity = capacity
        self.load_factor = load_factor
        self.threshold = int(self.capacity * self.load_factor)
        self.length = 0
        self.hash_table = [None] * self.capacity

    def __setitem__(self, key: Any, value: Any) -> None:
        index = hash(key) % len(self.hash_table)
        while self.hash_table[index] and self.hash_table[index][0] != key:
            index = (index + 1) % len(self.hash_table)
        if self.hash_table[index] and self.hash_table[index][0] == key:
            self.hash_table[index] = (key, hash(key), value)
        else:
            self.hash_table[index] = (key, hash(key), value)
            self.length += 1
            if self.length >= self.threshold:
                self.resize()

    def __getitem__(self, key: Any) -> None:
        index = hash(key) % len(self.hash_table)
        while self.hash_table[index]:
            if self.hash_table[index][0] == key:
                return self.hash_table[index][2]
            index = (index + 1) % len(self.hash_table)
        raise KeyError(key)

    def __len__(self) -> int:
        return self.length

    def resize(self) -> None:
        self.capacity *= 2
        new_table = self.hash_table
        self.hash_table = [None] * self.capacity
        self.threshold = int(self.capacity * self.load_factor)
        self.length = 0
        for i in new_table:
            if i:
                self[i[0]] = i[2]

    def __delitem__(self, key: Any) -> None:
        index = hash(key) % len(self.hash_table)
        while self.hash_table[index]:
            if self.hash_table[index][0] == key:
                self.hash_table[index] = None
                self.length -= 1
                return
            index = (index + 1) % len(self.hash_table)
        raise KeyError(key)

    def get(self, key: Any, default: None = None) -> None:
        try:
            return self[key]
        except KeyError:
            return default

    def clear(self) -> None:
        self.hash_table = [None] * self.capacity
        self.length = 0

    def pop(self, key: Any, default: None = None) -> None:
        try:
            value = self[key]
            del self[key]
            return value
        except KeyError:
            return default

    def update(self, other_dict: dict) -> None:
        for key, value in other_dict.items():
            self[key] = value

    def __iter__(self) -> None:
        for item in self.hash_table:
            if item:
                yield item[0]
