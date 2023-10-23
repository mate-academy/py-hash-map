from typing import Any, Hashable


class Dictionary:
    def __init__(self, size: int = 8) -> None:
        self.data = size
        self.buckets = [[] for _ in range(self.data)]
        self.load_factor = 2 / 3
        self.total_count = 0

    def hash_data(self, key: Hashable) -> int:
        return hash(key) % self.data

    def __setitem__(self, key: Any, value: Any) -> None:
        key_hash = self.hash_data(key)
        for index, (exist_key, exist_value) in enumerate(self.buckets[key_hash]):
            if exist_key == key:
                self.buckets[key_hash][index] = (key, value)
                return
        self.buckets[key_hash].append((key, value))
        self.total_count += 1

    def __getitem__(self, key: Any) -> Any:
        key_hash = self.hash_data(key)
        for exist_key, exist_value in self.buckets[key_hash]:
            if exist_key == key:
                return exist_value
        raise KeyError(f"Key not found: {key}")

    def __len__(self) -> int:
        total_count = 0
        for bucket in self.buckets:
            total_count += len(bucket)
        return total_count

    def __resize__(self, new_size: int) -> None:
        new_buckets = [[] for _ in range(new_size)]

        for bucket in self.buckets:
            for key, value in bucket:
                new_index = hash(key) % new_size
                new_buckets[new_index].append((key, value))

        self.data = new_size
        self.buckets = new_buckets
