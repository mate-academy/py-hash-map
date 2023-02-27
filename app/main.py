from typing import Any, Hashable


class Dictionary:
    def __init__(self, capacity: int = 8, load_factor: float = 2 / 3) -> None:
        self.capacity = capacity
        self.load_factor = load_factor
        self.threshold = int(self.capacity * self.load_factor)
        self.length = 0
        self.hash_table = [None] * self.capacity

    def __len__(self) -> int:
        return self.length

    def resize(self) -> None:
        self.capacity *= 2
        new_table = [None] * self.capacity
        for item in self.hash_table:
            if item is not None:
                index = item[1] % self.capacity
                while (
                        new_table[index] is not None
                        and new_table[index][0] != item[0]
                ):
                    index = (index + 1) % self.capacity
                new_table[index] = item
        self.hash_table = new_table

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.length / self.capacity > self.load_factor:
            self.resize()
        key_hash = hash(key)
        index = key_hash % self.capacity
        while (self.hash_table[index] is not None
               and self.hash_table[index][0] != key):
            index = (index + 1) % self.capacity

        if self.hash_table[index] is None:
            self.length += 1
            self.hash_table[index] = (key, key_hash, value)
        else:
            self.hash_table[index] = (key, self.hash_table[index][1], value)

    def __getitem__(self, key: Hashable) -> None:
        key_hash = hash(key)
        index = key_hash % self.capacity
        while (self.hash_table[index] is not None
               and self.hash_table[index][0] != key):
            index = (index + 1) % self.capacity
        if self.hash_table[index] is None:
            raise KeyError(key)
        return self.hash_table[index][2]

    def __delitem__(self, key: Hashable) -> None:
        index = hash(key) % self.capacity
        if index is not None:
            self.hash_table[index] = None
            self.count -= 1
        else:
            raise KeyError(f"{key} is not in {self}")
