from typing import Any, Hashable


class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.hash_table: list = [None] * 8
        self.size = len(self.hash_table)

    def __setitem__(
        self, key: Hashable, value: Any
    ) -> None:
        index = hash(key) % self.size
        while (
            self.hash_table[index] is not None
            and self.hash_table[index][0] != key
            and self.hash_table[index][1] != hash(key)
        ):
            index = (index + 1) % self.size
        if self.hash_table[index] is None:
            self.length += 1
        self.hash_table[index] = (key, value, hash(key))
        if self.length > self.size * (2 / 3):
            self.resize()

    def __getitem__(self, key: Hashable) -> Any:
        index = hash(key) % self.size
        if not self.hash_table[index]:
            raise KeyError(key)
        while self.hash_table[index][0] != key:
            index = (index + 1) % self.size
        return self.hash_table[index][1]

    def resize(self) -> None:
        self.size *= 2
        self.length = 0
        hash_table_copy = self.hash_table
        self.hash_table = [None] * self.size
        for item in hash_table_copy:
            if item:
                key, value, _ = item
                self.__setitem__(key, value)

    def __len__(self) -> int:
        return self.length
