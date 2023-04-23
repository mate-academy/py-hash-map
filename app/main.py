from typing import Hashable, Any


class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.hash_table: list = [None] * 8

    def resize(self) -> None:
        new_hash_table = [None] * len(self.hash_table) * 2
        for i in range(len(self.hash_table)):
            if self.hash_table[i] is not None:
                key, hash_key, value = self.hash_table[i]
                index = hash_key % len(new_hash_table)
                while True:
                    if new_hash_table[index] is None:
                        new_hash_table[index] = self.hash_table[i]
                        break
                    if key == new_hash_table[index][0]:
                        new_hash_table[index][2] = value
                        break
                    index = (index + 1) % len(new_hash_table)
        self.hash_table = new_hash_table

    def __setitem__(self, key: Hashable, value: Any) -> None:
        hash_key = hash(key)
        if self.length > len(self.hash_table) * 2 / 3:
            self.resize()
        index = hash_key % len(self.hash_table)
        node = [key, hash_key, value]
        while True:
            if self.hash_table[index] is None:
                self.hash_table[index] = node
                self.length += 1
                break
            if key == self.hash_table[index][0]:
                self.hash_table[index][2] = value
                break
            index = (index + 1) % len(self.hash_table)

    def __getitem__(self, key: Hashable) -> None:
        hash_key = hash(key)
        index = hash_key % len(self.hash_table)
        while True:
            if self.hash_table[index] is None:
                raise KeyError
            if key == self.hash_table[index][0]:
                return self.hash_table[index][2]
            index = (index + 1) % len(self.hash_table)

    def __len__(self) -> int:
        return self.length
