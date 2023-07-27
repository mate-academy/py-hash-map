from typing import Any, Hashable


class Dictionary:
    def __init__(self) -> None:
        self.hash_capacity: int = 8
        self.hash_table: list = [None] * self.hash_capacity
        self.iter_no = 0
        self.dict_len = 0

    def __setitem__(self, key: Hashable, value: Any) -> None:
        try:
            hash_key = hash(key)
            if self.hash_capacity / (self.__len__() + 1) <= 1.5:
                self.resize()
            hash_index = hash_key % self.hash_capacity
            for _ in range(self.hash_capacity):
                if self.hash_table[hash_index] is None:
                    self.hash_table[hash_index] = [key, hash_key, value]
                    self.dict_len += 1
                elif self.hash_table[hash_index][1] == hash_key \
                        and self.hash_table[hash_index][0] == key:
                    self.hash_table[hash_index][2] = value
                else:
                    hash_index: int = (hash_index + 1) % self.hash_capacity
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
        return self.dict_len

    def clear(self) -> None:
        self.hash_table = [None] * self.hash_capacity
        self.dict_len = 0

    def __delitem__(self, key: Hashable) -> None:
        hash_key = hash(key)
        hash_index = hash_key % self.hash_capacity
        while self.hash_table[hash_index][1] != hash_key \
                and self.hash_table[hash_index][0] != key:
            hash_index += 1
        self.hash_table[hash_index] = None
        self.dict_len -= 1

    def get(self) -> dict:
        return {cell_no[0]: cell_no[2]
                for cell_no in self.hash_table if cell_no}

    def pop(self, key: Hashable) -> Any:
        deleted_value = self.__getitem__(key)
        self.__delitem__(key)
        return deleted_value

    def update(self, other_dictionary: Any) -> None:
        if isinstance(other_dictionary, Dictionary):
            for other_cell in other_dictionary.hash_table:
                if other_cell:
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
        raise StopIteration

    def __repr__(self) -> str:
        dict_repr = self.get()
        return str(dict_repr)

    def resize(self) -> None:
        hash_table_old = self.hash_table
        self.hash_capacity *= 2
        self.hash_table = [None] * self.hash_capacity
        self.dict_len = 0
        for cell in hash_table_old:
            if cell:
                self.__setitem__(cell[0], cell[2])
