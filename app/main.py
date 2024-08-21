from fractions import Fraction
from typing import Hashable, Any


class Node:
    def __init__(self, key: Hashable, value: Any) -> None:
        self.key = key
        self.value = value


class Dictionary:
    LOAD_FACTOR = Fraction(2, 3)

    def __init__(self, capacity: int = 8) -> None:
        self.capacity = capacity
        self.size = 0
        self.hash_table: list[Node | None] = [None] * self.capacity

    def _resize(self) -> None:
        old_hash_table = self.hash_table

        self.__init__(self.capacity * 2)

        for slot in old_hash_table:
            if slot:
                self.__setitem__(slot.key, slot.value)

    def _calculate_index(self, key: Hashable, setting: bool = True) -> int:
        index = hash(key) % self.capacity

        while True:
            if not self.hash_table[index]:
                return index if setting else -1
            if self.hash_table[index].key == key:
                return index
            index = (index + 1) % self.capacity

    def __setitem__(self, key: Hashable, value: any) -> None:
        if self.size > self.capacity * self.LOAD_FACTOR:
            self._resize()

        index = self._calculate_index(key)
        if not self.hash_table[index]:
            self.size += 1
        self.hash_table[index] = Node(key, value)

    def __getitem__(self, key: Hashable) -> any:
        index = self._calculate_index(key, False)
        if index == -1:
            raise KeyError(f"Key {key} not found")
        return self.hash_table[index].value

    def __len__(self) -> int:
        return self.size

    def clear(self) -> None:
        self.__init__(self.capacity)
