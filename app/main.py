from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.capacity_table = 8
        self.size_dict = 0
        self.table = [None, None, None] * self.capacity_table

    def __setitem__(self, key: Any, value: Any) -> None:
        key_hash = hash(key)
        index_table_cell = key_hash % self.capacity_table
        while True:
            if self.table[index_table_cell] is None:
                self.table[index_table_cell] = [key, value, key_hash]
                self.size_dict += 1
                break
            if (
                    self.table[index_table_cell][0] == key
                    and self.table[index_table_cell][2] == key_hash
            ):
                self.table[index_table_cell][1] = value
                break
            index_table_cell += 1

        if self.size_dict >= self.capacity_table * (2 / 3):
            self.resize_dict(self.table)

    def resize_dict(self, table_for_resize: list) -> None:
        self.capacity_table *= 2
        self.size_dict = 0
        self.table = [None] * self.capacity_table
        for item in table_for_resize:
            self.__setitem__(item[0], item[1])

    def __getitem__(self, key: Any) -> Any:
        key_hash = hash(key)
        index_table_cell = key_hash % self.capacity_table
        while True:
            if (
                    self.table[index_table_cell][0] == key
                    and self.table[index_table_cell][2] == key_hash
            ):
                return self.table[index_table_cell][1]
            index_table_cell += 1

    def __len__(self) -> int:
        return self.size_dict
