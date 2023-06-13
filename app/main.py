from __future__ import annotations
from copy import copy
from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.__capacity = 8
        self.clear()

    @property
    def capacity(self) -> int:
        return self.__capacity

    @property
    def data(self) -> list[list]:
        return self.__data

    def __capacity_resize(self) -> None:
        self.__capacity *= 2

    def __need_resize(self) -> bool:
        return (self.__len__() + 1) / self.capacity > 2 / 3

    def __rewrite_data(self) -> None:
        data = copy(self.data)
        self.clear()
        for cell in data:
            if cell[0]:
                self.__setitem__(cell[1], cell[2])

    def __setitem__(self, key: Any, value: Any) -> None:
        if self.__need_resize():
            self.__capacity_resize()
            self.__rewrite_data()
        key_hash = hash(key)
        cell = key_hash % self.capacity
        while True:
            if not self.data[cell][0] or (
                self.data[cell][0] == key_hash
                and self.data[cell][1] == key
            ):
                self.data[cell] = [key_hash, key, value]
                return
            cell = (cell + 1) % self.capacity

    def __getitem__(self, key: Any) -> Any:
        cell = self.__find_item(key)
        return self.data[cell][2]

    def __find_item(self, key: Any) -> int:
        key_hash = hash(key)
        cell = start = key_hash % self.capacity
        while cell != start - 1:
            if self.data[cell][1] == key:
                return cell
            cell = (cell + 1) % self.capacity
        raise KeyError("There is no such key!")

    def __len__(self) -> int:
        return len([1 for cell in self.data if cell[0]])

    def clear(self) -> None:
        self.__data = [[None, None, None] for _ in range(self.capacity)]

    def __delitem__(self, key: Any) -> None:
        cell = self.__find_item(key)
        self.data[cell] = [None, None, None]

    def get(self, key: Any, value: Any) -> Any:
        try:
            return self.__getitem__(key)
        except KeyError:
            return value

    def pop(self, key: Any) -> None:
        self.__delitem__(key)

    def update(self, another: Dictionary) -> None:
        for key, value in another:
            self.__setitem__(key, value)

    def __iter__(self) -> None:
        cells = [i for i in self.data if i[0]]
        current_element = 0
        while current_element < len(cells):
            yield cells[current_element][1], cells[current_element][2]
            current_element += 1
