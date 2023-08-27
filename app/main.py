from typing import Any


class Node:
    def __init__(self, key: str, _hash: int, value: str) -> None:
        self.key = key
        self.hash = _hash
        self.value = value


class Dictionary:
    def __init__(
        self, initial_capacity: int = 8, load_factor: float = 2 / 3
    ) -> None:
        self._length = 0
        self._capacity = initial_capacity
        self._load_factor = load_factor
        self._hash_table = [None] * self._capacity

    def _resize(self) -> None:
        old_hash_table = self._hash_table
        self._capacity *= 2
        self._hash_table = [None] * self._capacity
        self._length = 0
        for node in old_hash_table:
            if node is not None:
                self._set_node(node)

    def _set_node(self, node: Node) -> None:
        index = node.hash % self._capacity
        while (
            self._hash_table[index] is not None
            and self._hash_table[index].key != node.key
        ):
            index = (index + 1) % self._capacity
        if self._hash_table[index] is None:
            self._length += 1
        self._hash_table[index] = node

    def __setitem__(self, key: Any, value: Any) -> None:
        node = Node(key, hash(key), value)
        if (self._length / self._capacity) >= self._load_factor:
            self._resize()
        self._set_node(node)

    def _find_index(self, key: str) -> int:
        index = hash(key) % self._capacity
        while (
            self._hash_table[index] is not None
            and self._hash_table[index].key != key
        ):
            index = (index + 1) % self._capacity
        return index

    def __getitem__(self, key: str) -> str:
        index = self._find_index(key)
        if self._hash_table[index] is None:
            raise KeyError
        return self._hash_table[index].value

    def __delitem__(self, key: str) -> None:
        index = self._find_index(key)
        if self._hash_table[index] is not None:
            self._hash_table[index] = None
            self._length -= 1

    def clear(self) -> None:
        self._hash_table = [None] * self._capacity
        self._length = 0

    def get(self, key: str) -> str:
        return self.__getitem__(key)

    def pop(self) -> str | None:
        if self._length == 0:
            return None
        index = self._capacity - 1
        while self._hash_table[index] is None:
            index -= 1
        self._length -= 1
        node = self._hash_table[index]
        self._hash_table[index] = None
        return node.value

    def __iter__(self) -> iter:
        for node in self._hash_table:
            if node is not None:
                yield node.key

    def update(self, other: dict = None, **kwargs: str) -> None:
        if other is not None:
            items = other.items() if hasattr(other, "items") else other
            for key, value in items:
                self.__setitem__(key, value)
        for key, value in kwargs.items():
            self.__setitem__(key, value)

    def __len__(self) -> int:
        return self._length
