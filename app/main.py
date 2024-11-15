from typing import Any

import copy


class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.hash_table: list = [None] * 8
        self.len_hash_tabel = len(self.hash_table)

    def __len__(self) -> int:
        return self.length

    def get_cell_index(self, key: Any) -> int:
        return hash(key) % self.len_hash_tabel

    def resize_hash_tabel(self) -> None:
        old_tabel = copy.deepcopy(self.hash_table)
        self.hash_table = self.len_hash_tabel * [None] * 2
        self.len_hash_tabel = len(self.hash_table)
        self.length = 0
        for cell in old_tabel:
            if cell is not None:
                created_key, _, created_value = cell
                self.__setitem__(created_key, created_value)
        del old_tabel

    def threshold(self) -> int:
        return int((2 / 3) * self.len_hash_tabel)

    def check_threshold(self) -> bool:
        return self.length < self.threshold()

    def __setitem__(self, key: Any, value: Any) -> None:
        if not self.check_threshold():
            self.resize_hash_tabel()

        hashed_key = hash(key) % self.len_hash_tabel
        sell = self.hash_table[hashed_key]

        if sell is None:
            self.hash_table[hashed_key] = [key, hash(key), value]
            self.length += 1

        if sell is not None:
            found_key = False
            for index, cell in enumerate(self.hash_table):
                if cell is not None:
                    record_key, _, record_value = cell
                    if record_key == key:
                        found_key = True
                        break

            if found_key:
                self.hash_table[index] = [key, hash(key), value]
            else:
                index = self.hash_table.index(None)
                self.hash_table[index] = [key, hash(key), value]
                self.length += 1

    def __getitem__(self, key: Any) -> Any:
        found_key = False
        for index, cell in enumerate(self.hash_table):
            if cell is not None:
                record_key, _, record_value = cell
                if record_key == key:
                    found_key = True
                    break
        if found_key:
            return record_value
        raise KeyError

    def __delitem__(self, key: Any) -> None:
        found_key = False
        for index, cell in enumerate(self.hash_table):
            if cell is not None:
                record_key, _, record_value = cell
                if record_key == key:
                    found_key = True
                    break
        if found_key:
            self.hash_table.remove(cell)
            self.hash_table.append(None)
        else:
            raise KeyError
