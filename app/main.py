from __future__ import annotations
from app.point import Point
from typing import Any, Hashable


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
            index += 1
            if index > self.current_bucket - 1:
                index = 0

        if self.current_size == int(self.current_bucket * (2 / 3)) + 1:
            self.__table_size_up()

    def __getitem__(self, item: Hashable) -> Any:
        if item not in self.keys():
            raise KeyError

        index = hash(item) % self.current_bucket

        while True:
            if self.hash_table[index][0] == item:
                return self.hash_table[index][1]
            index += 1
            if index > self.current_bucket - 1:
                index = 0

    def __delitem__(self, item: Hashable) -> None:
        index = hash(item) % self.current_bucket

        while True:
            if self.hash_table[index] and self.hash_table[index][0] == item:
                self.hash_table[index] = []
                self.current_size -= 1
                break
            index += 1
            if index > self.current_bucket - 1:
                index = 0

        if 8 < self.current_size < int(self.current_bucket / 2 * (2 / 3)):
            self.__table_size_down()

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

    def __table_size_up(self) -> None:
        self.__increased_table = [[]] * self.current_bucket * 2
        self.current_bucket *= 2
        self.current_size = 0

        self.hash_table = self.__recalculation(self.__increased_table)

    def __table_size_down(self) -> None:
        self.__reduced_table = [[]] * int(self.current_bucket / 2)
        self.current_bucket //= 2
        self.current_size = 0

        self.hash_table = self.__recalculation(self.__reduced_table)

    def __recalculation(self, table: list) -> list:
        for cell in self.hash_table:
            if cell:
                index = hash(cell[0]) % self.current_bucket
                while True:
                    if not table[index]:
                        table[index] = [cell[0], cell[1]]
                        self.current_size += 1
                        break
                    index += 1
                    if index > self.current_bucket - 1:
                        index = 0
        return table
