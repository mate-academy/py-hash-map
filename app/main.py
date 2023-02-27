from typing import Any, Tuple


class Dictionary:
    def __init__(self, capacity: int = 16, load_factor: float = 0.75) -> None:
        self.capacity = capacity
        self.load_factor = load_factor
        self.size = 0
        self.table = [None] * self.capacity

    def __setitem__(self, key: Any, value: Any) -> None:
        index: int = self._get_index(key)
        if self.table[index] is None:
            self.table[index] = (key, hash(key), value)
            self.size += 1
            if self.size >= self.capacity * self.load_factor:
                self._resize()

        else:
            stored_key, _, current_value = self.table[index]
            if key == stored_key:
                self.table[index] = (key, hash(key), value)
            else:
                raise KeyError("Duplicate key")

    def __getitem__(self, key: Any) -> Any:
        index = self._get_index(key)
        if self.table[index] is not None:
            stored_key, _, stored_value = self.table[index]
            if key == stored_key:
                return stored_value
        raise KeyError("Key not found")

    def __len__(self) -> int:
        return self.size

    def _get_index(self, key: Any) -> int:
        return hash(key) % self.capacity

    def _resize(self) -> None:
        self.capacity *= 2
        old_table = self.table
        self.table = [None] * self.capacity
        for node in old_table:
            if node is not None:
                key, _, value = node
                self[key] = value
