from typing import Any, Hashable


class Dictionary:
    def __init__(self) -> None:
        self.hash_capacity: int = 8
        self.hash_table: list = [None] * self.hash_capacity
        self.iter_table: list = []
        self.iter_no = 0

    def __setitem__(self, key: Hashable, value: Any) -> None:
        try:
            hash_key = hash(key)
            if self.hash_capacity / (self.__len__() + 1) <= 1.5:
                self.resize()
            hash_index = hash_key % self.hash_capacity
            while self.hash_table[hash_index] is not None:
                if self.hash_table[hash_index][0] == key \
                        and self.hash_table[hash_index][1] == hash_key:
                    self.hash_table[hash_index][2] = value
                    break
                hash_index: int = (hash_index + 1) % self.hash_capacity
            self.hash_table[hash_index] = [key, hash_key, value]
        except TypeError:
            print(f"Unhashable type: {str(type(key)).split()[-1]}!")

    def __getitem__(self, key: Hashable) -> Any:
        try:
            hash_key = hash(key)
            hash_index = hash_key % self.hash_capacity
            while self.hash_table[hash_index][1] != hash_key \
                    or self.hash_table[hash_index][0] != key:
                hash_index = (hash_index + 1) % self.hash_capacity
            result_value = self.hash_table[hash_index][2]
            return result_value
        except (TypeError, KeyError):
            raise KeyError("Not found that index!")

    def __len__(self) -> int:
        return len(self.hash_table) - self.hash_table.count(None)

    def clear(self) -> None:
        self.hash_table = [None] * self.hash_capacity

    def __delitem__(self, key: Hashable) -> None:
        hash_key = hash(key)
        hash_index = hash_key % self.hash_capacity
        while self.hash_table[hash_index][1] != hash_index \
                and self.hash_table[hash_index][0] != key:
            hash_index += 1
        self.hash_table[hash_index] = None

    def get(self) -> dict:
        return {cell_no[0]: cell_no[2]
                for cell_no in self.hash_table if cell_no is not None}

    def pop(self, key: Hashable) -> Any:
        deleted_value = self.__getitem__(key)
        self.__delitem__(key)
        return deleted_value

    def update(self, other_dictionary: Any) -> None:
        if isinstance(other_dictionary, Dictionary):
            for other_cell in other_dictionary.hash_table:
                if other_cell is not None:
                    self.__setitem__(other_cell[0], other_cell[2])

    def __iter__(self) -> Any:
        self.iter_no = 0
        return self

    def __next__(self) -> str:
        if self.iter_no < self.hash_capacity - 1:
            self.iter_no += 1
            if self.hash_table[self.iter_no] is None:
                exit()
            return f"{self.hash_table[self.iter_no][0]}: " \
                   f"{self.hash_table[self.iter_no][2]}"
        else:
            raise StopIteration

    def __repr__(self) -> str:
        dict_repr = {cell[0]: cell[2]
                     for cell in self.hash_table if cell is not None}
        return str(dict_repr)

    def resize(self) -> None:
        hash_table_old = self.hash_table
        self.hash_capacity *= 2
        self.hash_table = [None] * self.hash_capacity
        for cell in hash_table_old:
            if cell is not None:
                self.__setitem__(cell[0], cell[2])
