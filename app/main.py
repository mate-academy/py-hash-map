from __future__ import annotations
from copy import deepcopy


class Dictionary:
    def __init__(self) -> None:
        self.len = 0

        self.hash_table: list = [[None, None] for _ in range(8)]
        self.capacity = 8

    def __setitem__(self, key: callable, value: callable) -> None:
        if value is None:
            raise ValueError
        good_keys = {list, dict}
        if type(key) in good_keys:
            raise KeyError

        key_hash_rewrite = hash(key) % self.capacity
        if self.hash_table[key_hash_rewrite][0] is not None:
            for _ in range(self.capacity):
                if self.hash_table[key_hash_rewrite][0] == key:
                    self.hash_table[key_hash_rewrite][1] = value
                    return
                key_hash_rewrite += 1
                if key_hash_rewrite == self.capacity:
                    key_hash_rewrite = 0

        if self.len > self.capacity * 2 // 3:
            self.capacity *= 2
            old_hash_tabel = deepcopy(self.hash_table)
            del self.hash_table
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

        key_hash = hash(key) % self.capacity
        for _ in range(self.capacity):
            if self.hash_table[key_hash][0] is None:
                self.hash_table[key_hash][0] = key
                self.hash_table[key_hash][1] = value
                self.len += 1
                break
            key_hash += 1
            if key_hash == self.capacity:
                key_hash = 0

    def __getitem__(self, key: callable) -> callable:
        keys_not_use = {list, dict}
        if type(key) in keys_not_use:
            raise KeyError
        key_hash = hash(key) % self.capacity
        for _ in range(self.capacity):
            if self.hash_table[key_hash][0] == key:
                return self.hash_table[key_hash][1]
            key_hash += 1
            if key_hash == self.capacity:
                key_hash = 0
        raise KeyError

    def __len__(self) -> int:
        return self.len
