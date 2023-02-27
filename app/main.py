from __future__ import annotations
from typing import Mapping, Any, Hashable


class DictDummy:
    __slots__ = "a"
    __instances = []

    def __new__(cls, *args, **kwargs) -> DictDummy:
        if not DictDummy.__instances:
            instance = cls
            DictDummy.__instances.append(instance)
        return DictDummy.__instances[0]

    def __hash__(self) -> int:
        return hash(None) - 1


class Dictionary:
    def __init__(self, capacity: int = 8, load_factor: float = 0.75) -> None:
        self.capacity = capacity
        self.load_factor = load_factor
        self.count = 0
        self.dummy = DictDummy()
        self.table = [self.dummy] * self.capacity

    def __iter__(self) -> Any:
        for item in self.table:
            if item is not self.dummy:
                yield item[0]

    def __len__(self) -> int:
        return self.count

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.count / self.capacity >= self.load_factor:
            self._resize()

        index = self._hash(key) % self.capacity
        while (self.table[index] is not self.dummy
               and self.table[index][0]) != key:
            index = (index + 1) % self.capacity

        if self.table[index] is self.dummy:
            self.count += 1
            self.table[index] = (key, self._hash(key), value)
        else:
            self.table[index] = (key, self.table[index][1], value)

    def __getitem__(self, key: Hashable) -> Any:
        index = self._find_key(key)
        if index is None:
            raise KeyError(key)
        else:
            return self.table[index][2]

    def __delitem__(self, key: Hashable) -> None:
        index = self._find_key(key)
        if index is not None:
            self.table[index] = self.dummy
            self.count -= 1
        else:
            raise KeyError(f"{key} is not in {self}")

    def pop(self, key: object = None, default: Any = None) -> Any:
        if key is None:
            raise ValueError(
                "pop() method with `Dictionary` works only with defined key"
            )

        index = self._find_key(key)
        if index is None:
            return default
        else:
            value = self.table[index][2]
            self.table[index] = self.dummy
            self.count -= 1
            return value

    def update(self, other: Mapping[Hashable, Any]) -> None:
        for key, value in other.items():
            self[key] = value

    def _find_key(self, key: Hashable) -> int:
        index = self._hash(key) % self.capacity
        while (self.table[index] is not self.dummy
                and self.table[index][0]) != key:
            index = (index + 1) % self.capacity
        return index if self.table[index] is not self.dummy else None

    def _resize(self) -> None:
        self.capacity *= 2
        new_table = [self.dummy] * self.capacity
        for item in self.table:
            if item is not self.dummy:
                index = item[1] % self.capacity
                while (
                    new_table[index] is not self.dummy
                    and new_table[index][0] != item[0]
                ):
                    index = (index + 1) % self.capacity
                new_table[index] = item
        self.table = new_table

    def _hash(self, key: Hashable) -> int:
        return hash(key)

    def items(self) -> list:
        return [(node[0], node[2]) for node in self.table
                if node is not self.dummy]

    def clear(self) -> None:
        self.table.clear()
        self.count = 0
