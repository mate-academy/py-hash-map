from typing import Union


class Dictionary:

    def __init__(self, keys: list[Union] = None, values: list[Union] = None) -> None:
        self.length: int = 0
        self.hash_table: list = [None] * 8
        self.keys = keys
        self.values = values
        self.need_key: Union = None
        for i in range(len(keys)):
            self.__setitem__(keys[i], values[i])

    def __setitem__(self, key: Union, value: Union) -> None:
        if (
            self.hash_table.count(None)
                == (
                    len(self.hash_table)
                    - int(len(self.hash_table) * 2 / 3)
                )
        ):
            copy_old_table = self.hash_table.copy()
            self.hash_table = [None] * len(self.hash_table) * 2
            for cell in copy_old_table:
                if cell:
                    self.need_key = cell[0]
                    self.hash_table[hash(self)] = cell
        self.need_key = key
        self.hash_table[hash(self)] = [key, value]
        self.length = len(self.hash_table) - self.hash_table.count(None)

    def __getitem__(self, key: Union) -> Union:
        self.need_key = key
        if not self.hash_table[hash(self)]:
            raise KeyError
        return self.hash_table[hash(self)][1]

    def __hash__(self) -> int:
        first_hash = hash(self.need_key) % len(self.hash_table)
        for _ in self.hash_table:
            if (
                    not self.hash_table[first_hash]
                    or self.hash_table[first_hash][0] == self.need_key
            ):
                return first_hash
            if first_hash == len(self.hash_table) - 1:
                first_hash = 0
            else:
                first_hash += 1

    def __len__(self) -> Union:

        return self.length



