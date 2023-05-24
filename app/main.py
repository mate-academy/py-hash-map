from __future__ import annotations
from typing import List, Union, Any
import traceback

from app.point import Point


class Dictionary:
    def __init__(self) -> None:
        self.load_factor = 2 / 3
        self.length = 0
        self.capacity = 8
        self.hash_table: List = [None] * self.capacity

    def __str__(self) -> str:
        return str(self.hash_table)

    def __len__(self) -> int:
        return self.length

    def __iter__(self) -> Dictionary:
        self.current_element = 0
        return self

    def __next__(self) -> Union[int, float, str, bool, tuple, Point]:
        while self.hash_table[self.current_element] is None:
            self.current_element += 1
            if self.current_element > self.capacity - 1:
                raise StopIteration
        result = self.hash_table[self.current_element][0]
        self.current_element += 1
        return result

    def __setitem__(
            self,
            key: Union[int, float, str, bool, tuple, Point],
            value: Any
    ) -> None:
        hashed_key = hash(key)
        index = hashed_key % self.capacity
        while self.hash_table[index] is not None:
            current_key, current_value = self.hash_table[index]
            if current_key == key:
                self.hash_table[index] = [current_key, value]
                return
            hashed_key += 1
            index = hashed_key % self.capacity
        self.hash_table[index] = [key, value]
        self.length += 1
        if self.length >= round(self.capacity * self.load_factor):
            self.resize()

    def __getitem__(
            self,
            item: Union[int, float, str, bool, tuple, Point]
    ) -> any:
        hashed_item = hash(item)
        index = hashed_item % self.capacity
        while self.hash_table[index] is not None:
            key, value = self.hash_table[index]
            if key == item:
                return value
            index = (index + 1) % self.capacity
        raise KeyError(f"Incorrect key {item}")

    def __delitem__(
            self,
            key: Union[int, float, str, bool, tuple, Point]
    ) -> None:
        hashed_key = hash(key)
        index = hashed_key % self.capacity
        while self.hash_table[index] is not None:
            current_key, current_value = self.hash_table[index]
            if current_key == key:
                self.hash_table[index] = ["dummy", 0]
                self.length -= 1
                return
            hashed_key += 1
            index = hashed_key % self.capacity
        raise KeyError(f"Incorrect key {key}")

    def resize(self) -> None:
        self.length = 0
        self.capacity *= 2
        temporary_list = self.hash_table
        self.hash_table = [None] * self.capacity
        for item in temporary_list:
            if item is not None:
                key, value = item
                self.__setitem__(key, value)

    def clear(self) -> None:
        self.__init__()

    def get(
            self,
            key: Union[int, float, str, bool, tuple, Point]
    ) -> Union[None, any]:
        return self.__getitem__(key)

    def pop(
            self,
            key: Union[int, float, str, bool, tuple, Point]
    ) -> Union[None, any]:
        try:
            self.length -= 1
            return [self.get(key), self.__delitem__(key)][0]
        except KeyError:
            traceback.print_exc()

    def update(self, dictionary: Dictionary) -> None:
        for item in dictionary.hash_table:
            if item is not None:
                key, value = item
                self.__setitem__(key, value)
