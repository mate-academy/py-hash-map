from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.load_factor = 5
        self.filled_cells = 0
        self.hash_table = [None] * self.capacity

    def __setitem__(self,
                    key: int | float | str | bool | tuple,
                    value: Any) -> None:
        index = hash(key) % self.capacity
        if self.hash_table[index] is None:
            self.hash_table[index] = []
        for cell in self.hash_table[index]:
            if cell[0] == key:
                cell[1] = hash(key)
                cell[2] = value
                return
        self.hash_table[index].append([key, hash(key), value])
        self.filled_cells += 1

    def __getitem__(self, key: int | float | str | bool | tuple) -> Any:
        index = hash(key) % self.capacity
        if self.hash_table[index] is None:
            raise KeyError
        for cell in self.hash_table[index]:
            if (
                    cell[1] == hash(key)
                    and cell[0] == key
            ):
                return cell[2]
        raise KeyError()

    def resize(self) -> None:
        hash_table_ = self.hash_table
        self.capacity = self.capacity * 2
        self.hash_table = [None] * self.capacity
        self.load_factor = int(self.capacity * (2 / 3))
        self.filled_cells = 0
        for cell in hash_table_:
            if cell is not None:
                self[cell[0]] = cell[2]

    def __len__(self) -> int:
        return self.filled_cells
