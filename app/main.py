from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Hashable


@dataclass
class DictItem:
    key: Hashable
    value: Any


class Dictionary:
    def __init__(self) -> None:
        self._capacity = 8
        self._load_factor = 2 / 3
        self._threshold = int(self._capacity * self._load_factor)
        self._size = 0
        self._source = [None for _ in range(self._capacity)]

    def __setitem__(self, key: Hashable, value: Any) -> None:
        index = hash(key) % self._capacity
        is_exist = False
        while (item := self._source[index]) is not None:
            if item.key == key:
                is_exist = True
                break
            if index == self._capacity - 1:
                index = 0
            else:
                index += 1
        self._source[index] = DictItem(key, value)
        if not is_exist:
            self._size += 1
        if self._size > self._threshold:
            self._resize()

    def __getitem__(self, key: Hashable) -> Any:
        index = hash(key) % self._capacity
        while (item := self._source[index]) is not None:
            if item.key == key:
                return item.value
            if index == self._capacity - 1:
                index = 0
            else:
                index += 1
        raise KeyError(key)

    def __delitem__(self, key: Hashable) -> None:
        index = hash(key) % self._capacity
        if self._source[index] is None:
            raise KeyError(key)
        self._source[index] = None
        self._size -= 1

    def __iter__(self) -> Dictionary:
        self.iter = 0
        return self

    def __next__(self) -> Any:
        while self._source[self.iter] is None:
            self.iter += 1
            if self.iter == self._capacity:
                del self.iter
                raise StopIteration
        result = self._source[self.iter]
        self.iter += 1
        return result

    def __len__(self) -> int:
        return self._size

    def _resize(self) -> None:
        self._size = 0
        items = [self._source[index]
                 for index in range(self._capacity)
                 if self._source[index] is not None]
        self._capacity *= 2
        self._threshold = int(self._capacity * self._load_factor)
        self._source = [None for _ in range(self._capacity)]
        for item in items:
            self[item.key] = item.value

    def clear(self) -> None:
        self._capacity = 8
        self._source = [None for _ in range(self._capacity)]

    def pop(self, key: Hashable) -> Any:
        value = self[key]
        del self[key]
        self._size -= 1
        return value

    def get(self, key: Hashable, default: Any) -> Any:
        try:
            return self[key]
        except KeyError:
            return default

    def update(self, other: Dictionary | dict) -> None:
        if isinstance(other, Dictionary):
            for index in range(other._capacity):
                item = other._source[index]
                if item is not None:
                    self[item.key] = item.value
        elif isinstance(other, dict):
            for key, value in other.items():
                self[key] = value
        raise TypeError("Argument is not a dict or Dictionary")
