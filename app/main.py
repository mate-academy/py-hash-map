from dataclasses import dataclass
from fractions import Fraction
from typing import Hashable, Any, Iterator, Optional, Iterable


class Dictionary:
    @dataclass
    class Node:
        key: Hashable
        obj_hash: hash
        value: Any

    def __init__(self) -> None:
        self.capacity = 8
        self.size = 0
        self.hash_table: list[Dictionary.Node | None] = [None] * self.capacity

    def _calculate_index(self, key: Hashable) -> int:
        index = hash(key) % self.capacity

        while (
            self.hash_table[index]
            and self.hash_table[index].key != key
        ):
            index = (index + 1) % self.capacity

        return index

    @property
    def current_max_size(self) -> Fraction:
        return self.capacity * Fraction(2 , 3)

    def _resize(self) -> None:
        old_hash_table = self.hash_table
        self.capacity *= 2
        self.size = 0
        self.hash_table = [None] * self.capacity
        for node in old_hash_table:
            if node:
                self[node.key] = node.value

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.size > self.current_max_size:
            self._resize()
        index = self._calculate_index(key)
        if not self.hash_table[index]:
            self.size += 1
        self.hash_table[index] = Dictionary.Node(key, hash(key), value)

    def __getitem__(self, item: Any) -> Any:
        index = self._calculate_index(item)

        if self.hash_table[index] is None:
            raise KeyError(f"Cannot find object with key -> {item}")

        return self.hash_table[index].value

    def __delitem__(self, key: Hashable) -> None:
        index = self._calculate_index(key)

        if not self.hash_table[index]:
            raise KeyError(f"Cannot find value for key: {key}")

        self.hash_table[index] = None
        self.size -= 1
        if self.size <= self.current_max_size // 2:
            self.capacity //= 4
            self._resize()

    def __len__(self) -> int:
        return self.size

    def __iter__(self) -> Iterator:
        generate = iter(self.hash_table)
        yield next(generate)

    def get(self, key: Hashable) -> Hashable | None:
        try:
            return self[key]
        except KeyError:
            print(f"Error! Value with key {key} does not exist")
        return None

    def clear(self) -> None:
        self.capacity = 8
        self.size = 0
        self.hash_table: list[Dictionary.Node | None] = [None] * 8

    def pop(self, key: Hashable, default: Optional[Any]) -> Any | None:
        temp = None
        index = self._calculate_index(key)
        try:
            temp = self.hash_table[index].value
            self.hash_table[index] = None
        except KeyError as e:
            if default:
                return default
            else:
                raise KeyError(f"{e}")
        else:
            return temp

    def keys(self) -> list[Hashable] | None:
        keys = [node_key.key for node_key in self.hash_table if node_key]
        return keys if keys else None

    def values(self) -> list[Any] | None:
        values = [node_val.value for node_val in self.hash_table if node_val]
        return values if values else None

    def items(self) -> list[tuple[Hashable, Any]] | None:
        items_ = []
        for key, value in zip(self.keys(), self.values()):
            if key:
                items_.append((key, value))
        return items_ if items_ else None

    def update(self, other: Optional[Iterable]) -> None:
        if not other:
            return

        if isinstance(other, Dictionary) or type(other) is dict:
            for key, value in other.items():
                self.hash_table[key] = value
        elif all(
                type(value[0]) is Hashable
                and type(value[1]) is Any for value in other
        ):
            for i in range(len(other)):
                self.hash_table[other[i][0]] = other[i][1]
        else:
            raise TypeError("Update data must be Dictionary!")
