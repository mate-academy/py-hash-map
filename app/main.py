import dataclasses
import math
from typing import Any


@dataclasses.dataclass
class Node:
    key: Any
    value: Any


class Dictionary:
    INITIAL_CAPACITY = 8
    THRESHOLD = 2/3
    RESIZE_MULTIPLIER = 2

    def __init__(self):
        self.size = 0
        self.capacity = Dictionary.INITIAL_CAPACITY
        self.hash_table: list[Node | None] = [None] * self.capacity

    def __setitem__(self, key, value):
        table_index = hash(key) % self.capacity
        while self.hash_table[table_index] is not None:
            if self.hash_table[table_index].key == key:
                self.hash_table[table_index].value = value
                return
            table_index = (table_index + 1) % self.capacity

        if self.size >= math.floor(self.capacity * Dictionary.THRESHOLD):
            self._resize_hash_table()
            self.__setitem__(key=key, value=value)
            return

        self.size += 1
        self.hash_table[table_index] = Node(key=key, value=value)

    def _resize_hash_table(self):
        self.capacity *= Dictionary.RESIZE_MULTIPLIER
        nodes = [el for el in self.hash_table if el is not None]
        new_hash_table = [None] * self.capacity
        self.size = 0
        self.hash_table = new_hash_table
        for node in nodes:
            self.__setitem__(node.key, node.value)

    def __getitem__(self, item):
        table_index = hash(item) % self.capacity
        while self.hash_table[table_index] is not None:
            if self.hash_table[table_index].key == item:
                return self.hash_table[table_index].value
            table_index = (table_index + 1) % self.capacity
        raise KeyError(f"Key {item} is not in dictionary")

    def __len__(self):
        return self.size


if __name__ == '__main__':
    t_dict = Dictionary()

    t_dict[15] = 'A'
    t_dict[3] = 'B'
    t_dict[5] = 'C'
    t_dict[13] = 'D'
    t_dict[3] = 'BChanged'
    t_dict[11] = 'h'
    t_dict[33] = 'L'
    t_dict[56] = 'k'
    t_dict[78] = '88'

    print(t_dict.hash_table)
    print(len(t_dict))































    # def __init__(self):
    #
    #     self._values = [None for item in range(256)]
    #     self._keys = []
    #
    # def __getitem__(self, key):
    #
    #     if self._values[self.hashfunc(key)] is not None:
    #         return self._values[self.hashfunc(key)]
    #
    #     else:
    #         return self.__missing__(key)
    #
    # def __setitem__(self, key, value):
    #
    #     if value is None:
    #         raise ValueError('None is not permitted as a value.')
    #
    #     if self._values[self.hashfunc(key)] is None:
    #         self._keys.append(key)
    #         self._values[self.hashfunc(key)] = value
    #
    #         if float(len(self._keys)) / len(self._values) > 0.1:
    #             self.__resize__()
    #
    #     else:
    #         if key in self._keys:
    #             self._values[self.hashfunc(key)] = value
    #
    #         else:
    #             self.__resize__()
    #             self.__setitem__(key, value)
    #
    # def __missing__(self, not_key):
    #
    #     raise KeyError('{0} is not a valid key'.format(not_key))
    #
    # def __repr__(self):
    #
    #     list_repr = ['{0}:{1}'.format(key, self._values[self.hashfunc(key)])
    #                  for key in self._keys]
    #     return 'HashMap({0})'.format(list_repr)
    #
    # def __contains__(self, key):
    #
    #     if key in self._keys:
    #         return True
    #     else:
    #         return False
    #
    # def __len__(self):
    #
    #     return len(self._keys)
    #
    # def __iter__(self):
    #
    #     return (key for key in self._keys)
    #
    # def hashfunc(self, key):
    #     return hash(key) % len(self._values)
    #
    # def __resize__(self, **kwargs):
    #     old_values = kwargs.get('values', [self._values[self.hashfunc(key)]
    #                                        for key in self._keys])
    #
    #     self._values = [None for item in range(2 * len(self._values))]
    #
    #     for key, value in zip(self._keys, old_values):
    #
    #         if self._values[self.hashfunc(key)] is None:
    #             self._values[self.hashfunc(key)] = value
    #
    #         else:
    #             self.__resize__(values=old_values)
