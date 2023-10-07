from typing import Any


class Node:
    def __init__(
            self, key: Any,
            value: Any
    ) -> None:
        self.key = key
        self.hash = hash(key)
        self.value = value


class Dictionary:
    def __init__(
            self, initial_capacity: int = 10,
            load_factor: float = 0.7
    ) -> None:
        self.capacity = initial_capacity
        self.load_factor = load_factor
        self.size = 0
        self.table = [[] for _ in range(self.capacity)]

    def _resize(self) -> None:
        new_capacity = self.capacity * 2
        new_table = [[] for _ in range(new_capacity)]
        for chain in self.table:
            if chain:
                for node in chain:
                    index = node.hash % new_capacity
                    new_table[index].append(node)
                    self.table = new_table
                    self.capacity = new_capacity

    def __setitem__(
            self, key: Any,
            value: Any
    ) -> None:
        if self.size >= self.capacity * self.load_factor:
            self._resize()
        index = hash(key) % self.capacity
        if not self.table[index]:
            self.table[index] = []
        for node in self.table[index]:
            if node.key == key:
                node.value = value
                return
        self.table[index].append(Node(key, value))
        self.size += 1

    def __getitem__(
            self, key: Any
    ) -> Any:
        index = hash(key) % self.capacity
        if self.table[index]:
            for node in self.table[index]:
                if node.key == key:
                    return node.value
        raise KeyError

    def __len__(self) -> int:
        return self.size

    def __delitem__(
            self, key: Any
    ) -> None:
        index = hash(key) % self.capacity
        if self.table[index]:
            for i, node in enumerate(self.table[index]):
                if node.key == key:
                    del self.table[index][i]
                    self.size -= 1
                    return
                raise KeyError(key)

    def clear(self) -> None:
        self.table = [None] * self.capacity
        self.size = 0

    def get(
            self, key: Any,
            default: Any = None
    ) -> Any:
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    def pop(
            self, key: Any,
            default: Any = None
    ) -> Any:
        try:
            value = self.__getitem__(key)
            del self[key]
            return value
        except KeyError:
            return default

    def update(
            self, other_dict: dict
    ) -> None:
        for key, value in other_dict.items():
            self[key] = value

    def __iter__(self) -> Any:
        for index in range(self.capacity):
            if self.table[index]:
                for node in self.table[index]:
                    yield node.key
