import math
from dataclasses import dataclass
from typing import Hashable, Any, Iterator


@dataclass
class Node:
    key: Hashable
    obj_hash: hash
    value: Any


class Dictionary:
    def __init__(self, capacity: int = 8) -> None:
        self.capacity = capacity
        self.size = 0
        self.hash_table: list[Node | None] = [None] * self.capacity

    def _calculate_index(self, key: Hashable) -> int:
        index = hash(key) % self.capacity

        while (
            self.hash_table[index]
            and self.hash_table[index].key != key
        ):
            index = (index + 1) % self.capacity

        return index

    @property
    def current_max_size(self) -> int:
        return math.floor(self.capacity * 2 / 3)

    def _resize(self) -> None:
        old_hash_table = self.hash_table

        self.__init__(self.capacity * 2)

        for node in old_hash_table:
            if node:
                self.__setitem__(node.key, node.value)

    def __setitem__(self, key: Hashable, value: Any) -> None:
        index = self._calculate_index(key)

        if self.hash_table[index] is None:
            if self.size + 1 >= self.current_max_size:
                self._resize()
                return self.__setitem__(key, value)
            self.size += 1

        self.hash_table[index] = Node(key, hash(key), value)

    def __getitem__(self, item: Any) -> Any:
        index = self._calculate_index(item)

        if self.hash_table[index] is None:
            raise KeyError(f"Cannot find object with key -> {item}")

        return self.hash_table[index].value

    def __delitem__(self, key: Hashable) -> None:
        index = self._calculate_index(key)

        if self.hash_table[index] is None:
            raise KeyError(f"Cannot find value for key: {key}")

        self.hash_table[index] = None
        self.size -= 1

    def __len__(self) -> int:
        return self.size

    def __iter__(self) -> Iterator:
        return iter(self.hash_table)

    def get(self, key: Hashable) -> Hashable | None:
        try:
            return self[key]
        except KeyError:
            print(f"Error! Value with key {key} does not exist")
        return None

    def clear(self) -> None:
        self.__init__()

    def pop(self, key: Hashable) -> Any | None:
        temp = None
        index = self._calculate_index(key)
        if self.hash_table[index]:
            temp = self.hash_table[index]
            self.hash_table[index] = None
        return temp

    def keys(self) -> list[Hashable] | None:
        keys = []
        for node_key in self.hash_table:
            keys.append(node_key.key)
        return keys if keys else None

    def values(self) -> Any:
        values = []
        for node_value in self.hash_table:
            values.append(node_value.value)
        return values if values else None

    def items(self) -> tuple[Hashable, Any] | tuple[None, None]:
        return self.keys(), self.values()

    def update(self, other: object) -> None:
        if isinstance(other, Dictionary):
            for key, value in other.items():
                self.hash_table[key] = value
        else:
            raise TypeError("Update data must be Dictionary!")
