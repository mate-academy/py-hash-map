from typing import Any


class Dictionary:
    def __init__(
        self, initial_capacity: int = 8, load_factor: float = 2 / 3
    ) -> None:
        self.initial_capacity = initial_capacity
        self.load_factor = load_factor
        self.capacity = initial_capacity
        self.size = 0
        self.buckets = [[] for _ in range(initial_capacity)]

    def __setitem__(self, key: Any, value: Any) -> None:
        bucket_index = self._get_bucket_index(key)
        bucket = self.buckets[bucket_index]

        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.size += 1

        if self.size / self.capacity > self.load_factor:
            self._resize()

    def __getitem__(self, key: Any) -> Any:
        bucket_index = self._get_bucket_index(key)
        bucket = self.buckets[bucket_index]

        for find_key, value in bucket:
            if find_key == key:
                return value

        raise KeyError(key)

    def __len__(self) -> int:
        return self.size

    def _get_bucket_index(self, key: Any) -> int:
        return hash(key) % self.capacity

    def _resize(self) -> None:
        self.capacity *= 2
        new_buckets = [[] for _ in range(self.capacity)]

        for bucket in self.buckets:
            for key, value in bucket:
                new_bucket_index = hash(key) % self.capacity
                new_buckets[new_bucket_index].append((key, value))

        self.buckets = new_buckets
