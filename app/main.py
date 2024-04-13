from app.point import Point
from typing import Any
import sys


class Dictionary:

    def __init__(self) -> None:
        self.hash_table = [[]] * 8
        self.current_bucket = 8
        self.current_size = 0

    def __setitem__(self,
                    key: int | str | tuple | float | Point,
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
            self.table_size_up()

    def __getitem__(self, item: int | str | tuple | float | Point) -> Any:
        if item not in self.keys():
            raise KeyError

        index = hash(item) % self.current_bucket

        while True:
            if self.hash_table[index][0] == item:
                return self.hash_table[index][1]
            index += 1
            if index > self.current_bucket - 1:
                index = 0

    def __delitem__(self, item: int | str | tuple | float | Point) -> None:
        index = hash(item) % self.current_bucket

        while True:
            if self.hash_table[index] and self.hash_table[index][0] == item:
                self.hash_table[index] = []
                self.current_size -= 1
                break
            index += 1
            if index > self.current_bucket - 1:
                index = 0

        if self.current_size < int(self.current_bucket / 2 * (2 / 3)):
            self.table_size_down()

    def __len__(self) -> int:
        return self.current_size

    def keys(self) -> list[int | str | tuple | float | Point]:
        return [pair[0] for pair in self.hash_table if pair]

    def values(self) -> list[Any]:
        return [pair[1] for pair in self.hash_table if pair]

    def table_size_up(self) -> None:
        self.increased_table = [[]] * self.current_bucket * 2
        self.current_bucket *= 2
        self.current_size = 0

        self.hash_table = self.recalculation(self.increased_table)

    def table_size_down(self) -> None:
        self.reduced_table = [[]] * int(self.current_bucket / 2)
        self.current_bucket //= 2
        self.current_size = 0

        self.hash_table = self.recalculation(self.reduced_table)

    def recalculation(self, table: list) -> None:
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
