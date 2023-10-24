from typing import Any


class Dictionary:
    def __init__(
            self,
            initial_capacity: int = 8,
            load_factor: float = 2 / 3
    ) -> None:
        self.initial_capacity = initial_capacity
        self.load_factor = load_factor
        self.size = 0
        self.hash_table = [None] * initial_capacity

    def hash(self, key: Any) -> Any:
        return hash(key) % self.initial_capacity

    def resize(self) -> None:
        self.initial_capacity *= 2
        new_table = [None] * self.initial_capacity
        for item in self.hash_table:
            if item is not None:
                for key, value in item:
                    index = hash(key) % self.initial_capacity
                    if new_table[index] is None:
                        new_table[index] = []
                    new_table[index].append([key, value])
        self.hash_table = new_table

    def __setitem__(self, key: Any, value: Any) -> None:
        index = self.hash(key)
        if self.hash_table[index] is None:
            self.hash_table[index] = []
        for entry in self.hash_table[index]:
            if entry[0] == key:
                entry[1] = value
                return
        self.hash_table[index].append([key, value])
        self.size += 1
        if self.size >= self.load_factor * self.initial_capacity:
            self.resize()

    def __getitem__(self, key: Any) -> Any:
        index = self.hash(key)
        if self.hash_table[index] is not None:
            for entry in self.hash_table[index]:
                if entry[0] == key:
                    return entry[1]
        raise KeyError(key)

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        return str(self.hash_table)
