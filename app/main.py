from dataclasses import dataclass
from typing import Hashable, Any, Optional
from fractions import Fraction


class Dictionary:
    _INITIAL_CAPACITY = 8
    _RESIZE_THRESHOLD = Fraction(2, 3)
    _CAPACITY_MULTIPLIER = 2

    @dataclass
    class Node:
        key: Hashable
        value: Any
        hash: int

    def __init__(
            self,
            capacity: int = _INITIAL_CAPACITY
    ) -> None:
        self.capacity = capacity
        self.resize_threshold: Fraction = Dictionary._RESIZE_THRESHOLD
        self.capacity_multyplier: int = Dictionary._CAPACITY_MULTIPLIER
        self.size = 0
        self.hash_table: list[Dictionary.Node | None] = [None] * self.capacity

    def _calculate_index(self, key: Hashable, hash_value: int) -> int:
        index = hash_value % self.capacity

        while (
                self.hash_table[index] is not None
                and self.hash_table[index].key != key
        ):
            index = (index + 1) % self.capacity
        return index

    @property
    def current_max_size(self) -> int:
        return int(self.capacity * self.resize_threshold)

    def resize(self) -> None:
        old_hash_table = self.hash_table
        self.capacity *= self.capacity_multyplier
        self.size = 0
        self.hash_table = [None] * self.capacity

        for node in old_hash_table:
            if node is not None:
                self.__setitem__(node.key, node.value)

    def __setitem__(self, key: Hashable, value: Any) -> None:
        hash_value = hash(key)
        index = self._calculate_index(key, hash_value)

        if self.hash_table[index] is None:
            if self.size + 1 >= self.current_max_size:
                self.resize()
                return self.__setitem__(key, value)
            self.size += 1
        elif self.hash_table[index].key == key:
            self.hash_table[index].value = value
            return

        self.hash_table[index] = Dictionary.Node(key, value, hash_value)

    def __getitem__(self, key: Hashable) -> Any:
        hash_value = hash(key)
        index = self._calculate_index(key, hash_value)

        if self.hash_table[index] is None:
            raise KeyError(f"Cannot find value for key: {key}")

        return self.hash_table[index].value

    def __delitem__(self, key: Hashable) -> None:
        hash_value = hash(key)
        index = self._calculate_index(key, hash_value)

        if self.hash_table[index] is None:
            raise KeyError(f"Cannot find value for key: {key}")

        self.hash_table[index] = None
        self.size -= 1

    def get(self, key: Hashable, default: Optional[Any] = None) -> Any:
        try:
            return self[key]
        except KeyError:
            return default

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        return str(self.hash_table)

    def clear(self) -> None:
        self.__init__()

    def pop(self, key: Hashable, default: Optional[Any] = None) -> Any:
        try:
            value = self[key]
            del self[key]
            return value
        except KeyError:
            if default is not None:
                return default
            raise KeyError(f"Cannot find a key: {key}")
