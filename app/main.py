from typing import Any, Hashable


class Dictionary:

    def __init__(self) -> None:
        self._size = 8
        self._table = [None] * self._size
        self._counter = 0

    class Node:
        def __init__(self, key: Hashable, value: Any) -> None:
            self.key = key
            self.value = value
            self._hash = hash(key)

        def __str__(self) -> str:
            key_string = \
                f"'{self.key}'" if isinstance(self.key, str) \
                else self.key
            value_string = \
                f"'{self.value}'" if isinstance(self.value, str) \
                else self.value
            return f"{key_string}: {value_string}"

    def _resize(self) -> None:
        old_table = self._table
        self._size *= 2
        self._table = [None] * self._size
        self._counter = 0

        for node in old_table:
            if node:
                self[node.key] = node.value

    def _hash_to_index(self, key: Hashable) -> int:
        return hash(key) % self._size

    def __setitem__(self, key: Hashable, value: Any) -> None:

        if self._counter >= round(self._size * 2 / 3):
            self._resize()

        index = self._hash_to_index(key)

        while self._table[index] is not None:
            if self._table[index].key == key:
                self._table[index].value = value
                return
            index = (index + 1) % self._size

        self._table[index] = self.Node(key, value)
        self._counter += 1

    def __getitem__(self, key: Hashable) -> Any:
        index = self._hash_to_index(key)

        while self._table[index] is not None:
            if self._table[index].key == key:
                return self._table[index].value
            index = (index + 1) % self._size

        raise KeyError(f"Key {key} not found")

    def __len__(self) -> int:
        return self._counter

    def __str__(self) -> str:
        presentation = ", ".join(str(el) for el in self._table if el)
        return f"{{{presentation}}}"
