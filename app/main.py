from typing import Any, Hashable


class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.hash_table: list = [None] * 8
        self.capacity = 8
        self.load_factor = 2 / 3
        self.resize = 2
        self.threshold = self.capacity * self.load_factor

    def __len__(self) -> int:
        return self.length

    def get_ind(self, key: Hashable) -> object:
        index = hash(key) % self.capacity
        while self.hash_table[index] and self.hash_table[index][0] != key:
            index = (index + 1) % self.capacity
        return index

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.length > self.threshold:
            table_copy = self.hash_table
            self.capacity *= self.resize
            self.threshold = self.capacity * self.load_factor
            self.hash_table = [None] * self.capacity
            self.length = 0

            for element in table_copy:
                if element:
                    self[element[0]] = element[2]

        ind = self.get_ind(key)
        if self.hash_table[ind] is None:
            self.length += 1

        self.hash_table[ind] = (key, hash(key), value)

    def __getitem__(self, key: Hashable) -> Any:
        ind = self.get_ind(key)
        if not self.hash_table[ind]:
            raise KeyError
        return self.hash_table[ind][2]
