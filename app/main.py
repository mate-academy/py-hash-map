from dataclasses import dataclass
from fractions import Fraction
from typing import Hashable, Any, Iterator, Iterable


@dataclass
class Node:
    key: Hashable
    value: Any


class Dictionary:
    def __init__(self) -> None:
        self.__iter = 0
        self.__capacity = 8
        self.__threshold = Fraction(2, 3)
        self.__table = [None] * self.__capacity
        self.__length = 0
        self.__deleted = object()

    def __setitem__(self, key: Hashable, value: Any) -> None:
        index = hash(key) % self.__capacity
        node = Node(key, value)

        if self.__table[index]:
            for _ in range(self.__capacity):

                if (self.__table[index] == self.__deleted
                        or key == self.__table[index].key):
                    self.__table[index] = node
                    return

                index += 1

                if index == self.__capacity:
                    index = 0

                if not self.__table[index]:
                    break

        if self.__length + 1 > round(self.__capacity * self.__threshold):
            self.__double_capacity()
            self[key] = value
            return

        self.__table[index] = node
        self.__length += 1

    def __getitem__(self, key: Hashable) -> Any:
        return self.__find_entry(key, False)

    def __delitem__(self, key: Hashable) -> None:
        self.__find_entry(key, True)

    def __len__(self) -> int:
        return self.__length

    def __str__(self) -> str:
        return str([
            f"Key: {node.key}, Val: {node.value}"
            for node in self.__table
            if node and node != self.__deleted
        ])

    def __iter__(self) -> Iterator:
        self.__counter = 0
        return self

    def __next__(self) -> Any:
        if self.__counter == self.__capacity:
            raise StopIteration

        if (
            self.__table[self.__counter] is None
            or self.__table[self.__counter] == self.__deleted
        ):
            self.__counter += 1
            next(self)
            return

        return self.__table[self.__counter - 1].value

    def __find_entry(self, key: Hashable, erase: bool) -> Any:
        index = hash(key) % self.__capacity

        while True:
            if not self.__table[index]:
                raise KeyError(f"no such key: {key}")
            if self.__table[index] == self.__deleted:
                continue
            if key == self.__table[index].key:
                temp = self.__table[index]
                if erase:
                    self.__counter = 0
                    self.__table[index] = self.__deleted
                return temp.value
            index += 1
            if index == self.__capacity:
                index = 0

    def pop(self, key: Hashable, default: Any = None) -> Any:
        try:
            return self.__find_entry(key, True)
        except KeyError:
            return default

    def __double_capacity(self) -> None:
        self.__counter = 0
        self.__capacity *= 2
        self.__length = 0
        old_table = self.__table
        self.__table = [None] * self.__capacity

        for node in old_table:
            if node is not None:
                self[node.key] = node.value

    def update(
            self,
            source: dict | Iterable[tuple[Hashable, Any]] = None,
            **kwargs
    ) -> None:
        if source:
            if isinstance(source, dict):
                for key, value in source.items():
                    self[key] = value
            if isinstance(source, Iterable):
                for tuple_ in source:
                    self[tuple_[0]] = tuple_[1]
        for key, value in kwargs.items():
            self[key] = value

    def clear(self) -> None:
        self.__init__()
