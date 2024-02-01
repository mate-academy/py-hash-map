from typing import Hashable, Any


class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.hash_table: list = [None] * 8
        self.initial_capacity = 8
        self.load_factor = self.initial_capacity * 2 // 3

    def __setitem__(self, key: Hashable, value: Any) -> None:
        self.length += 1
        if self.length > self.load_factor:
            self.resize()

        self.hash_table[self.get_index(key)] = (key, hash(key), value)

    def __getitem__(self, key: Hashable) -> Any:
        for item in self.hash_table:
            if item and key == item[0]:
                return item[2]
        raise KeyError

    def __len__(self) -> int:
        return self.length

    def resize(self) -> None:
        new_hash_table: list = [None] * (self.initial_capacity * 2)
        for i in range(self.initial_capacity):
            if self.hash_table[i]:
                new_hash_table[i] = self.hash_table[i]

        self.initial_capacity *= 2
        self.load_factor = self.initial_capacity * 2 // 3
        self.hash_table = new_hash_table

    def get_index(self, key: Hashable) -> int:
        index = hash(key) % self.initial_capacity
        for item in self.hash_table:
            if item and item[0] == key:
                index = self.hash_table.index(item)
                self.length -= 1
        if self.hash_table[index] and (key != self.hash_table[index][0]):
            for i in range(index, self.initial_capacity * 2):
                if not self.hash_table[i % self.initial_capacity]:
                    index = i % self.initial_capacity
                    break
        return index
