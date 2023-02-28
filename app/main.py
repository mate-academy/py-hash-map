from typing import Hashable, Any


class Dictionary:
    def __init__(self, capacity: int = 8, load_factor: float = 0.66) -> None:
        self.capacity = capacity
        self.load_factor = load_factor
        self.size = 0
        self.table = [None] * self.capacity

    def __len__(self) -> int:
        return self.size

    def __setitem__(self, key: Hashable, value: Any) -> None:
        index = hash(key) % self.capacity
        while self.table[index] is not None:
            if self.table[index][0] == key:
                break
            index = (index + 1) % self.capacity
        else:
            self.size += 1
            if self.size >= self.capacity * self.load_factor:
                self._resize()
        self.table[index] = (key, value)

    def __getitem__(self, key: Hashable) -> Any:
        index = hash(key) % self.capacity
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.capacity
        raise KeyError(key)

    def _resize(self) -> None:
        old_table = self.table
        self.capacity *= 2
        self.table = [None] * self.capacity
        self.size = 0
        for node in old_table:
            if node is not None:
                key, value = node
                self[key] = value
