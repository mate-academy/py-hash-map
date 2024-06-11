from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.size = 0
        self.hash_table = self.create_hash_table()
        self.load_factor = self.calculate_load_factor()

    def create_hash_table(self) -> list:
        return [None for _ in range(self.capacity)]

    def calculate_load_factor(self) -> int:
        return int(self.capacity * (2 / 3))

    def __len__(self) -> int:
        return self.size

    def __setitem__(self, key: Any, value: Any) -> None:
        hash_key = hash(key)
        position = hash_key % self.capacity
        while True:
            if not self.hash_table[position]:
                self.hash_table[position] = (key, value, hash_key)
                self.size += 1
                if self.size >= self.load_factor:
                    self.resize()
                break
            elif self.hash_table[position][0] == key:
                self.hash_table[position] = (key, value, hash_key)
                break
            position += 1
            position %= self.capacity

    def __getitem__(self, item: Any) -> Any:
        hash_key = hash(item)
        position = hash_key % self.capacity
        while True:
            if not self.hash_table[position]:
                raise KeyError
            if self.hash_table[position][0] == item:
                return self.hash_table[position][1]
            position += 1
            position %= self.capacity

    def resize(self) -> None:
        self.capacity *= 2
        self.size = 0
        self.load_factor = self.calculate_load_factor()
        old_table = self.hash_table.copy()
        self.hash_table = self.create_hash_table()
        for item in old_table:
            if item:
                key, value, hash_key = item
                self.__setitem__(key, value)
