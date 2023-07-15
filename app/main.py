from app.point import Point
from typing import Hashable, Any


class Dictionary:
    def __init__(self, capacity: int = 8) -> None:
        self._capacity = capacity
        self._load_factor = 0.75
        self._size = 0
        self._table = [None] * capacity

    def __setitem__(self, key: Hashable, value: Any) -> None:
        hash_key = hash(key)
        index = hash_key % self._capacity
        node = key, hash_key, value
        if self._table[index] is None:
            self._table[index] = [node]
            self._size += 1
        else:
            found = False
            for i in range(len(self._table[index])):
                if self._table[index][i][0] == key and \
                        self._table[index][i][1] == hash_key:

                    self._table[index][i] = node
                    found = True
                    break
            if not found:
                self._table[index].append(node)
                self._size += 1
        if self._size / self._capacity > self._load_factor:
            self._resize()

    def __getitem__(self, key: Hashable) -> None:
        hash_key = hash(key)
        index = hash_key % self._capacity
        if self._table[index] is None:
            raise KeyError(key)
        else:
            for node in self._table[index]:
                if node[0] == key and node[1] == hash_key:
                    return node[2]
            raise KeyError(key)

    def __len__(self) -> int:
        return self._size

    def _resize(self) -> None:
        new_capacity = self._capacity * 2
        new_table = [None] * new_capacity
        for index in range(self._capacity):
            if self._table[index] is not None:
                for node in self._table[index]:
                    new_index = node[1] % new_capacity
                    if new_table[new_index] is None:
                        new_table[new_index] = [node]
                    else:
                        new_table[new_index].append(node)
        self._capacity = new_capacity
        self._table = new_table



