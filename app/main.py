from typing import List, Any, Optional, Tuple, Iterator


class Dictionary:
    def __init__(self,
                 initial_capacity: int = 8,
                 load_factor: float = 2 / 3) -> None:
        self.capacity: int = initial_capacity
        self.load_factor: float = load_factor
        self.size: int = 0
        self.buckets: List[List[Tuple[Any, Any, int]]] = \
            [[] for _ in range(self.capacity)]

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.size / self.capacity > self.load_factor:
            self.resize()
        index: int = self.get_index(key)
        key_hash: int = hash(key)

        for i, (k, v, h) in enumerate(self.buckets[index]):
            if k == key:
                self.buckets[index][i] = (key, value, key_hash)
                return

        self.buckets[index].append((key, value, key_hash))
        self.size += 1

    def __getitem__(self, key: Hashable) -> Any:
        index: int = self.get_index(key)
        key_hash: int = hash(key)

        for k, v, h in self.buckets[index]:
            if k == key and h == key_hash:
                return v

        raise KeyError(f"Key '{key}' not found.")

    def __len__(self) -> int:
        return self.size

    def __delitem__(self, key: Hashable) -> None:
        index: int = self.get_index(key)
        key_hash: int = hash(key)

        for i, (k, v, h) in enumerate(self.buckets[index]):
            if k == key and h == key_hash:
                del self.buckets[index][i]
                self.size -= 1
                return

        raise KeyError(f"Key '{key}' not found.")

    def __contains__(self, key: Hashable) -> bool:
        index: int = self.get_index(key)
        key_hash: int = hash(key)

        for k, v, h in self.buckets[index]:
            if k == key and h == key_hash:
                return True

        return False

    def get_index(self, key: Any) -> int:
        return hash(key) % self.capacity

    def resize(self) -> None:
        old_buckets: List[List[Tuple[Any, Any, int]]] = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0

        for bucket in old_buckets:
            for key, value, h in bucket:
                self.__setitem__(key, value)

    def clear(self) -> None:
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0

    def get(self, key: Any, default: Optional[Any] = None) -> Optional[Any]:
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    def pop(self, key: Any, default: Optional[Any] = None) -> Optional[Any]:
        try:
            value: Any = self.__getitem__(key)
            self.__delitem__(key)
            return value
        except KeyError:
            if default is not None:
                return default
            raise KeyError(f"Key '{key}' not found "
                           f"and no default value provided.")

    def update(self, other: dict) -> None:
        for key, value in other.items():
            self.__setitem__(key, value)

    def __iter__(self) -> Iterator[Any]:
        for bucket in self.buckets:
            for key, value, h in bucket:
                yield key
