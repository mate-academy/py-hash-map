from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.hash_table = self.create_hash_table()
        self.load_factor = self.calculate_factor()
        self.size = 0

    def create_hash_table(self) -> list:
        return [None for _ in range(self.capacity)]

    def calculate_factor(self) -> int:
        return int(self.capacity * (2 / 3))

    def __setitem__(self, key: Any, value: Any) -> None:
        key_hash = hash(key)
        position = key_hash % self.capacity
        while True:
            if not self.hash_table[position]:
                self.hash_table[position] = (key, value, key_hash)
                self.size += 1
                if self.size >= self.load_factor:
                    self.increase()
                break
            elif self.hash_table[position][0] == key:
                self.hash_table[position] = (key, value, key_hash)
                break
            position += 1
            position %= self.capacity

    def __getitem__(self, item: Any) -> Any:
        key_hash = hash(item)
        position = key_hash % self.capacity
        while True:
            if not self.hash_table[position]:
                raise KeyError
            if self.hash_table[position][0] == item:
                return self.hash_table[position][1]
            position += 1
            position %= self.capacity

    def increase(self) -> None:
        old_hash_table = self.hash_table.copy()
        self.capacity *= 2
        self.load_factor = self.calculate_factor()
        self.hash_table = self.create_hash_table()
        self.size = 0
        for i in old_hash_table:
            if i:
                key, value, key_hash = i
                self.__setitem__(key, value)

    def __len__(self) -> int:
        return self.size
# im tired, i need more practice
