from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.table_size = 8
        self.hash_table: list = [None] * self.table_size

    def __setitem__(
            self,
            key: (int, float, bool, tuple, str),
            value: Any
    ) -> None:
        hashed_value = hash(key)
        index = hashed_value % self.table_size
        while self.hash_table[index] is not None:
            saved_key, saved_hashed_value, saved_value = self.hash_table[index]
            if saved_key == key and hashed_value == saved_hashed_value:
                self.hash_table[index] = (key, hashed_value, value)
                break
            print(f"The key {key} collided with {self.hash_table[index]}")
            index = (index + 1) % len(self.hash_table)
        if self.hash_table[index] is None:
            self.hash_table[index] = (key, hashed_value, value)
            self.length += 1
            self.resize()

    def __getitem__(
            self,
            key: (int, float, bool, tuple, str)
    ) -> Any:
        hashed_value = hash(key)
        index = hashed_value % self.table_size
        while True:
            try:
                if self.hash_table[index][0] == key:
                    return self.hash_table[index][2]
            except TypeError:
                raise KeyError
            index = (index + 1) % self.table_size

    def __len__(self) -> int:
        return self.length

    def resize(self) -> None:
        if self.length > 2 / 3 * self.table_size:
            copy_table = [data for data in self.hash_table if data is not None]
            self.table_size *= 2
            self.hash_table = [None] * self.table_size
            self.length = 0
            for key, hashed_value, value in copy_table:
                self.__setitem__(key, value)
