from typing import Any, Hashable


class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.hash_table: list = [None] * 8

    def _hash(self, key: Any) -> int:
        return hash(key) % len(self.hash_table)

    def __setitem__(self, key: Hashable, value: Any) -> None:
        index = self._hash(key)

        if self.hash_table[index] is None:
            self.hash_table[index] = []

        for i, (k, v) in enumerate(self.hash_table[index]):
            if k == key:
                self.hash_table[index][i] = (key, value)
                return

        self.hash_table[index].append((key, value))
        self.length += 1

    def __getitem__(self, key: Any) -> Any:
        index = self._hash(key)
        if self.hash_table[index] is None:
            raise KeyError(f"Key {key} not found.")

        for (k, v) in self.hash_table[index]:
            if k == key:
                return v

        raise KeyError(f"Key {key} not found.")

    def __len__(self) -> int:
        return self.length
