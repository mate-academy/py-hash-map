from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.hash_table: list = [None] * 8
        self.hash_table_capacity = 8
        self.hash_table_threshold = 5

    def __setitem__(self, key: Any, value: Any) -> None:
        position = hash(key) % self.hash_table_capacity

        while True:
            if self.hash_table[position] is None:
                self.hash_table[position] = (key, hash(key), value)
                self.length += 1
                break

            if self.hash_table[position][0] == key:
                self.hash_table[position] = (key, hash(key), value)
                break

            position += 1

            if position > self.hash_table_threshold - 1:
                position = 0

        if self.length == self.hash_table_threshold:
            self.rehash()

    def rehash(self) -> None:
        hash_table = self.hash_table
        self.hash_table_capacity *= 2
        self.hash_table_threshold = round(self.hash_table_capacity * (2 / 3))
        self.hash_table = [None] * self.hash_table_capacity
        self.length = 0

        for item in hash_table:
            if item is not None:
                self.__setitem__(item[0], item[2])

    def __getitem__(self, item: Any) -> Any:
        position = hash(item) % self.hash_table_capacity
        count = 0

        while True:
            if self.hash_table[position] is None:
                raise KeyError

            if self.hash_table[position][0] == item:
                return self.hash_table[position][2]

            count += 1
            if count == self.hash_table_threshold:
                raise KeyError

            position += 1

            if position > self.hash_table_threshold - 1:
                position = 0

    def __len__(self) -> int:
        return self.length
