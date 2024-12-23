from __future__ import annotations
from math import floor, log
from typing import Hashable, Any, Iterator


PairType = tuple[Hashable, Any]
BucketType = list[PairType]


class Dictionary:

    DEFAULT_CAPACITY: int = 8

    def __init__(
            self,
            capacity: int = DEFAULT_CAPACITY,
            load_factor_limit: float = 0.75
    ) -> None:
        if capacity < Dictionary.DEFAULT_CAPACITY:
            capacity = Dictionary._next_power_of_two(capacity)

        self._buckets: list[BucketType] = [[] for _ in range(capacity)]

        self._load_factor_limit = load_factor_limit

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self._load_factor() >= self._load_factor_limit:
            self._resize_and_rehash()

        bucket = self._buckets[self._index(key)]
        try:
            index, _ = self._find_pair(bucket, key)
            bucket[index] = (key, value)
        except KeyError:
            bucket.append((key, value))

    def __getitem__(self, key: Hashable) -> Any:
        bucket = self._buckets[self._index(key)]
        _, pair = self._find_pair(bucket, key)
        return pair[1]

    def __delitem__(self, key: Hashable) -> None:
        bucket = self._buckets[self._index(key)]
        index, _ = self._find_pair(bucket, key)
        del bucket[index]

    def __contains__(self, key: Hashable) -> bool:
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True

    def __len__(self) -> int:
        return len(self.items())

    def __iter__(self) -> Iterator:
        yield from self.keys()

    @classmethod
    def from_dict(cls, dictionary: dict) -> Dictionary:
        my_dictionary = cls(len(dictionary))

        for key, value in dictionary.items():
            my_dictionary[key] = value

        return my_dictionary

    def get(self, key: Hashable, default: Any = None) -> Any:
        try:
            return self[key]
        except KeyError:
            return default

    def items(self) -> list[PairType]:
        return [
            pair for bucket in self._buckets
            for pair in bucket
        ]

    def values(self) -> list[Any]:
        return [pair[1] for pair in self.items()]

    def keys(self) -> list[Hashable]:
        return [pair[0] for pair in self.items()]

    def pop(self) -> Any:
        ...

    def update(self) -> None:
        ...

    def clear(self) -> None:
        ...

    @staticmethod
    def _find_pair(bucket: BucketType, key: Hashable) -> tuple[int, PairType]:
        for index, pair in enumerate(bucket):
            if pair[0] == key:
                return index, pair
        raise KeyError(f"{key} not in dict")

    @staticmethod
    def _next_power_of_two(number: int) -> int:
        return 2 ** (floor(log(number) / log(2)) + 1)

    def _capacity(self) -> int:
        return len(self._buckets)

    def _load_factor(self) -> float:
        return len(self) / self._capacity()

    def _index(self, key: Hashable) -> int:
        return hash(key) & (self._capacity() - 1)

    def _resize_and_rehash(self) -> None:
        copy = Dictionary(capacity=self._capacity() * 2)
        for key, value in self.items():
            copy[key] = value
        self._buckets = copy._buckets
