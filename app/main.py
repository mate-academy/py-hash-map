from typing import Any, Iterable, Optional, Hashable


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

    def __setitem__(self, key: Hashable, value: Any) -> None:
        index = self.get_index(key)
        if not self.hash_table[index]:
            self.hash_table[index] = []
        bucket = self.hash_table[index]
        for i, (keys, values) in enumerate(bucket):
            if keys == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.length += 1
        if self.length >= self.capacity * self.load_factor:
            self._resize()

    def __getitem__(self, key: Hashable) -> Any:
        index = self.get_index(key)
        bucket = self.hash_table[index]
        if bucket:
            for k, v in bucket:
                if k == key:
                    return v
        raise KeyError(f"Key {key} not in hash table")

    def __iter__(self) -> Iterable:
        for bucket in self.hash_table:
            if bucket:
                for key, _ in bucket:
                    yield key

    def clear(self) -> None:
        self.hash_table = [None] * self.capacity
        self.length = 0

    def get_index(self, key: Hashable) -> int:
        return hash(key) % self.capacity

    def _resize(self) -> None:
        self.capacity *= 2
        new_hash = [None] * self.capacity
        for bucket in self.hash_table:
            if bucket:
                for key, value in bucket:
                    index = self.get_index(key)
                    if not new_hash[index]:
                        new_hash[index] = []
                    new_hash[index].append((key, value))
        self.hash_table = new_hash

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

    def update(self, other: dict) -> None:
        for key, value in other.items():
            self[key] = value

    def __delitem__(self, key: Hashable) -> None:
        index = self.get_index(key)
        bucket = self.hash_table[index]
        try:
            del bucket[self._get_index_in_bucket(bucket, key)]
            self.length -= 1
        except KeyError:
            raise KeyError(f"Key {key} not in hash table")

    @staticmethod
    def _get_index_in_bucket(bucket: list, key: Hashable) -> int:
        for i, (keys, _) in enumerate(bucket):
            if keys == key:
                return i
        raise KeyError()
