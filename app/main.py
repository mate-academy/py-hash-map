from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Hashable


@dataclass
class DictItem:
    key: Hashable
    value: Any


class Dictionary:
    _capacity = 8
    _load_factor = 2 / 3
    _threshold = 5

    def __init__(self) -> None:
        self._size = 0
        self._store = [None for _ in range(self._capacity)]

    def get(self, key: Hashable, default: Any = None) -> Any:
        try:
            return self[key]
        except KeyError:
            return default

    def pop(self, key: Hashable) -> Any:
        value = self[key]
        del self[key]
        self._size -= 1
        return value

    def update(self, other: Dictionary | dict) -> None:
        if isinstance(other, Dictionary):
            for index in range(other._capacity):
                item = other._store[index]
                if item is not None:
                    self[item.key] = item.value
        elif isinstance(other, dict):
            for key, value in other.items():
                self[key] = value
        raise TypeError("Argument is not a dict or Dictionary")

    def clear(self) -> None:
        self._capacity = 8
        self._threshold = 5
        self._store = [None for _ in range(self._capacity)]

    def _resize(self) -> None:
        self._size = 0
        items = self._store
        self._capacity *= 2
        self._threshold = int(self._capacity * self._load_factor)
        self._store = [None for _ in range(self._capacity)]
        for item in items:
            if item is not None:
                self[item.key] = item.value

    def __setitem__(self, key: Hashable, value: Any) -> None:
        index = hash(key) % self._capacity
        key_exists = False
        while (item := self._store[index]) is not None:
            if item.key == key:
                key_exists = True
                break
            index = (index + 1) % self._capacity
        self._store[index] = DictItem(key, value)
        if not key_exists:
            self._size += 1
            if self._size > self._threshold:
                self._resize()

    def __getitem__(self, key: Hashable) -> Any:
        index = hash(key) % self._capacity
        while (item := self._store[index]) is not None:
            if item.key == key:
                return item.value
            index = (index + 1) % self._capacity
        raise KeyError(key)

    def __delitem__(self, key: Hashable) -> None:
        index = hash(key) % self._capacity
        if self._store[index] is None:
            raise KeyError(key)
        self._store[index] = None
        self._size -= 1

    def __iter__(self) -> Dictionary:
        self.iter = iter(self._store)
        return self

    def __next__(self) -> Any:
        result = next(self.iter)
        while result is None:
            result = next(self.iter)
        return result.key

    def __len__(self) -> int:
        return self._size
