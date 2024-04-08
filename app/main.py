from typing import Any, Hashable


class Dictionary(object):

    def __init__(self) -> None:
        self._capacity = 8
        self._size = 0
        self._table = [None] * self._capacity

    def __getitem__(self, key: Hashable) -> Any:
        index = self.get_index(key, hash(key))

        if not self._table[index]:
            raise KeyError(f"{key} is not found!")

        return self._table[index][2]

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self._size > self._capacity * 2 / 3:
            self._resize()

        key_hash = hash(key)
        index = self.get_index(key, key_hash)
        if not self._table[index]:
            self._size += 1

        self._table[index] = (key, key_hash, value)

    def __delitem__(self, key: Hashable) -> None:
        index = self.get_index(key)

        if self._table[index] is None:
            raise KeyError(key)

        for index, item in enumerate(self._table[index]):
            if item[0] == key:
                del self._table[index][index]
                self._size -= 1
                return
            raise KeyError(key)

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Any:
        for cell in self._table:
            if cell:
                yield cell[0]

    def get_index(self, key: Hashable, key_hash: int) -> int:
        index = key_hash % self._capacity

        while self._table[index] and self._table[index][0] != key:
            index += 1

            index %= self._capacity
        return index

    def _resize(self) -> None:
        table_copy = self._table
        self._capacity *= 2
        self._table = [None] * self._capacity
        self._size = 0
        for item in table_copy:
            if item:
                self[item[0]] = item[2]

    def clear(self) -> None:
        self._table = [None] * self._capacity
        self._size = 0

    def get(self, key: Hashable) -> Any:
        try:
            return self[key]
        except KeyError:
            return None

    def pop(self, key: Hashable) -> Any:
        try:
            value: Any = self[key]
            del self[key]
            return value
        except KeyError:
            return None

    def update(self, other_dict: dict) -> None:
        for key, value in other_dict.items():
            self[key] = value
