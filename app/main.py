from typing import Any, Iterable, Optional, Union


Immutable = Union[int, float, str, bytes, tuple]


class Dictionary:

    def __init__(
            self,
            capacity: int = 8,
            load_factor: float = 0.75
    ) -> None:
        self.length: int = 0
        self.capacity: int = capacity
        self.load_factor: float = load_factor
        self.hash_table: list = [None] * capacity

    def __len__(self) -> int:
        return self.length

    def __setitem__(self, key: Immutable, value: Any) -> None:
        index = self._hash(key)
        if not self.hash_table[index]:
            self.hash_table[index] = []
        bucket = self.hash_table[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.length += 1
        if self.length >= self.capacity * self.load_factor:
            self._resize()

    def __getitem__(self, key: Immutable) -> Any:
        index = self._hash(key)
        bucket = self.hash_table[index]
        if bucket:
            for k, v in bucket:
                if k == key:
                    return v
        raise KeyError(f"Key {key} not in hash table")

    def __delitem__(self, key: Immutable) -> None:
        index = self._hash(key)
        bucket = self.hash_table[index]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.length -= 1
                return
        raise KeyError(f"Key {key} not in hash table")

    def __iter__(self) -> Iterable:
        for bucket in self.hash_table:
            if bucket:
                for key, _ in bucket:
                    yield key

    def clear(self) -> None:
        self.hash_table = [None] * self.capacity
        self.length = 0

    def _hash(self, key: Immutable) -> int:
        return hash(key) % self.capacity

    def _resize(self) -> None:
        self.capacity *= 2
        new_hash = [None] * self.capacity
        for bucket in self.hash_table:
            if bucket:
                for key, value in bucket:
                    index = self._hash(key)
                    if not new_hash[index]:
                        new_hash[index] = []
                    new_hash[index].append((key, value))
        self.hash_table = new_hash

    def get(self, key: Immutable, default: Optional[Any] = None) -> Any:
        try:
            return self[key]
        except KeyError:
            return default

    def pop(self, key: Immutable, default: Optional[Any] = None) -> Any:
        try:
            value = self[key]
            del self[key]
            return value
        except KeyError:
            return default

    def update(self, other: dict) -> None:
        for key, value in other.items():
            self[key] = value
