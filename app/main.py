from typing import Hashable, Any
from app.point import Point
import random


class Dictionary:
    capacity = 8

    def __init__(self):
        self.table = self.table_update()
        self.size = 0
        self.trashold = int(self.capacity * (2/3)) + 1

    def table_update(self):
        return [None] * self.capacity

    def increase_capacity(self):
        self.capacity *= 2
        temp_table = [None] * self.capacity
        for hash_table_list in self.table:
            if hash_table_list is not None:
                index = hash_table_list[1] % self.capacity
                while temp_table[index] is not None:
                    index = random.randint(0, self.capacity - 1)
                temp_table[index] = hash_table_list
        self.table = temp_table
        self.trashold = int(self.capacity * (2 / 3)) + 1

    def __setitem__(self, key, value):
        if self.size + 1 == self.trashold:
            self.increase_capacity()

        key_hash = hash(key)
        index = key_hash % self.capacity

        if self.table[index] is None:
            self.table[index] = [key, key_hash, value]
        elif self.table[index][0] == key and self.table[index][1] == key_hash:
            self.table[index] = [key, key_hash, value]
        else:
            try:
                self.__getitem__(key)
            except KeyError:
                while self.table[index] is not None:
                    index = random.randint(0, self.capacity - 1)
                self.table[index] = [key, key_hash, value]
            else:
                for index, el in enumerate(self.table):
                    if el is not None and el[0] == key and el[1] == key_hash:
                        self.table[index][2] = value
                        break
        self.size += 1

    def __getitem__(self, key):
        for i in self.table:
            if i is not None and i[0] == key:
                return i[2]
        raise KeyError(key)

    def __len__(self):
        return self.size


if __name__ == '__main__':
    pass



