from __future__ import annotations
from typing import Any
import math


class Node:
    def __init__(
        self, key: int | float | str | tuple | None, value: Any
    ) -> None:
        self.key = key
        self.value = value
        self.hash = hash(key)

    def __str__(self) -> str:
        return f"{self.key}: {self.value}"


class Dictionary:
    default_capacity = 8
    load_factor = 2 / 3

    def __init__(self) -> None:
        self.length = 0
        self.hash_table: list = [None] * self.default_capacity
        self.capacity = self.default_capacity

    def resize(self) -> None:
        elements = self.items()
        self.capacity = 2 * self.capacity
        self.hash_table = [None] * self.capacity
        self.length = 0
        for key, value in elements:
            self.__setitem__(key, value)

    def __setitem__(
        self, key: int | float | str | tuple | None, value: Any
    ) -> None:
        threshold = math.floor(self.load_factor * self.capacity)
        if self.length >= threshold:
            self.resize()
        new_element = Node(key, value)
        index = self.get_index(key)
        while self.hash_table[index]:
            if self.hash_table[index].key == new_element.key:
                self.length -= 1
                break
            index += 1
            index = index % self.capacity
        self.hash_table[index] = new_element
        self.length += 1

    def __getitem__(
        self, key: int | float | str | tuple | None
    ) -> Any | KeyError:
        index = self.get_index(key)
        current_element = self.hash_table[index]
        if not current_element:
            raise KeyError
        if current_element.key != key:
            for i in range(self.capacity):
                if self.hash_table[i]:
                    if self.hash_table[i].key == key:
                        return self.hash_table[i].value
            raise KeyError
        return current_element.value

    def __len__(self) -> int:
        return self.length

    def get_index(self, key: int | float | str | tuple | None) -> int:
        return hash(key) % self.capacity

    def items(self) -> list[tuple]:
        items = []
        for element in self.hash_table:
            if element:
                pair = (element.key, element.value)
                items.append(pair)
        return items

    def clear(self) -> None:
        self.__init__()

    def __delitem__(self, key: int | float | str | tuple | None) -> None:
        current_element = self.hash_table[self.get_index(key)]
        if current_element and current_element.key == key:
            self.hash_table[self.get_index(key)] = None
        for i in range(self.length):
            if self.hash_table[i] and self.hash_table[i].key == key:
                self.hash_table[i] = None

    def get(self, key: int | float | str | tuple | None) -> Any:
        current_element = self.hash_table(self.get_index(key))
        if current_element and current_element.key == key:
            return current_element.value
        for node in self.hash_table:
            if node and node.key == key:
                return node.value

    def pop(self, key: int | float | str | tuple | None) -> Any:
        current_element = self.hash_table[self.get_index(key)]
        if current_element and current_element.key == key:
            value_to_return = current_element.value
            self.hash_table[self.get_index(key)] = None
            return value_to_return
        for i in range(self.length):
            if self.hash_table[i] and self.hash_table[i].key == key:
                value_to_return = self.hash_table[i].value
                self.hash_table[i] = None
        return value_to_return

    def update(self, other: Dictionary) -> None:
        for element in other.hash_table:
            self.__setitem__(element.key, element.value)

    def __iter__(self) -> int | float | str | tuple | None:
        for element in self.hash_table:
            if element:
                yield element.key
