from __future__ import annotations
from copy import deepcopy
from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.hash_table: list = [[None, None] for _ in range(8)]
        self.capacity = 8

    def key_upp(self, key: int) -> int:
        key += 1
        if key == self.capacity:
            key = 0
        return key

    def write(self, index: int, key: Any, value: Any) -> None:
        self.hash_table[index][0] = key
        self.hash_table[index][1] = value

    def resize(self) -> None:
        self.capacity *= 2
        old_hash_tabel = deepcopy(self.hash_table)
        self.hash_table = [[None, None] for _ in range(self.capacity)]
        for pair_key_value in old_hash_tabel:
            if pair_key_value[0] is None:
                continue
            index = hash(pair_key_value[0]) % self.capacity
            for _ in range(self.capacity):
                if self.hash_table[index][0] is None:
                    self.write(index, pair_key_value[0], pair_key_value[1])
                    break
                index += 1
                if index == self.capacity:
                    index = 0
        del old_hash_tabel

    def __setitem__(self, key: Any, value: Any) -> None:

        if self.length > self.capacity * 2 // 3:
            self.resize()

        index = hash(key) % self.capacity
        for _ in range(self.capacity):
            if self.hash_table[index][0] is None:
                self.write(index, key, value)
                self.length += 1
                break
            else:
                if self.hash_table[index][0] == key:
                    self.write(index, key, value)
                    break
            index = self.key_upp(index)

    def __getitem__(self, key: Any) -> Any:
        index = hash(key) % self.capacity
        for _ in range(self.capacity):
            if self.hash_table[index][0] == key:
                return self.hash_table[index][1]
            index = self.key_upp(index)
        raise KeyError

    def __len__(self) -> int:
        return self.length
