from typing import Any, Dict, Optional
from collections.abc import Hashable


class Dictionary:
    def __init__(self,
                 initial_capacity: int = 8,
                 load_factor: float = 0.67) -> None:
        self.initial_capacity = initial_capacity
        self.load_factor = load_factor
        self.size = 0
        self.table = [[] for _ in range(self.initial_capacity)]

    def __setitem__(self, key: Hashable, value: Any) -> None:
        hash_value = hash(key) % self.initial_capacity
        for entry in self.table[hash_value]:
            if entry[0] == key:
                entry[1] = value
                return
        self.table[hash_value].append([key, value])
        self.size += 1
        if self.size > self.initial_capacity * self.load_factor:
            self.resize()

    def __getitem__(self, key: Hashable) -> Any:
        hash_value = hash(key) % self.initial_capacity
        for entry in self.table[hash_value]:
            if entry[0] == key:
                return entry[1]
        raise KeyError

    def __len__(self) -> int:
        return self.size

    def resize(self) -> None:
        new_size = self.initial_capacity * 2
        new_table = [[] for _ in range(new_size)]
        for cell in self.table:
            for entry in cell:
                new_hash_value = hash(entry[0]) % new_size
                new_table[new_hash_value].append(entry)
            self.table = new_table
            self.initial_capacity = new_size

    def clear(self) -> None:
        self.initial_capacity = 8
        self.size = 0
        self.table = [[] for _ in range(self.size)]

    def __delitem__(self, key: Hashable) -> None:
        hash_value = hash(key) % self.size
        for i, entry in enumerate(self.table[hash_value]):
            if entry[0] == key:
                del self.table[hash_value][i]
                self.size -= 1
                return

    def get(self, key: Hashable, default: Optional[Any] = None) -> Any:
        try:
            return self[key]
        except KeyError:
            return default

    def pop(self, key: Hashable, default: Optional[Any] = None) -> Any:
        try:
            value = self[key]
            del self[key]
            return value
        except KeyError:
            return default

    def update(self, other_dict: Dict[Any, Any]) -> None:
        for key, value in other_dict.items():
            self[key] = value

    def __iter__(self) -> None:
        for bucket in self.table:
            for entry in bucket:
                yield entry[0]
