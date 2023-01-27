from __future__ import annotations
from copy import deepcopy


class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.hash_table: list = [[None, None] for _ in range(8)]
        self.capacity = 8

    def resize(self) -> None:
        self.capacity *= 2
        old_hash_tabel = deepcopy(self.hash_table)
        self.hash_table = [[None, None] for _ in range(self.capacity)]
        for pair_key_value in old_hash_tabel:
            if pair_key_value[0] is None:
                continue
            new_key_hash = hash(pair_key_value[0]) % self.capacity
            for _ in range(self.capacity):
                if self.hash_table[new_key_hash][0] is None:
                    self.hash_table[new_key_hash][0] = pair_key_value[0]
                    self.hash_table[new_key_hash][1] = pair_key_value[1]
                    break
                new_key_hash += 1
                if new_key_hash == self.capacity:
                    new_key_hash = 0
        del old_hash_tabel

    def __setitem__(self, key: any, value: any) -> None:
        key_hash_rewrite = hash(key) % self.capacity
        if self.hash_table[key_hash_rewrite][0] is not None:
            for _ in range(self.capacity):
                if self.hash_table[key_hash_rewrite][0] == key:
                    self.hash_table[key_hash_rewrite][1] = value
                    return
                key_hash_rewrite += 1
                if key_hash_rewrite == self.capacity:
                    key_hash_rewrite = 0

        if self.length > self.capacity * 2 // 3:
            self.resize()

        key_hash = hash(key) % self.capacity
        for _ in range(self.capacity):
            if self.hash_table[key_hash][0] is None:
                self.hash_table[key_hash][0] = key
                self.hash_table[key_hash][1] = value
                self.length += 1
                break
            key_hash += 1
            if key_hash == self.capacity:
                key_hash = 0

    def __getitem__(self, key: any) -> any:
        key_hash = hash(key) % self.capacity
        for _ in range(self.capacity):
            if self.hash_table[key_hash][0] == key:
                return self.hash_table[key_hash][1]
            key_hash += 1
            if key_hash == self.capacity:
                key_hash = 0
        raise KeyError

    def __len__(self) -> int:
        return self.length
