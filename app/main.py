from __future__ import annotations
from typing import NamedTuple, Any
from collections import deque


IMMUTABLE = [str, int, float, tuple]


class Pair(NamedTuple):
    key: Any
    value: Any


class Dictionary:
    def __init__(
            self,
            capacity: int = 8,
            load_factor_threshold: float = 0.6
    ) -> None:
        if capacity < 1:
            raise ValueError("Capacity must be a positive number!")
        if not (0 < load_factor_threshold <= 1):
            raise ValueError("Load factor must be a number between (0, 1)")
        self._keys = []
        self._buckets = [deque() for _ in range(capacity)]
        self._load_factor_threshold = load_factor_threshold

    def __len__(self) -> int:
        return len(self.pairs)

    def __delitem__(self, key: IMMUTABLE) -> None:
        bucket = self._buckets[self._index(key)]
        for index, pair in enumerate(bucket):
            if pair.key == key:
                del bucket[index]
                self._keys.remove(key)
                break
        else:
            raise KeyError(key)

    def __setitem__(self, key: IMMUTABLE, value: Any) -> None:
        if self.load_factor >= self._load_factor_threshold:
            self._resize_and_rehash()

        bucket = self._buckets[self._index(key)]
        for index, pair in enumerate(bucket):
            if pair.key == key:
                bucket[index] = Pair(key, value)
                break
        else:
            bucket.append(Pair(key, value))
            self._keys.append(key)

    def __getitem__(self, key: IMMUTABLE) -> Any:
        bucket = self._buckets[self._index(key)]
        for _, pair in enumerate(bucket):
            if pair.key == key:
                return pair.value
        raise KeyError(key)

    def __contains__(self, key: IMMUTABLE) -> bool:
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True

    def __iter__(self) -> Any:
        yield from self.keys

    def __str__(self) -> str:
        pairs = []
        for key, value in self.pairs:
            pairs.append(f"{key!r}: {value!r}")
        return "{" + ", ".join(pairs) + "}"

    def __repr__(self) -> str:
        print(self.__class__.__name__)
        cls = self.__class__.__name__
        return f"{cls}.from_dict({str(self)})"

    def __eq__(self, other: Dictionary) -> bool:
        if self is other:
            return True
        if type(self) is not type(other):
            return False
        return set(self.pairs) == set(other.pairs)

    def _index(self, key: IMMUTABLE) -> int:
        return hash(key) % self.capacity

    def copy(self) -> Dictionary:
        return Dictionary.from_dict(dict(self.pairs), self.capacity)

    def get(self, key: IMMUTABLE, default: Any = None) -> Any | None:
        try:
            return self[key]
        except KeyError:
            return default

    @property
    def pairs(self) -> list:
        return [(key, self[key]) for key in self.keys]

    @property
    def values(self) -> list:
        return [self[key] for key in self.keys]

    @property
    def keys(self) -> list:
        return self._keys.copy()

    @property
    def capacity(self) -> int:
        return len(self._buckets)

    @property
    def load_factor(self) -> int | float:
        return len(self) / self.capacity

    @classmethod
    def from_dict(cls, dictionary: dict, capacity: int = None) -> Dictionary:
        hash_table = cls(capacity or len(dictionary))
        for key, value in dictionary.items():
            hash_table[key] = value
        return hash_table

    def clear(self) -> None:
        self._slots = self.capacity * [None]

    def _resize_and_rehash(self) -> None:
        copy = Dictionary(capacity=self.capacity * 2)
        for key, value in self.pairs:
            copy[key] = value

        self._buckets = copy._buckets
