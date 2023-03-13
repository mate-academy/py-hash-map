from typing import Any


class Dictionary:

    load_factor = 2 / 3

    def __init__(self) -> None:
        self.capacity = 8
        self.length = 0
        self.hash_table: list = [None] * self.capacity

    def resize(self) -> None:
        hash_table_to_resize = self.hash_table
        self.capacity *= 2
        self.hash_table: list = [None] * self.capacity
        self.length = 0
        for node in hash_table_to_resize:
            if node:
                key, value, hash_value = node
                self.__setitem__(key, value)

    def __setitem__(self, key: int | float | str | bool, value: Any) -> None:
        if self.length > int(self.capacity * self.load_factor):
            self.resize()

        index = hash(key) % self.capacity
        while self.hash_table[index]:
            if self.hash_table[index][0] == key:
                break
            index = (index + 1) % self.capacity
        else:
            self.length += 1
        self.hash_table[index] = key, value, hash(key)

    def __getitem__(self, key: int | float | str | bool) -> Any:
        index = hash(key) % self.capacity

        while self.hash_table[index]:
            if (
                    hash(key) == self.hash_table[index][2]
                    and key == self.hash_table[index][0]
            ):
                return self.hash_table[index][1]

            index = (index + 1) % self.capacity

        raise KeyError(f"There is no key/value pair assigned to key: '{key}'")

    def __delitem__(self, key: int | float | str | bool) -> None:
        index = hash(key) % self.capacity

        if not self.hash_table[index][1]:
            pass

        while self.hash_table[index]:
            if (
                    hash(key) == self.hash_table[index][2]
                    and key == self.hash_table[index][0]
            ):
                self.hash_table[index] = (
                    None,
                    None,
                    self.hash_table[index][2]
                )
                self.length - 1

            index = (index + 1) % self.capacity

    @classmethod
    def clear(cls) -> None:
        cls.capacity = 8
        cls.length = 0
        cls.hash_table: list = [None] * cls.capacity

    def __len__(self) -> int:
        return self.length
