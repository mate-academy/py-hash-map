from dataclasses import dataclass

from click import Tuple
from typing import Hashable, Any, Iterator

INITIAL_CAPACITY = 8
RESIZE_THRESHOLD = 2 / 3
CAPACITY_MULTIPLIER = 2


@dataclass
class Node:
    key: Hashable
    value: Any


class Dictionary:
    def __init__(self, capacity: int = INITIAL_CAPACITY) -> None:
        self.capacity = capacity
        self.size = 0
        self.hash_table: list[Node | None] = [None] * self.capacity

    def _calculate_index(self, key: Hashable) -> int:
        index = hash(key) % self.capacity

        while (
            self.hash_table[index] is not None
            and self.hash_table[index].key != key
        ):
            index = (index + 1) % self.capacity

        return index

    @property
    def current_max_size(self) -> int:
        return self.capacity * RESIZE_THRESHOLD

    def resize(self) -> None:
        old_hash_table = self.hash_table

        self.__init__(self.capacity * CAPACITY_MULTIPLIER)

        for node in old_hash_table:
            if node is not None:
                self.__setitem__(node.key, node.value)

    def __setitem__(self, key: Hashable, value: Any) -> None:
        index = self._calculate_index(key)

        if self.hash_table[index] is None:
            if self.size + 1 >= self.current_max_size:
                self.resize()
                return self.__setitem__(key, value)
            self.size += 1

        self.hash_table[index] = Node(key, value)

    def __getitem__(self, key: Hashable) -> Node:
        index = self._calculate_index(key)

        if self.hash_table[index] is None:
            raise KeyError(f"Cannot find value for key: {key}")

        return self.hash_table[index].value

    def __delitem__(self, key: Hashable) -> None:
        index = self._calculate_index(key)

        if self.hash_table[index] is None:
            raise KeyError(f"Cannot delete value for key: {key}")

        self.hash_table[index] = None
        self.size -= 1

    def __iter__(self) -> Iterator[tuple[Hashable, Any]]:
        for node in self.hash_table:
            if node is not None:
                yield (node.key, node.value)

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        items = [
            f"{node.key}: {node.value}"
            for node in self.hash_table
            if node is not None
        ]
        return "{" + ", ".join(items) + "}"

    def get(self, key: Hashable, default: Any = None) -> Node:
        try:
            return self[key]
        except KeyError:
            return default

    def pop(self, key: Hashable, default: Any = None) -> Node:
        value = self[key]
        self.__delitem__(key)
        return value

    def update(self, data: Node) -> None:
        self.__setitem__(data.key, data.value)
