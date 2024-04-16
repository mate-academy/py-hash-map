from collections.abc import Hashable
from typing import Any
from app.point import Point


class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.capacity = 8
        self.load_factor = 2 / 3
        self.hash_table: list = [[]] * self.capacity

    def __setitem__(self, key: Hashable, value: Any) -> None:
        table_index = hash(key) % self.capacity
        if self.length == round(self.capacity * self.load_factor):
            self.resize()

        # if not self.hash_table[table_index]:
        #     self.hash_table[table_index][0] = (key, hash(key), value)
        #     self.length += 1
        #     return
        for cell in self.hash_table[table_index]:
            if cell[0] == key:
                cell[2] = value
                return
        self.hash_table[table_index].append([key, hash(key), value])
        self.length += 1
        # elif self.hash_table[table_index][0] == key:
        #     self.hash_table[table_index] = (key, hash(key), value)
        # else:
        #     while True:
        #         if self.hash_table[table_index]:
        #             table_index += 1
        #             continue
        #         self.hash_table[table_index] = (key, hash(key), value)
        #         break

    def __getitem__(self, item: Any) -> Any:
        table_index = hash(item) % self.capacity
        for cell in self.hash_table[table_index]:
            if cell[0] == item:
                return cell[2]
        raise KeyError
            # if (self.hash_table[table_index]
            #     and self.hash_table[table_index][0] == item):
            #     return self.hash_table[table_index][2]
            # table_index += 1
        # raise KeyError

        # for cell in self.hash_table:
        #     if cell and item in cell:
        #         return cell[2]
        #     # if it's the last cell, it's index == length - 1
        #     if self.hash_table.index(cell) == len(self.hash_table) - 1:
        #         raise KeyError

        # while True:
        #     if table_index == len(self.hash_table):
        #         raise KeyError
        #     if self.hash_table[table_index] and item in self.hash_table[table_index]:
        #         return self.hash_table[table_index][2]
        #     table_index += 1

    def __len__(self) -> int:
        return self.length

    def resize(self):
        self.capacity *= 2
        old_table_copy = self.hash_table.copy()
        self.hash_table = [[]] * self.capacity
        for cell in old_table_copy:
            if not cell:
                key = cell[0]
                key_index = hash(key) % self.capacity
                self.hash_table[key_index] = cell
            # for ele in cell:
            #     self.__setitem__(ele[0], ele[2])
                # if cell is not None:
                #     new_index = cell[1] % self.capacity
                #     if self.hash_table[new_index] is None:
                #         self.hash_table[new_index] = cell
                #     else:
                #         empty_cell = self.hash_table.index(None)
                #         self.hash_table[empty_cell] = cell
                    # for i, c in enumerate(self.hash_table):
                    #     if c is None:
                    #         self.hash_table[i] = cell
                    #         break
                    #     else:
                    #         continue
