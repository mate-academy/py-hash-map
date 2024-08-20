from typing import Any, Hashable, Optional, List, Iterable, Union, Tuple


class Dictionary:
    class _Node:
        def __init__(self, key: Hashable, value: Any) -> None:
            self.key = key
            self.hash_key = hash(key)
            self.value = value

    def __init__(
            self,
            initial_capacity: int = 8,
            load_factor: float = 2 / 3
    ) -> None:
        self._capacity: int = initial_capacity
        self._load_factor: float = load_factor
        self._size: int = 0
        self._buckets: (
            List)[Optional[Dictionary._Node]] = [None] * self._capacity

    def _get_index(self, key: Hashable) -> int:
        return hash(key) % self._capacity

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self._size / self._capacity >= self._load_factor:
            self._resize()
        index = self._get_index(key)
        while self._buckets[index] is not None:
            if self._buckets[index].key == key:
                self._buckets[index].value = value
                return
            index = (index + 1) % self._capacity
        self._buckets[index] = self._Node(key, value)
        self._size += 1

    def __getitem__(self, key: Hashable) -> Any:
        index = self._get_index(key)
        while self._buckets[index] is not None:
            if self._buckets[index].key == key:
                return self._buckets[index].value
            index = (index + 1) % self._capacity
        raise KeyError(f'KeyError: "{key}" not found in Dictionary')

    def __len__(self) -> int:
        return self._size

    def _resize(self) -> None:
        new_capacity = self._capacity * 2
        new_buckets: List[Optional[Dictionary._Node]] = [None] * new_capacity
        for node in self._buckets:
            if node is not None:
                index = node.hash_key % new_capacity
                while new_buckets[index] is not None:
                    index = (index + 1) % new_capacity
                new_buckets[index] = node
        self._buckets = new_buckets
        self._capacity = new_capacity

    def clear(self) -> None:
        self._buckets = [None] * self._capacity
        self._size = 0

    def __delitem__(self, key: Hashable) -> None:
        index = self._get_index(key)
        while self._buckets[index] is not None:
            if self._buckets[index].key == key:
                self._buckets[index] = None
                self._size -= 1
                return
            index = (index + 1) % self._capacity
        raise KeyError(f'KeyError: "{key}" not found in Dictionary')

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
            if default is not None:
                return default
            raise

    def update(
            self,
            other: Union[dict, "Dictionary", Iterable[Tuple[Hashable, Any]]]
    ) -> None:
        if other is None:
            return
        if isinstance(other, dict) or isinstance(other, Dictionary):
            for key, value in other.items():
                self[key] = value
        else:
            for key, value in other:
                self[key] = value

    def __iter__(self) -> Iterable[Hashable]:
        for node in self._buckets:
            if node is not None:
                yield node.key
