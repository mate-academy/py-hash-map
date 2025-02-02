from collections.abc import Hashable
from typing import Any

"""
number of elements = ⅔ * table size + 1
 - (same as the number of elements > ⅔ * table size);
"""


class Dictionary:
    def __init__(self, no_of_elements: int = 8) -> None:
        self.no_of_elements = no_of_elements
        self.size = 0
        self.box = [None] * self.no_of_elements

    def __delitem__(self, key: Hashable) -> None:
        index = self.index_key(key)
        if self.box[index] is None:
            raise KeyError
        self.box[index] = None
        self.size -= 1

    def __iter__(self) -> Any:
        for item in self.box:
            if item is not None:
                yield item[0]

    def __setitem__(self, key: Hashable, value: Any) -> None:
        index = self.index_key(key)
        if self.box[index] is None:
            self.size += 1
        self.box[index] = (key, value)
        if self.size >= self.no_of_elements * (2 / 3):
            self.resize()

    def __getitem__(self, key: Hashable) -> Any:
        index = self.index_key(key)
        if self.box[index] is None:
            raise KeyError
        return self.box[index][1]

    def __len__(self) -> int:
        return self.size

    def index_key(self, key: Hashable) -> int:
        index = hash(key) % self.no_of_elements
        while self.box[index] is not None:
            _key, _value = self.box[index]
            if _key == key:
                return index
            index = (index + 1) % self.no_of_elements
        return index

    def resize(self) -> None:
        # when the table is filled more than ⅔ of its size, it increases by a
        # factor of 2.
        resizing_elements = self.no_of_elements * 2
        resizing_box = [None] * resizing_elements
        for item in self.box:
            if item is not None:
                key, value = item
                index = hash(key) % resizing_elements
                while resizing_box[index] is not None:
                    index = (index + 1) % resizing_elements
                resizing_box[index] = (key, value)
        self.box = resizing_box
        self.no_of_elements = resizing_elements

    def clear(self) -> None:
        self.size = 0
        self.box = [None] * self.no_of_elements
