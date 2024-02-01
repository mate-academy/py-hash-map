from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.hash_table: list = [None] * 8

    def resize_hash_table(self) -> None:
        new_table = [None] * (2 * len(self.hash_table))
        for item in self.hash_table:
            if item:
                self.set_item(key=item[0], value=item[2], table=new_table)
        self.hash_table = new_table

    @staticmethod
    def set_item(key: Any, value: Any, table: list) -> bool:
        key_hash = hash(key)
        index = key_hash % len(table)
        cell = table[index]
        if cell is None:
            table[index] = (key, key_hash, value)
            return True
        elif cell[0] == key:
            table[index] = (key, key_hash, value)
        else:
            while True:
                index += 1
                if index >= len(table):
                    index = 0
                next_cell = table[index]
                if next_cell is None:
                    table[index] = (key, key_hash, value)
                    return True
                elif next_cell[0] == key:
                    table[index] = (key, key_hash, value)
                    break

    def __setitem__(self, key: Any, value: Any) -> None:
        if self.set_item(key=key, value=value, table=self.hash_table):
            self.length += 1
        if self.length >= int(len(self.hash_table) * (2 / 3)):
            self.resize_hash_table()

    def __getitem__(self, key: Any) -> None:
        iteration = 1
        key_hash = hash(key)
        index = key_hash % len(self.hash_table)
        cell = self.hash_table[index]
        if cell and cell[0] == key:
            return cell[2]
        else:
            while True:
                index += 1
                iteration += 1
                if index >= len(self.hash_table):
                    index = 0
                next_cell = self.hash_table[index]
                if next_cell and next_cell[0] == key:
                    return next_cell[2]
                elif iteration == len(self.hash_table):
                    raise KeyError(key)

    def __len__(self) -> int:
        return self.length
