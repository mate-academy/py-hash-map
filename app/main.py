from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.size = 8
        self.count = 0
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key: Any) -> int:
        return hash(key) % self.size

    def _rehash(self) -> None:
        old_buckets = self.buckets
        self.size *= 2
        self.buckets = [[] for _ in range(self.size)]
        self.count = 0
        for bucket in old_buckets:
            for key, value in bucket:
                self[key] = value

    def __setitem__(self, key: Any, value: Any) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.count += 1
        if self.count / self.size > 0.75:
            self._rehash()

    def __getitem__(self, key: Any) -> Any:
        index = self._hash(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(f"Key {key} not found.")

    def __delitem__(self, key: Any) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.count -= 1
                return
        raise KeyError(f"Key {key} not found.")

    def __len__(self) -> int:
        return self.count

    def _clear(self) -> None:
        self.buckets = [[] for _ in range(self.size)]
        self.count = 0
