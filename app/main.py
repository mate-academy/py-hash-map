# from __future__ import annotations
# import pickle
# import struct
from typing import Tuple, Any, Iterable, Union

# import mmh3


class Dictionary:
    def __init__(self,
                 initial_capacity: int = 8,
                 load_factor: float = 0.75) -> None:
        self.table: list[list[Tuple[Any, Any]]] = \
            [[] for _ in range(initial_capacity)]
        self.size: int = 0
        self.load_factor = load_factor
        self.capacity = initial_capacity

    def _hash(self, key: Any) -> int:
        return hash(key) % self.capacity

    # def _hash_murmur(self, key: Any) -> int:
    #     return mmh3.hash(self._key_to_bytes(key)) % self.capacity
    #
    # def _hash_fnv1a(self, key: Any) -> int:
    #     key_bytes = self._key_to_bytes(key)
    #     hash_value = 14695981039346656037
    #     fnv_prime = 1099511628211
    #
    #     for byte in key_bytes:
    #         hash_value ^= byte
    #         hash_value *= fnv_prime
    #
    #     return hash_value % self.capacity
    #
    #
    # def _key_to_bytes(self, key: Any):
    #     if isinstance(key, str):
    #         return key.encode('utf-8')
    #     elif isinstance(key, int):
    #         return key.to_bytes((key.bit_length() + 7) // 8, 'big')
    #     elif isinstance(key, float):
    #         return struct.pack('d', key)
    #     elif isinstance(key, bytes):
    #         return key
    #     else:
    #         return pickle.dumps(key)

    def __setitem__(self, key: Any, value: Any) -> None:
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.size += 1

        if self.size / self.capacity > self.load_factor:
            self._resize()

    def __getitem__(self, key: Any) -> Any:
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(f"Key '{key}' not found.")

    def __len__(self) -> int:
        return self.size

    def __delitem__(self, key: Any) -> None:
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                bucket.remove((k, v))
                self.size -= 1
                return

        raise KeyError(f"Key '{key}' not found.")

    def __iter__(self) -> Iterable[Any]:
        for bucket in self.table:
            for key in bucket:
                yield key

    def __contains__(self, key: Any) -> bool:
        index = self._hash(key)
        bucket = self.table[index]
        for k, _ in bucket:
            if k == key:
                return True
        return False

    def _resize(self) -> None:
        new_capacity = self.capacity * 2
        new_table: list[list[Tuple[Any, Any]]] = \
            [[] for _ in range(new_capacity)]

        for bucket in self.table:
            for key, value in bucket:
                index = hash(key) % new_capacity
                new_table[index].append((key, value))

        self.table = new_table
        self.capacity = new_capacity

    def clear(self) -> None:
        # Creating new empty list. More mem usage
        # self.table = [[] for _ in range(self.capacity)]

        # Deleting data from already created list. Less mem usage
        for i in range(self.capacity):
            self.table[i] = []
        self.size = 0

    def get(self, key: Any, default: Any = None) -> Any:
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    # More modal but more mem usage
    # def pop(self, key, default = None):
    #     try:
    #         value = self.__getitem__(key)
    #
    #         self.__delitem__(key)
    #
    #         return value
    #     except KeyError:
    #         return default

    # Alternative. Less flexible bit less mem usage
    def pop(self, key: Any) -> Any:
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                # Also can use bucket.remove((k, v))
                # but it will cause problems with collisions
                del bucket[i]
                self.size -= 1
                return v

        raise KeyError(f"Key '{key}' not found.")

    def items(self) -> Iterable[Tuple[Any, Any]]:
        for bucket in self.table:
            for key, value in bucket:
                yield key, value

    def values(self) -> Iterable[Any]:
        for bucket in self.table:
            for _, value in bucket:
                yield value

    # Iterable[Tuple] -> list, generator, iterator, any type with __iter__()
    # -> zip(['a', 'b'], [1, 2])
    def update(self,
               *args: Union["Dictionary", Iterable[Tuple[Any, Any]]],
               **kwargs: Any) -> None:
        for arg in args:
            if isinstance(arg, Dictionary):
                for key, value in arg.items():
                    self[key] = value
            elif isinstance(arg, Iterable):
                for key, value in arg:
                    self[key] = value
            else:
                raise TypeError(f"Unsupported type: {type(arg)}")

        for key, value in kwargs.items():
            self[key] = value
