from typing import Any, Hashable


class Dictionary:
    capacity = 8
    load_factor = 2 / 3
    size = 0

    def __init__(self) -> None:
        self.hash_table = self.create_hash_table(8)

    def __len__(self) -> int:
        return self.size

    def __setitem__(self, key: Hashable, value: Any) -> None:
        self.size += 1
        if self.size > self.load_factor * self.capacity:
            self.resize()
        index = hash(key) % self.capacity

        keys = [key[0] for key in self.hash_table]
        if key in keys:
            while keys[index] != key:
                index += 1
                if index > self.capacity:
                    index = 0
            self.hash_table[index] = [key, value]
            self.size -= 1
        else:
            while self.hash_table[index] != [None, None]:
                index += 1
                if index > self.capacity:
                    index = 0
            self.hash_table[index] = [key, value]

    def __getitem__(self, find_key: Hashable) -> any:
        coli = 0
        index = hash(find_key) % self.capacity
        while True:
            key_d, val = self.hash_table[index]
            if key_d != find_key:
                coli += 1
                index += 1
                if index > self.capacity:
                    index = 0
                if coli > self.capacity * 2:
                    raise KeyError("Error due to big count of collisions!!")
            else:
                return val

    @staticmethod
    def create_hash_table(size: int) -> list:
        return [[None, None] for _ in range(size + 1)]

    def calculate_index(self, hash_key: int) -> int:
        index = hash_key % self.capacity
        return index

    def resize(self) -> None:
        temp = self.hash_table
        self.capacity *= 2
        self.hash_table = self.create_hash_table(self.capacity)
        for fill_cell in temp:
            if fill_cell != [None, None]:
                key, val = fill_cell
                index = hash(key) % self.capacity
                while self.hash_table[index] != [None, None]:
                    index += 1
                    if index > self.capacity:
                        index = 0
                self.hash_table[index] = (key, val)
