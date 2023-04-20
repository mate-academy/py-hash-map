from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.threshold = 5
        self.filled_cells = 0
        self.hash_table = [[] for _ in range(self.capacity)]

    def __setitem__(self,
                    key: int | float | str | bool | tuple,
                    value: Any) -> None:
        if self.filled_cells == self.threshold:
            self.resize()
        hash_key = hash(key)
        index = hash_key % self.capacity

        while True:
            if not self.hash_table[index]:
                self.hash_table[index] = [hash_key, key, value]
                self.filled_cells += 1
                return
            if self.hash_table[index][1] == key:
                self.hash_table[index][0] = hash_key
                self.hash_table[index][2] = value
                return
            index = (index + 1) % self.capacity

    def __getitem__(self, key: int | float | str | bool | tuple) -> Any:
        hash_key = hash(key)
        index = hash_key % self.capacity

        while self.hash_table[index]:
            if self.hash_table[index][:2] == [hash_key, key]:
                return self.hash_table[index][2]
            index = (index + 1) % self.capacity
        raise KeyError

    def resize(self) -> None:
        hash_table_ = self.hash_table
        self.capacity = self.capacity * 2
        self.hash_table = [[] for _ in range(self.capacity)]
        self.threshold = int(self.capacity * (2 / 3))
        self.filled_cells = 0
        for cell in hash_table_:
            if cell:
                self.__setitem__(cell[1], cell[2])

    def __len__(self) -> int:
        return self.filled_cells
