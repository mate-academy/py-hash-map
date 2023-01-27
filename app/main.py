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
            new_key = hash(pair_key_value[0]) % self.capacity
            for _ in range(self.capacity):
                if self.hash_table[new_key][0] is None:
                    self.write(new_key, pair_key_value[0], pair_key_value[1])
                    break
                new_key += 1
                if new_key == self.capacity:
                    new_key = 0
        del old_hash_tabel

    def __setitem__(self, key: Any, value: Any) -> None:
        key_hash_rewrite = hash(key) % self.capacity
        if self.hash_table[key_hash_rewrite][0] is not None:
            for _ in range(self.capacity):
                if self.hash_table[key_hash_rewrite][0] == key:
                    self.hash_table[key_hash_rewrite][1] = value
                    return
                key_hash_rewrite = self.key_upp(key_hash_rewrite)

        if self.length > self.capacity * 2 // 3:
            self.resize()

        key_hash = hash(key) % self.capacity
        for _ in range(self.capacity):
            if self.hash_table[key_hash][0] is None:
                self.write(key_hash, key, value)
                self.length += 1
                break
            key_hash = self.key_upp(key_hash)

    def __getitem__(self, key: Any) -> Any:
        key_hash = hash(key) % self.capacity
        for _ in range(self.capacity):
            if self.hash_table[key_hash][0] == key:
                return self.hash_table[key_hash][1]
            key_hash = self.key_upp(key_hash)
        raise KeyError

    def __len__(self) -> int:
        return self.length
