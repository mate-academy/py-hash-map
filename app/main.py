from copy import copy
from typing import Union, Any


class Dictionary:
    def __init__(self):
        self.length = 0
        self.capacity = 8
        self.load_factor = round(self.capacity * 2 / 3)
        self.table = [[] for i in range(self.length)]  # [[key, hash, value]]

    def _resize(self):
        temp = copy(self.table)
        self.capacity *= 2
        self.length = 0
        self.table = [[] for i in range(self.capacity)]

        for node in temp:
            if node:
                self.__setitem__(node[0], node[1])

    def __setitem__(
            self,
            key: Union[int, float, str, bool, tuple],
            value: Any
    ):
        if self.length == self.capacity:
            self._resize()

        index = hash(key) % self.capacity
        for _ in range(self.capacity):
            node = self.table[index]
            if node and node[0] != key:
                index = (index + 1) % 8
            elif node and node[0] == key:
                node[2] = value
            else:
                node.append([key, hash(key), value])
                self.length += 1

    def __getitem__(self, key: Union[int, float, str, bool, tuple]):
        index = hash(key) % self.capacity
        for _ in range(self.capacity):
            node = self.table[index]
            if node[0] == key:
                return node[2]
            index = (index + 1) % self.capacity

        raise KeyError

    def __len__(self) -> int:
        return self.length

    def clear(self) -> None:
        self.length = 0
        self.capacity = 8
        self.load_factor = round(self.capacity * 2 / 3)
        self.table = [[] for i in range(self.length)]

    def __delitem__(self, key):
