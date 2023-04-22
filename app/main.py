from typing import Any, Hashable


class Dictionary:

    def __init__(self,
                 capacity: int = 8,
                 load_factor: float = 0.67
                 ) -> None:
        self.capacity = capacity
        self.load_factor = load_factor
        self.occupied = 0
        self.hash_table = [None] * self.capacity

    def __setitem__(
            self,
            key: Hashable,
            value: Any
    ) -> None:
        index_ = hash(key) % self.capacity
        while (self.hash_table[index_]
               and self.hash_table[index_][0] != key):
            index_ = (index_ + 1) % self.capacity
        if (self.hash_table[index_]
                and self.hash_table[index_][0] == key):
            self.hash_table[index_][1] = value
        if not self.hash_table[index_]:
            self.occupied += 1
            self.hash_table[index_] = [key, value]
        if self.occupied >= self.capacity * self.load_factor:
            self.__resize()

    def __getitem__(self,
                    key: Hashable
                    ) -> Any:
        index_ = hash(key) % self.capacity
        while self.hash_table[index_]:
            if self.hash_table[index_][0] == key:
                return self.hash_table[index_][1]
            index_ = (index_ + 1) % self.capacity
        raise KeyError(f"{key} is not in the dictionary")

    def __len__(self) -> int:
        return self.occupied

    def __resize(self) -> None:
        table_copy = self.hash_table
        self.capacity = self.capacity * 2
        self.hash_table = [None] * self.capacity
        self.occupied = 0
        for node in table_copy:
            if node:
                self[node[0]] = node[1]
