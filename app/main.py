from dataclasses import dataclass
from typing import Hashable, Any

RESIZE_THRESHOLD = 0.7
INITIAL_CAPACITY = 8


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
    def current_max_size(self) -> float:
        return self.capacity * RESIZE_THRESHOLD

    def resize(self) -> None:
        old_hash_table = self.hash_table
        new_size = self.capacity * 2
        self.__init__(new_size)

        for node in old_hash_table:
            if node is not None:
                self.__setitem__(node.key, node.value)

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.size + 1 > self.current_max_size:
            self.resize()

        index = self._calculate_index(key)

        if self.hash_table[index] is None:
            self.hash_table[index] = Node(key, value)
            self.size += 1
        else:
            self.hash_table[index].value = value

    def __getitem__(self, key: Hashable) -> Any:
        index = self._calculate_index(key)

        if self.hash_table[index] is None:
            raise KeyError(f"Cannot find value for key {key}")
        return self.hash_table[index].value

    def __str__(self) -> str:
        return str(self.hash_table)

    def __delitem__(self, key: Hashable) -> None:
        index = self._calculate_index(key)

        if self.hash_table[index] is None:
            raise KeyError(f"Cannot find value for key {key}")

        self.hash_table[index] = None
        self.size -= 1

    def get(self, key: Hashable, default: Any = None) -> Any:
        try:
            return self[key]
        except KeyError:
            return default

    def __len__(self) -> int:
        return self.size


class PermanentHash:
    def __hash__(self) -> int:
        return 1


if __name__ == "__main__":
    my_dict = Dictionary(INITIAL_CAPACITY)
    my_dict["one"] = 1
