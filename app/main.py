from __future__ import annotations
from typing import Any, Hashable


class Dictionary:
    def __init__(self) -> None:
        self.cells = [[] for i in range(8)]
        self.next_index = 0
        self.length = 0

    def __get_index__(self, key: Hashable, action: str) -> int:
        cell_index = hash(key) % len(self.cells)
        step = 0
        is_key_exist = False
        for items in self.cells[cell_index:] + self.cells[:cell_index]:
            if action == "add":
                if not items or items[0] == key:
                    break
            elif action == "get":
                if items and items[0] == key:
                    is_key_exist = True
                    break
            step += 1
        if action == "get" and not is_key_exist:
            raise KeyError(f"No such a key {key}")
        return (cell_index + step) % len(self.cells)

    def __setitem__(self, key: Hashable, value: Any) -> None:
        cell_index = self.__get_index__(key, "add")
        cell_content = self.cells[cell_index]
        if not cell_content:
            self.length += 1
        self.cells[cell_index] = [key, value]
        self.resize()

    def resize(self) -> None:
        if len(self) > len(self.cells) / 3 * 2:
            items_present = {
                items[0] : items[1] for items in self.cells if items
            }
            self.cells = [[] for i in range(len(self.cells) * 2)]
            self.length = 0
            for key, value in items_present.items():
                self.__setitem__(key, value)

    def __getitem__(self, key: Hashable) -> Any:
        return self.cells[self.__get_index__(key, "get")][1]

    def __len__(self) -> int:
        return self.length

    def clear(self) -> None:
        self.cells = [[] for i in range(8)]
        self.length = 0

    def __delitem__(self, key: Hashable, ) -> None:
        self.cells[self.__get_index__(key, "get")] = []

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
        if self.next_index == len(self.cells):
            raise StopIteration
        items = self.cells[self.next_index]
        self.next_index = (self.next_index + 1)
        return items
