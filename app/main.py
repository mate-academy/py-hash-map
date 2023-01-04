from typing import Any, Union

from app.point import Point


class Dictionary:
    def __init__(self) -> None:
        self.length = 8
        self.size = 0
        self.hash_table = [(None,)] * self.length

    def __setitem__(
            self,
            key: Union[str, int, tuple, Point],
            value: Any
    ) -> list:
        if self.size / self.length >= 0.625:
            self.length *= 2
            self.hash_table += [(None,)] * self.length

        index = hash(key) % len(self.hash_table)
        if self.hash_table[index][0] is None:
            self.hash_table[index] = [key, value]
            self.size += 1
            return self.hash_table
        for pairs in self.hash_table:
            if pairs[0] == key:
                pairs[1] = value
                return self.hash_table

        next_index = (index + 1) % len(self.hash_table)
        while self.hash_table[next_index][0] is not None:
            next_index = (next_index + 1) % len(self.hash_table)

        self.hash_table[next_index] = [key, value]
        self.size += 1
        return self.hash_table

    def __getitem__(self, input_key: Union[str, int, tuple, Point]) -> Any:
        for key in self.hash_table:
            if key[0] == input_key:
                return key[1]
        raise KeyError(f"Key {input_key} does not exist")

    def __len__(self) -> int:
        return self.size

    def __delitem__(self, key: Union[str, int, tuple, Point]) -> list:
        index = hash(key) % len(self.hash_table)
        self.hash_table.pop(index)
        self.hash_table.insert(index, (None,))

    def clear(self) -> None:
        self.hash_table.clear()
        self.size = 0
        self.hash_table = [(None,)] * self.length

    def pop(self, key: Union[str, int, tuple, Point]) -> Any:
        index = hash(key) % len(self.hash_table)
        del_el = self.hash_table.pop(index)
        self.hash_table.insert(index, (None,))
        return del_el
