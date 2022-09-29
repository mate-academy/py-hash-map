from __future__ import annotations
from typing import Hashable, Any, Generator


class KeyValuePair:
    def __init__(self, key: Hashable, value: Any) -> None:
        self._key = key
        self.value = value

    def __eq__(self, other: KeyValuePair | int):
        if isinstance(other, KeyValuePair):
            return other.key == self.key
        return other == self.key

    def __hash__(self):
        return hash(self.key)

    def __str__(self) -> str:
        return f"Key={self.key} : Value={self.value}"

    @property
    def key(self):
        return self._key


# I implement dictionary via chaining
class Dictionary:
    _INITIAL_CAPACITY = 8
    _LOAD_FACTOR = 2 / 3

    def __init__(self) -> None:
        self._hash_table = [[] for _ in range(Dictionary._INITIAL_CAPACITY)]
        self._size = 0

    def _ensure_capacity(self) -> None:
        self._size += 1
        if self._size > int(self.capacity * Dictionary._LOAD_FACTOR):
            self._resize()

    def _resize(self) -> None:
        new_hash_table = [[] for _ in range(self.capacity * 2)]
        for pair in iter(self):
            index = hash(pair) % len(new_hash_table)
            new_hash_table[index].append(pair)
        self._hash_table = new_hash_table

    def clear(self) -> None:
        self._hash_table = [[] for _ in range(Dictionary._INITIAL_CAPACITY)]
        self._size = 0

    def pop(self, key: Hashable) -> Any:
        res = self.__get__(key)
        self.__delitem__(key)
        return res

    def get(self, key: Hashable, default: Any = None) -> Any:
        try:
            return self[key]
        except KeyError:
            return default

    def __get__(self, key: Hashable) -> Any:
        ind = hash(key) % self.capacity
        for i, pair in enumerate(self._hash_table[ind]):
            if pair == key:
                return pair.value
        raise KeyError(f"Key {key} does not exist")

    def __set__(self, key: Hashable, value: Any) -> None:
        ind = hash(key) % self.capacity
        for i, pair in enumerate(self._hash_table[ind]):
            if pair == key:
                self._hash_table[ind][i].value = value
                return
        self._hash_table[ind].append(KeyValuePair(key, value))
        self._ensure_capacity()

    def __getitem__(self, item: Hashable) -> Any:
        return self.__get__(item)

    def __setitem__(self, key: Hashable, value: Any) -> None:
        self.__set__(key, value)

    def __delitem__(self, key: Hashable) -> None:
        ind = hash(key) % self.capacity
        for i, pair in enumerate(self._hash_table[ind]):
            if pair == key:
                self._hash_table[ind].pop(i)

    def __iter__(self) -> Generator:
        for bucket in self._hash_table:
            for pair in bucket:
                yield pair

    def __len__(self) -> int:
        return self._size

    @property
    def capacity(self):
        return len(self._hash_table)
