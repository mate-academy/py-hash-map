from typing import Any, Hashable


class Dictionary:
    def __init__(self) -> None:
        self.length: int = 0
        self.initial_capacity: int = 8
        self.load_factor: float = 2 / 3
        self.resize: int = 2
        self.hash_table: list = [None] * self.initial_capacity

    def __setitem__(self, key: Hashable, value: Any) -> None:
        hash_key = hash(key)

        index = hash_key % self.initial_capacity
        node = [key, hash_key, value]

        while True:
            if self.hash_table[index] is None:
                self.hash_table[index] = node
                self.length += 1
                break
            if key == self.hash_table[index][0]:
                self.hash_table[index][2] = value
                break

            index = (index + 1) % self.initial_capacity

        if self.length >= self.initial_capacity * self.load_factor:
            self.__resize()

    def __getitem__(self, key: Hashable) -> Any:
        index = hash(key) % self.initial_capacity
        while self.hash_table[index] is not None:
            if self.hash_table[index][0] == key:
                return self.hash_table[index][2]
            index = (index + 1) % self.initial_capacity
        raise KeyError(f"{key} is not in the dictionary")

    def __len__(self) -> int:
        return self.length

    def __resize(self) -> None:
        self.initial_capacity *= 2
        self.length = 0
        last_table = self.hash_table
        self.hash_table = [None] * self.initial_capacity
        for element in last_table:
            if element is not None:
                self.__setitem__(element[0], element[2])
