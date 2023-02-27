from typing import Any, Hashable


class Dictionary:

    def __init__(self, table_len: int = 8, load_factor: float = 0.75) -> None:
        self.table_len = table_len
        self.load_factor = load_factor
        self.length = 0
        self.hash_table: list = [None] * 8

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.table_len < int(self.length * 2 / 3):
            self.resize()
        hash_key = hash(key)
        index = hash_key % self.table_len
        while True:
            if not self.hash_table[index]:
                self.hash_table[index] = [key, value, hash_key]
                self.length += 1
                break
            elif self.hash_table[index][0] == key and self.hash_table[index][2] == hash_key:
                self.hash_table[index][1] = value
                break
            else:
                index = (index + 1) % self.table_len

    def __getitem__(self, key: Hashable) -> Any:
        hash_key = hash(key)
        index = hash_key % self.table_len
        while self.hash_table[index]:
            if self.hash_table[index][0] == key:
                return self.hash_table[index][1]
            index = (index + 1) % self.table_len
        raise KeyError

    def __len__(self) -> int:
        return self.length

    def resize(self) -> None:
        self.table_len *= 2
        self.length = 0
        start_table = self.hash_table
        self.hash_table = [None] * self.table_len
        for cell in start_table:
            if cell:
                self.__setitem__(cell[0], cell[1])