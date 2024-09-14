from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.hash_table = [None] * self.capacity
        self.load_factor = self.calculate_factor()
        self.size = 0

    def calculate_factor(self) -> int:
        return int(self.capacity * (2 / 3))

    def get_position(self, key: Any) -> int:
        key_hash = hash(key)
        position = key_hash % self.capacity

        while (self.hash_table[position] is not None
               and self.hash_table[position][0] != key):
            position += 1
            position = position % self.capacity

        return position

    def __setitem__(self, key: Any, value: Any) -> None:
        if self.size >= self.load_factor:
            self.increase()
        position = self.get_position(key)
        if self.hash_table[position] is None:
            self.size += 1
        self.hash_table[position] = (key, value, hash(key))

    def __getitem__(self, item: Any) -> Any:
        position = self.get_position(item)
        if not self.hash_table[position]:
            raise KeyError(item)
        if self.hash_table[position][0] == item:
            return self.hash_table[position][1]

    def increase(self) -> None:
        old_hash_table = self.hash_table.copy()
        self.capacity *= 2
        self.load_factor = self.calculate_factor()
        self.hash_table = [None] * self.capacity
        self.size = 0
        for i in old_hash_table:
            if i:
                key, value, key_hash = i
                self.__setitem__(key, value)

    def __len__(self) -> int:
        return self.size
