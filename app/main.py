from typing import Any
from typing import Iterator


class Dictionary:
    def __init__(self, initial_capacity: int = 8) -> None:
        self.initial_capacity = initial_capacity
        self.buckets = [[] for _ in range(initial_capacity)]
        self.keys = []
        self.values = []

    def _hash_function(self, key: Any) -> int:
        hash_key_ = hash(key)
        return hash_key_ % self.initial_capacity

    def _load_factor(self) -> float:
        return len(self) / self.initial_capacity

    def _resize(self) -> None:
        if self._load_factor() > 2 / 3:
            new_size = self.initial_capacity * 2
            new_buckets = [[] for _ in range(new_size)]

            for bucket in self.buckets:
                for key, value in bucket:
                    new_hash_key = hash(key) % new_size
                    new_buckets[new_hash_key].append((key, value))

            self.size = new_size
            self.buckets = new_buckets

    def __setitem__(self, key: int, value: str) -> None:
        self._resize()
        hash_key = self._hash_function(key)
        bucket = self.buckets[hash_key]
        for i, (existing_key, existing_value) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key, value)
        bucket.append((key, value))

        if key in self.keys:
            index = self.keys.index(key)
            self.values[index] = value
        else:
            self.keys.append(key)
            self.values.append(value)

    def __getitem__(self, key: Any) -> Any:
        if key in self.keys:
            index = self.keys.index(key)
            return self.values[index]
        else:
            raise KeyError(key)

    def __len__(self) -> int:
        return len(self.keys)

    def __list__(self) -> Any:
        data_list = []
        for bucket in self.buckets:
            data_list.extend(bucket)
        return data_list

    def clear(self) -> None:
        for bucket in self.buckets:
            bucket.clear()

    def pop(self, k: Any, d: Any = None) -> Any:
        for bucket in self.buckets:
            for i, (key, value) in enumerate(bucket):
                if key == k:
                    del bucket[i]
                    return value
        if d is not None:
            return d
        raise KeyError(k)

    def update(self, e: Any = None, **f) -> None:
        if e is not None:
            if hasattr(e, "keys"):
                for k in e.keys():
                    self[k] = e[k]
            else:
                for k, v in e:
                    self[k] = v
        for k in f:
            self[k] = f[k]

    def get(self, key: Any, default: Any = None) -> Any:
        try:
            return self[key]
        except KeyError:
            return default

    def __delitem__(self, key: Any) -> None:
        for bucket in self.buckets:
            for i, (existing_key, existing_value) in enumerate(bucket):
                if existing_key == key:
                    del bucket[i]
                    return
        raise KeyError(key)

    def __iter__(self) -> Iterator:
        return iter(self.keys)
