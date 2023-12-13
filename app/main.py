from __future__ import annotations
from typing import Any, Hashable


class Dictionary:
    def __init__(self) -> None:
        self.pairs = [[] for i in range(8)]
        self.next_index = 0
        self.length = 0

    def __setitem__(self, key: Hashable, value: Any) -> None:
        cell_index = hash(key) % len(self.pairs)
        step = 0
        for pair in self.pairs[cell_index:] + self.pairs[:cell_index]:
            if len(pair) == 0:
                self.length += 1
                break
            elif pair[0] == key:
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
            self.length = 0
            for key, value in _items_present.items():
                self.__setitem__(key, value)

    def __getitem__(self, key: Hashable) -> Any:
        cell_index = hash(key) % len(self.pairs)
        for pair in self.pairs[cell_index:] + self.pairs[:cell_index]:
            if len(pair) == 2 and pair[0] == key:
                return pair[1]
        raise KeyError

    def __len__(self) -> int:
        return self.length

    def clear(self) -> None:
        self.pairs = [[] for i in range(8)]
        self.length = 0

    def __delitem__(self, key: Hashable,) -> None:
        is_key_exist = False
        cell_index = hash(key) % len(self.pairs)
        step = 0
        for pair in self.pairs[cell_index:] + self.pairs[:cell_index]:
            if len(pair) == 2 and pair[0] == key:
                is_key_exist = True
                break
            step += 1
        if is_key_exist:
            self.pairs[(cell_index + step) % len(self.pairs)] = []
            self.length -= 1
        else:
            raise KeyError

    def get(self, key: Hashable) -> Any:
        return self.__getitem__(key)

    def pop(self, key: Hashable) -> Any:
        value = self.__getitem__(key)
        self.__delitem__(key)
        return value

    def update(self, iterable_item: dict | list | tuple) -> None:
        if isinstance(iterable_item, dict):
            iterable_item = [(key, value)
                             for key, value in iterable_item.items()]
        for key, value in iterable_item:
            self.__setitem__(key, value)

    def __iter__(self) -> Dictionary:
        self.next_index = 0
        return self

    def __next__(self) -> list:
        if self.next_index == len(self.pairs):
            raise StopIteration
        pair = self.pairs[self.next_index]
        self.next_index = (self.next_index + 1)
        return pair
