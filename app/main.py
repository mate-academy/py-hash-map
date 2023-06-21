from __future__ import annotations

from typing import Any, Hashable


class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.load_factor = 2 / 3
        self.hash_table = [None] * self.capacity

    def __getitem__(self, input_key: Hashable) -> None:
        for item in self.hash_table:
            if item is not None:
                if item[0] == input_key:
                    return item[2]
        raise KeyError

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if len(self) == round(self.capacity * self.load_factor):
            self.resize()
        index = hash(key) % self.capacity
        while (self.hash_table[index] is not None
               and self.hash_table[index][0] != key):
            index += 1
            if index > self.capacity - 1:
                index = 0
        self.hash_table[index] = (key, hash(key), value)

    def __len__(self) -> int:
        len_counter = 0
        for item in self.hash_table:
            if item is not None:
                len_counter += 1
        return len_counter

    def __delitem__(self, key: Hashable) -> None:
        if self[key]:
            for i in range(self.capacity):
                if self.hash_table[i] is not None:
                    if self.hash_table[i][0] == key:
                        self.hash_table[i] = None
                        break
        else:
            raise KeyError

    def resize(self) -> None:
        self.capacity *= 2
        old_hash_table_items = [item for item in self.hash_table
                                if item is not None]
        self.hash_table = [None] * self.capacity
        for key, _hash, value in old_hash_table_items:
            self[key] = value

    def get(self, input_key: Hashable) -> Any:
        for item in self.hash_table:
            if item is not None:
                if input_key == item[0]:
                    return item[2]

    def clear(self) -> None:
        self.__init__()

    def update(self, other: Dictionary) -> None:
        for item in other.hash_table:
            if item is not None:
                self[item[0]] = other[item[0]]

    def pop(self, key: Hashable) -> Any:
        if self[key]:
            for i in range(self.capacity):
                if self.hash_table[i] is not None:
                    if self.hash_table[i][0] == key:
                        popped_value = self.hash_table[i]
                        self.hash_table[i] = None
                        return popped_value

        else:
            raise KeyError
