from math import floor
from typing import Any

from app.point import Point


class Dictionary:
    def __init__(self) -> None:
        self._initial_capacity: int = 8
        self._load_factor: float = 2 / 3
        self._resize: int = 5
        self._length = 0
        self._hash_table: list = [None] * self._initial_capacity

    def __setitem__(self, key, value) -> None:
        def set_item(key_item: Any, value_item: Any) -> None:
            hash_index = hash(key_item) % self._initial_capacity
            cell_in_table = self._hash_table
            while cell_in_table[hash_index] is not None:
                if cell_in_table[hash_index][0] == key_item:
                    break
                if hash_index < self._initial_capacity - 1:
                    hash_index += 1
                else:
                    hash_index = 0

            self._hash_table[hash_index] = [key_item, hash(key_item), value_item]

        if self._resize <= self._length:
            self._initial_capacity *= 2
            self._resize = floor(self._initial_capacity * self._load_factor)

            temporary_hash_table = list(self._hash_table)
            self._hash_table = [None] * self._initial_capacity

            for item in temporary_hash_table:
                if item:
                    set_item(item[0], item[2])
            del temporary_hash_table

        set_item(key, value)
        self._length = self._initial_capacity - self._hash_table.count(None)

    def __getitem__(self, item):
        hash_index = hash(item) % self._initial_capacity

        while self._hash_table[hash_index] is not None:
            if self._hash_table[hash_index][0] != item:
                if hash_index < self._initial_capacity - 1:
                    hash_index += 1
                else:
                    hash_index = 0
            else:
                return self._hash_table[hash_index][2]
        raise KeyError

    def __len__(self) -> int:
        return self._length

# my_dict = Dictionary()
# print(my_dict._hash_table)
# my_dict[Point(5, 5)] = 50
# print(my_dict._hash_table)
# my_dict[Point(6, 5)] = 75
# print(my_dict._hash_table)
# my_dict[Point(4, 6)] = 46
# print(my_dict._hash_table)
# my_dict[Point(6, 5)] = 150
# print(my_dict._hash_table)
# print(my_dict[Point(4, 6)])
# # my_dict[Point(4, 6)] = 100
# # print(my_dict._hash_table)
# # my_dict[Point(4, 6)] = 123
# # print(my_dict._hash_table)
# # my_dict[Point(15, 5)] = 5
# # print(my_dict._hash_table)
# print(len(my_dict))
# print(my_dict._initial_capacity)
# print(my_dict._resize)

