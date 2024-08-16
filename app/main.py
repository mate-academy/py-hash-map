from dataclasses import dataclass
from typing import Hashable, Any

CAPACITY = 8
INCREASE_KOEF = 2
TO_INCREASE = 2 / 3


@dataclass()
class Node:
    key: Hashable
    value: Any


class Dictionary:
    def __init__(self, capacity: int = CAPACITY) -> None:
        self.capacity = capacity
        self.length = 0
        self.hash_table = [None] * self.capacity

    def calculate_index(self, key: Hashable) -> int:
        index = hash(key) % self.capacity

        while (
            self.hash_table[index] is not None
            and self.hash_table[index].key != key
        ):

            index = (index + 1) % self.capacity

        return index

    def rehash(self, key: Hashable, value: Any) -> None:
        old_hash_table = self.hash_table

        self.__init__(self.capacity * 2)
        self.__setitem__(key, value)

        for obj in old_hash_table:
            if obj is not None:
                self.__setitem__(obj.key, obj.value)

    @property
    def max_size(self) -> int:
        return round(self.capacity * TO_INCREASE)

    def __setitem__(self, key: Hashable, value: Any) -> None:
        index = self.calculate_index(key)

        if self.length > self.max_size:
            return self.rehash(key, value)

        if self.hash_table[index] is None:
            self.length += 1

        self.hash_table[index] = Node(key, value)

    def __getitem__(self, key: Hashable) -> Any:
        index = self.calculate_index(key)

        if self.hash_table[index] is None:
            raise KeyError(f"Can not find element with key: '{key}'")

        return self.hash_table[index].value

    def __len__(self) -> int:
        return self.length

    def __delitem__(self, key: Hashable) -> None:
        index = self.calculate_index(key)

        if self.hash_table[index] is None:
            raise KeyError(f"No such element with key: '{key}'")

        self.hash_table[index] = None
        self.length -= 1

    def clear(self) -> None:
        self.__init__()

    def __str__(self) -> str:
        return str(self.hash_table)
