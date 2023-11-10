from typing import Any


class Dictionary:

    def __init__(
            self,
            initial_size: int = 8,
            load_factor: float = 0.7
    ) -> None:
        self._initial_size = initial_size
        self._load_factor = load_factor
        self._array_buckets = [[] for _ in range(initial_size)]
        # self._length =

    def _get_hash_code(self, key: int | float | str) -> int:
        return hash(key) % self._initial_size

    def add_data(self, key: int | float | str, value: Any) -> None:
        hash_code = self._get_hash_code(key)
        bucket = self._array_buckets[hash_code]
        for i, (key_, _) in enumerate(bucket):
            if key_ == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get_data(self, key: int | float | str) -> Any:
        hash_code = self._get_hash_code(key)
        bucket = self._array_buckets[hash_code]
        for key_, value_ in bucket:
            if key_ == key:
                return value_
        raise KeyError(f"Key {key} not found")

    def __setitem__(self, key: int | float | str, value: Any) -> None:
        self.add_data(key, value)

    def __getitem__(self, key: int | float | str) -> Any:
        return self.get_data(key)

    def __repr__(self) -> str:
        return (
            "".join("".join(str(item) + ", " for item in bucket) for bucket in
                    self._array_buckets)
        )

    def __len__(self) -> int:
        return sum(len(bucket) for bucket in self._array_buckets)
