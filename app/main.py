from typing import Hashable, Any


class Dictionary:
    def __init__(self) -> None:
        self.length: int = 0
        self.hash_table: list = [None] * 8

    def __setitem__(self, key: Hashable, value: Any) -> None:
        index: int = hash(key) % len(self.hash_table)
        if self.hash_table[index] is None:
            self.hash_table[index]: list = []
        for i, (k, v) in enumerate(self.hash_table[index]):
            if k == key:
                self.hash_table[index][i] = (key, value)
                break
        else:
            self.hash_table[index].append((key, value))
            self.length += 1
            if self.length > len(self.hash_table) * 2 / 3:
                self._resize()

    def __getitem__(self, key: Hashable) -> Any:
        index: int = hash(key) % len(self.hash_table)
        if self.hash_table[index] is None:
            raise KeyError("Key not found")
        for k, v in self.hash_table[index]:
            if k == key:
                return v
        raise KeyError("Key not found")

    def __delitem__(self, key: Hashable) -> None:
        index: int = hash(key) % len(self.hash_table)
        if self.hash_table[index] is None:
            raise KeyError("Key not found")
        for i, (k, v) in enumerate(self.hash_table[index]):
            if k == key:
                del self.hash_table[index][i]
                self.length -= 1
                return
        raise KeyError("Key not found")

    def __len__(self) -> int:
        return self.length

    def clear(self) -> None:
        self.hash_table = [None] * 8
        self.length = 0

    def get(self, key: Hashable, default: Any = None) -> object:
        try:
            return self[key]
        except KeyError:
            return default

    def pop(self, key: Hashable, default: Any = None) -> object:
        try:
            value = self[key]
            del self[key]
            return value
        except KeyError:
            return default

    def update(self, other: dict) -> None:
        if isinstance(other, dict):
            other = other.items()
        for key, value in other:
            self[key] = value

    def __iter__(self) -> iter:
        for chain in self.hash_table:
            if chain is None:
                continue
            for key, value in chain:
                yield key

    def _resize(self) -> None:
        new_table: list = [None] * len(self.hash_table) * 2
        for chain in self.hash_table:
            if chain is None:
                continue
            for key, value in chain:
                index: int = hash(key) % len(new_table)
                if new_table[index] is None:
                    new_table[index]: list = []
                new_table[index].append((key, value))
        self.hash_table = new_table
