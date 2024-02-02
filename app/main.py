from typing import Any, Hashable


class Dictionary:

    def __init__(self) -> None:
        self.capacity = 8
        self.load_factor = 2 / 3
        self.hash_table = [None] * self.capacity
        self.count = 0

    def __setitem__(self, key: Hashable, value: Any) -> None:
        index = self.calculate_index(key)

        if not self.hash_table[index]:
            self.count += 1

            if self.count >= int(self.capacity * self.load_factor):
                self.resize()
                index = self.calculate_index(key)

        self.hash_table[index] = (key, hash(key), value)

    def __getitem__(self, key: Hashable) -> Any:
        index = self.calculate_index(key)

        if not self.hash_table[index]:
            raise KeyError

        return self.hash_table[index][2]

    def __len__(self) -> int:
        return self.count

    def resize(self) -> None:
        self.capacity *= 2
        old_hash_table = self.hash_table
        self.hash_table = [None] * self.capacity

        for item in old_hash_table:
            if item:
                key, hash_, value = item
                self.hash_table[self.calculate_index(key)] = \
                    (key, hash_, value)

    def calculate_index(self, key: Hashable) -> int:
        index = hash(key) % self.capacity

        while self.hash_table[index] and self.hash_table[index][0] != key:
            index = (index + 1) % self.capacity

        return index
