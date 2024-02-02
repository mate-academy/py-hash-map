from typing import Hashable, Any
from collections import namedtuple

HashedMap = namedtuple(
    "HashedMap", ["key", "hashed_key", "value"]
)


class Dictionary:
    def __init__(self) -> None:
        self._length = 0
        self._capacity = 8
        self._table: list[None | HashedMap] = [None] * self._capacity
        self._threshold = int(self._capacity * (2 / 3))

    def __repr__(self) -> str:
        items = [
            f"{item.key}: {item.value}"
            for item in self._table
            if item is not None
        ]
        return "{" + ", ".join(items) + "}"

    def __getitem__(self, key: Hashable) -> Any:
        index = self._get_hash_index(key)

        while (
                self._table[index] is not None
                and self._table[index].key != key
        ):
            index = (index + 1) % self._capacity

        if self._table[index] is None:
            raise KeyError(f"Key `{key}` is not found!")
        return self._table[index].value

    def __setitem__(self, key: str, value: Any) -> None:
        index = self._get_hash_index(key)

        while (
                self._table[index] is not None
                and self._table[index].key != key
        ):
            index = (index + 1) % self._capacity

        if self._table[index] is None:
            self._length += 1
            if self._length >= self._threshold:
                self.__resize()
                self[key] = value
                return

        self._table[index] = HashedMap(key, hash(key), value)

    def __len__(self) -> int:
        return self._length

    def _get_hash_index(self, key: Hashable) -> int:
        return hash(key) % self._capacity

    def __resize(self) -> None:
        self._capacity *= 2
        self._threshold = int(self._capacity * (2 / 3))
        self._length = 0

        old_table = self._table
        self._table = [None] * self._capacity

        for item in old_table:
            if item is not None:
                self[item.key] = item.value

    def get(self, key: Hashable, value: Any = None) -> Any:
        try:
            return self[key]
        except KeyError:
            return value

    def clear(self) -> None:
        self._capacity = 8
        self._table = [None] * self._capacity
        self._length = 0
