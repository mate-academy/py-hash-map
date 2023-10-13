from typing import Any


class Dictionary:
    def __init__(
            self,
            initial_capacity: int = 16,
            load_factor: float = 0.75
    ) -> None:
        self.capacity = initial_capacity
        self.load_factor = load_factor
        self.size = 0
        self.table = [None] * initial_capacity

    def __setitem__(self, key: Any, value: Any) -> None:
        index = self._hash(key)
        if not self.table[index]:
            self.table[index] = []
        for node in self.table[index]:
            if node[0] == key:
                node[2] = value
                return
        self.table[index].append([key, self._hash(key), value])
        self.size += 1
        if self.size > self.capacity * self.load_factor:
            self._resize()

    def __getitem__(self, key: Any) -> Any:
        index = self._hash(key)
        if self.table[index]:
            for node in self.table[index]:
                if node[0] == key:
                    return node[2]
        raise KeyError(key)

    def __len__(self) -> int:
        return self.size

    def _hash(self, key: Any) -> int:
        return hash(key) % self.capacity

    def _resize(self) -> None:
        self.capacity *= 2
        new_table = [None] * self.capacity
        for bucket in self.table:
            if bucket:
                for node in bucket:
                    index = self._hash(node[0])
                    if not new_table[index]:
                        new_table[index] = []
                    new_table[index].append(node)
        self.table = new_table
