from typing import Any, Hashable


class Node:
    def __init__(self, key: Hashable, hash_key: int, value: Any) -> None:
        self.key = key
        self.hash_key = hash_key
        self.value = value


class Dictionary:
    def __init__(
            self,
            initial_capacity: int = 8,
            load_factor: float = 0.75
    ) -> None:
        self._capacity = initial_capacity
        self._load_factor = load_factor
        self._size = 0
        self._buckets = [[] for _ in range(self._capacity)]

    def _get_index(self, key: Hashable) -> int:
        return hash(key) % self._capacity

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self._size / self._capacity >= self._load_factor:
            self._resize()
        index = self._get_index(key)
        for node in self._buckets[index]:
            if node.key == key:
                node.value = value
                return
        self._buckets[index].append(Node(key, hash(key), value))
        self._size += 1

    def __getitem__(self, key: Hashable) -> Any:
        index = self._get_index(key)
        for node in self._buckets[index]:
            if node.key == key:
                return node.value
        raise KeyError(f"KeyError: '{key}' not found in Dictionary")

    def __len__(self) -> int:
        return self._size

    def _resize(self) -> None:
        new_capacity = self._capacity * 2
        new_buckets = [[] for _ in range(new_capacity)]
        for bucket in self._buckets:
            for node in bucket:
                index = node.hash_key % new_capacity
                new_buckets[index].append(node)
        self._buckets = new_buckets
        self._capacity = new_capacity

    def clear(self) -> None:
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0

    def __delitem__(self, key: Hashable) -> None:
        index = self._get_index(key)
        for i, node in enumerate(self._buckets[index]):
            if node.key == key:
                del self._buckets[index][i]
                self._size -= 1
                return
        raise KeyError(f"KeyError: '{key}' not found in Dictionary")

    def get(self, key: Hashable, default: Any = None) -> Any:
        try:
            return self[key]
        except KeyError:
            return default

    def pop(self, key: Hashable, default: Any = None) -> Any:
        index = self._get_index(key)
        for i, node in enumerate(self._buckets[index]):
            if node.key == key:
                value = node.value
                del self._buckets[index][i]
                self._size -= 1
                return value
        if default is not None:
            return default
        raise KeyError(f"KeyError: '{key}' not found in Dictionary")

    def update(self, other: dict) -> None:
        if other is None:
            return
        for key, value in other.items():
            self[key] = value

    def __iter__(self) -> Any:
        for bucket in self._buckets:
            for node in bucket:
                yield node.key
