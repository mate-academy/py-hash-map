from typing import Any
from copy import deepcopy


class Dictionary:
    def __init__(
            self,
    ) -> None:
        self._capacity = 8
        self._load_factor = 2 / 3
        self._threshold = self._capacity * self._load_factor
        self._hash_table = [[] for _ in range(self._capacity)]
        self._size = 0

    def __setitem__(self, key: Any, value: Any) -> None:
        if self._size > self._threshold:
            self._get_resized()
        try:
            calc_hash = hash(key)
        except TypeError:
            raise TypeError
        index = calc_hash % self._capacity
        for cell in self._hash_table[index]:
            if cell[0] == key:
                self._hash_table[index].remove(cell)
                self._size -= 1
                break
        self._hash_table[index].append((key, value, calc_hash))
        self._size += 1

    def __len__(self) -> int:
        return self._size

    def __getitem__(self, key: Any) -> Any:
        try:
            index = hash(key) % self._capacity
        except TypeError:
            raise TypeError
        for cell in self._hash_table[index]:
            if cell[0] == key:
                return cell[1]
        raise KeyError

    def _get_resized(self) -> None:
        self._capacity = self._capacity * 2
        self._threshold = self._capacity * self._load_factor
        copy_table = deepcopy(self._hash_table)
        self._hash_table = [[] for i in range(self._capacity)]
        self._size = 0
        for ext_cell in copy_table:
            for key, value, _ in ext_cell:
                self.__setitem__(key, value)
