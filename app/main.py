from __future__ import annotations
from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.pairs = [[] for i in range(8)]

    def __setitem__(
            self,
            key: int | float | str | type | bool | tuple | frozenset,
            value: Any
    ) -> None:
        cell_index = hash(key) % len(self.pairs)
        step = 0
        for pair in self.pairs[cell_index:] + self.pairs[:cell_index]:
            if len(pair) == 0 or pair[0] == key:
                break
            step += 1
        self.pairs[(cell_index + step) % len(self.pairs)] = [key, value]
        self.resize()

    def resize(self) -> None:
        if len(self) > len(self.pairs) / 3 * 2:
            _items_present = {
                pair[0] : pair[1] for pair in self.pairs if len(pair) == 2
            }
            self.pairs = [[] for i in range(len(self.pairs) * 2)]
            for key, value in _items_present.items():
                self.__setitem__(key, value)

    def __getitem__(
            self,
            key: int | float | str | type | bool | tuple | frozenset
    ) -> Any:
        cell_index = hash(key) % len(self.pairs)
        for pair in self.pairs[cell_index:] + self.pairs[:cell_index]:
            if len(pair) == 2 and pair[0] == key:
                return pair[1]
        raise KeyError

    def __len__(self) -> int:
        return sum(len(pair) == 2 for pair in self.pairs)

    def clear(self) -> None:
        self.pairs = [[] for i in range(8)]

    def __delitem__(
            self,
            key: int | float | str | type | bool | tuple | frozenset
    ) -> None:
        is_key_exist = False
        cell_index = hash(key) % len(self.pairs)
        if (len(self.pairs[cell_index]) == 2
                and self.pairs[cell_index][0] == key):
            self.pairs[cell_index] = []
            is_key_exist = True
        else:
            for pair in self.pairs[cell_index + 1:] + self.pairs[:cell_index]:
                if len(pair) == 2 and pair[0] == key:
                    pair = []
                    is_key_exist = True
        if not is_key_exist:
            raise KeyError

    def get(
            self,
            key: int | float | str | type | bool | tuple | frozenset
    ) -> Any:
        return self.__getitem__(key)

    def pop(
            self,
            key: int | float | str | type | bool | tuple | frozenset
    ) -> Any:
        value = self.__getitem__(key)
        self.__delitem__(key)
        return value

    def update(self, iterable_item: dict | list | tuple) -> None:
        if isinstance(iterable_item, dict):
            for key, value in iterable_item.items():
                self.__setitem__(key, value)
        else:
            for pair in iterable_item:
                self.__setitem__(pair[0], pair[1])

    def __iter__(self) -> Dictionary:
        self.next_index = 0
        return self

    def __next__(self) -> list:
        if self.next_index == len(self.pairs):
            raise StopIteration
        pair = self.pairs[self.next_index]
        self.next_index = (self.next_index + 1)
        return pair
