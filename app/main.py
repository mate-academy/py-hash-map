from typing import Any, List, Optional

from dataclasses import dataclass


@dataclass()
class Node:
    hash: int
    key: Any
    value: Any


class Dictionary:
    _DEFAULT_LENGTH = 8
    _RESIZE_COEF = 2 / 3
    _RESIZE_MULTIPLICATOR = 2

    def __init__(self):
        self._table: List[Optional[Node]] = [None for _ in range(Dictionary._DEFAULT_LENGTH)]
        self._capacity = Dictionary._DEFAULT_LENGTH
        self._size = 0

    def __setitem__(self, key, value):
        index = self._index(hash(key))
        while self._table[index] is not None:
            current_key, _ = self._table[index]
            if key == current_key:
                self._table[index] = (current_key, value)
                return
            index = self._index(index + 1)

        self._table[index] = (key, value)
        self._size += 1

        if self._size >= self._capacity * self._RESIZE_COEF:
            self._resize()

    def __getitem__(self, key, data):
        index = self._index(hash(data))
        while self._table[index] is not None:
            key, value = self._table[index]
            if key == data:
                return value
            index = self._index(index + 1)
        raise KeyError

    def __len__(self):
        return self._size

    def _resize(self):
        old = [item for item in self._table if item]
        self._capacity *= 2
        self._size = 0
        self._table = [None] * self._capacity

        for key, value in old:
            self[key] = value

    def _index(self, hashed_value):
        return hashed_value % self._capacity
