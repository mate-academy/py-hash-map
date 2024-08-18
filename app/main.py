from __future__ import annotations
from fractions import Fraction
from dataclasses import dataclass
from typing import Any, Iterable, Hashable


_not_provided = object()


class Dictionary:
    DEFAULT_SIZE = 8
    THRESHOLD = Fraction(2, 3)

    @dataclass
    class Node:
        hash_: int
        key: Hashable
        value: Any

    class DictionaryIterator:
        def __init__(self, dict_: Dictionary) -> None:
            self.dict = dict_
            self.index = 0

        def __iter__(self):
            return self

        def __next__(self) -> Any:
            hash_table_len = len(self.dict.hash_table)
            while (
                self.index < hash_table_len
                and self.dict.hash_table[self.index] is None
            ):
                self.index += 1
            if self.index >= hash_table_len:
                raise StopIteration

            key = self.dict.hash_table[self.index].key
            self.index += 1
            return key

    def __init__(self, items: Iterable = (), **kwargs) -> None:
        self.length = 0
        self.hash_table: list[self.__class__.Node | None] = [
            None
        ] * self.DEFAULT_SIZE

        for key, value in items:
            self[key] = value
        self.update(kwargs)

    def __getitem__(self, key: Hashable) -> Any:
        node = self._get_with_hash(key, hash(key))
        return node.value

    def __setitem__(self, key: Hashable, value: Any) -> None:
        key_hash = hash(key)

        if self.length + 1 > len(self.hash_table) * self.THRESHOLD:
            self._resize()

        self._set_with_hash(key, key_hash, value)

    def __delitem__(self, key: Hashable) -> None:
        self[key]
        self.hash_table[self._get_index(key)] = None
        self.length -= 1

    def _resize(self) -> None:
        old_hash_table = self.hash_table

        self.length = 0
        self.hash_table = [None] * len(old_hash_table) * 2

        for node in filter(None, old_hash_table):
            self._set_with_hash(node.key, node.hash_, node.value)

    def _get_with_hash(self, key: Hashable, hash_: int) -> int:
        index = self._get_index(key)
        node = self.hash_table[index]
        if node is None:
            raise KeyError(key)
        return node

    def _get_index(self, key: Hashable) -> int:
        hash_table_len = len(self.hash_table)
        index = hash(key) % hash_table_len

        while (
            self.hash_table[index] is not None
            and self.hash_table[index].key != key
        ):
            index = (index + 1) % hash_table_len

        return index

    def _set_with_hash(self, key: Hashable, hash_: int, value: Any) -> None:
        index = self._get_index(key)

        if self.hash_table[index] is None:
            self.length += 1
            self.hash_table[index] = self.__class__.Node(hash_, key, value)
        else:
            self.hash_table[index] = self.__class__.Node(
                hash_, self.hash_table[index].key, value
            )

    def __len__(self) -> int:
        return self.length

    def __iter__(self) -> DictionaryIterator:
        return self.__class__.DictionaryIterator(self)

    def clear(self) -> None:
        self.__init__()

    def items(self) -> Iterable[tuple[Hashable, Any]]:
        for node in self.hash_table:
            if not node:
                continue
            yield node.key, node.value

    def update(self, other: dict | Dictionary) -> None:
        for key, value in other.items():
            self[key] = value

    def get(self, key: Hashable, default: Any | None = None) -> Any:
        try:
            return self[key]
        except KeyError:
            return default

    def pop(self, key: Hashable, default: Any | None = _not_provided) -> Any:
        try:
            value = self[key]
        except KeyError:
            if default is _not_provided:
                raise
            return default
        del self[key]
        return value
