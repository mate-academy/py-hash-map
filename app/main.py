from typing import Any


class Dictionary:
    def __init__(self, capacity: int = 10) -> None:
        self.table = [[] for _ in range(capacity)]

    def _hash(self, key: str) -> int:
        return hash(key) % len(self.table)

    def __setitem__(self, key: Any, value: Any) -> None:
        index = self._hash(key)
        for kv in self.table[index]:
            if kv[0] == key:
                kv[1] = value
                return
        self.table[index].append([key, value])

    def __getitem__(self, key: Any) -> Any:
        index = self._hash(key)
        for kv in self.table[index]:
            if kv[0] == key:
                return kv[1]
        raise KeyError(f"Key {key} not found")

    def __len__(self) -> int:
        return sum(len(bucket) for bucket in self.table)
