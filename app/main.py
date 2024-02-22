from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.hash_table: list = [None] * 8

    def __setitem__(
            self,
            key: int | float | str | tuple,
            value: Any
    ) -> None:
        key_hash = hash(key)
        if len(self) >= len(self.hash_table) * (2.0 / 3):
            self.update()
        index = key_hash % len(self.hash_table)
        while True:
            if not self.hash_table[index]:
                self.length += 1
            if not self.hash_table[index] or self.hash_table[index][0] == key:
                self.hash_table[index] = (key, key_hash, value)
                return
            index += 1
            if index >= len(self.hash_table):
                index = 0

    def __getitem__(self, key: int | float | str | tuple) -> Any:
        return self.hash_table[self.get(key)][2]

    def get(self, key: int | float | str | tuple) -> int | KeyError:
        key_hash = hash(key)
        start_index = key_hash % len(self.hash_table)
        index = start_index
        while True:
            if self.hash_table[index] and self.hash_table[index][0] == key:
                return index
            index += 1
            if index >= len(self.hash_table):
                index = 0
            if index == start_index:
                raise KeyError("Key was not found")

    def __len__(self) -> int:
        return self.length

    def __delitem__(self, key: int | float | str | tuple) -> None:
        index = self.get(key)
        self.hash_table[index] = None
        self.length -= 1

    def update(self) -> None:
        copy_hash_table = self.hash_table
        self.hash_table = [None] * len(self) * 2
        self.length = 0
        for item in copy_hash_table:
            if item:
                self[item[0]] = item[2]

    def __iter__(self) -> tuple:
        for item in self.hash_table:
            if item:
                yield item

    def clear(self) -> None:
        self.hash_table.clear()
