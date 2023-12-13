from __future__ import annotations
from typing import Hashable, Any, Iterable


class Cell:
    def __init__(self, key: Hashable, value: Any) -> None:
        self.key = key
        self.value = value
        self.key_hash = hash(self.key)


class Dictionary:
    def __init__(self) -> None:
        self._length = 0
        self._hash_table: list = [None] * 8
        self._load_factor = 2 / 3
        self._current_capacity = 8

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if not hasattr(key, "__hash__") and hasattr(key, "__eq__"):
            raise TypeError(f"Object {key} cannot be a key")
        key_hash = hash(key)
        position = key_hash % self._current_capacity
        while True:
            cell = self._hash_table[position]
            if (
                    self._hash_table[position] is None
                    or cell.key_hash == key_hash
                    and cell.key == key
            ):
                self._hash_table[position] = Cell(key, value)
                break
            position = (position + 1) % self._current_capacity
        self._length = sum(1 for cell in self._hash_table if cell)
        if self._length > self._current_capacity * self._load_factor:
            self._resize()

    def __getitem__(self, key: Hashable) -> Any:
        for cell in self._hash_table:
            if cell:
                if key == cell.key:
                    return cell.value
        raise KeyError(f"No such key {key} was found in the dictionary")

    def _resize(self) -> None:
        self._current_capacity *= 2
        temporary_hash_table = [None] * self._current_capacity
        for cell in self._hash_table:
            if not cell:
                continue
            position = cell.key_hash % self._current_capacity
            while True:
                if temporary_hash_table[position] is None:
                    temporary_hash_table[position] = cell
                    break
                position = (position + 1) % self._current_capacity
        self._hash_table = temporary_hash_table

    def __len__(self) -> int:
        return self._length

    def __delitem__(self, key: Hashable) -> None:
        for index, cell in enumerate(self._hash_table):
            if cell and cell.key == key:
                self._hash_table[index] = None
                return
        raise KeyError(f"No such key {key} was found in the dictionary")

    def clear(self) -> None:
        self._hash_table = [None] * self._current_capacity
        self._length = 0

    def get(self, key: Hashable) -> Any:
        return self[key]

    def pop(self, key: Hashable) -> Any:
        return_value = self[key]
        del self[key]
        return return_value

    def __repr__(self) -> str:
        temporary_list = []
        for cell in self._hash_table:
            if cell:
                temporary_list.append(f"{str(cell.key)}: {cell.value}")
        return ", ".join(temporary_list)

    def __iter__(self) -> Iterable:
        iterable = [
            (cell.key, cell.value)
            for cell in self._hash_table
            if cell
        ]
        return iter(iterable)

    def update(self, other_custom_dict: Dictionary) -> None:
        new_list = [cell for cell in other_custom_dict._hash_table if cell]
        for cell in new_list:
            self._hash_table[cell.key] = cell.value
