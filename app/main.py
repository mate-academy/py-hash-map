from __future__ import annotations
from app.point import Point
from typing import Any, Hashable
import inspect


class Dictionary:

    def __init__(self) -> None:
        self.hash_table = [[]] * 8
        self.current_bucket = 8
        self.current_size = 0

    def __setitem__(self,
                    key: Hashable,
                    value: Any) -> None:

        if not isinstance(key, (int, str, tuple, float, Point)):
            raise KeyError

        index = hash(key) % self.current_bucket

        while True:
            if self.hash_table[index] and key == self.hash_table[index][0]:
                self.hash_table[index] = [key, value]
                break
            if not self.hash_table[index]:
                self.hash_table[index] = [key, value]
                self.current_size += 1
                break

            index = (index + 1) % self.current_bucket

        if self.current_size == int(self.current_bucket * (2 / 3)) + 1:
            self.__resize()

    def __getitem__(self, item: Hashable) -> Any:
        if item not in self.keys():
            raise KeyError

        index = hash(item) % self.current_bucket

        while True:
            if self.hash_table[index][0] == item:
                return self.hash_table[index][1]

            index = (index + 1) % self.current_bucket

    def __delitem__(self, item: Hashable, pop: bool = False) -> Any | None:
        if item not in self.keys():
            raise KeyError

        index = hash(item) % self.current_bucket

        while True:
            if (pop and self.hash_table[index]
                    and self.hash_table[index][0] == item):
                value = self.hash_table[index][1]
                self.hash_table[index] = []
                self.current_size -= 1
                return value

            if self.hash_table[index] and self.hash_table[index][0] == item:
                self.hash_table[index] = []
                self.current_size -= 1
                break

            index = (index + 1) % self.current_bucket

        if 8 < self.current_size < int(self.current_bucket / 2 * (2 / 3)):
            self.__resize()

    def __len__(self) -> int:
        return self.current_size

    def __iter__(self) -> Dictionary:
        self.iter_index = -1
        return self

    def __next__(self) -> Any:
        while self.iter_index <= self.current_bucket:
            self.iter_index += 1
            try:
                if self.hash_table[self.iter_index]:
                    return self.hash_table[self.iter_index]
            except IndexError:
                raise StopIteration

    def keys(self) -> list[Hashable]:
        return [pair[0] for pair in self.hash_table if pair]

    def values(self) -> list[Any]:
        return [pair[1] for pair in self.hash_table if pair]

    def get(self, key: Hashable) -> Any:
        return self.__getitem__(key)

    def pop(self, key: Hashable, default: bool = False) -> None:
        keys = self.keys()
        if not default and key not in keys:
            raise KeyError
        if default and key not in keys:
            return default
        return self.__delitem__(key, pop=True)

    def clear(self) -> None:
        self.current_bucket = 8
        self.current_size = 0
        self.hash_table = [[]] * self.current_bucket

    def __resize(self):
        if inspect.stack()[1].function == "__setitem__":
            self.current_bucket *= 2
        if inspect.stack()[1].function == "__delitem__":
            self.current_bucket //= 2
        self.__old_table = self.hash_table.copy()
        self.current_size = 0
        self.hash_table = [[]] * self.current_bucket

        self.__recalculation(self.__old_table)

    def __recalculation(self, table: list) -> None:
        for cell in table:
            if cell:
                self.__setitem__(*cell)
