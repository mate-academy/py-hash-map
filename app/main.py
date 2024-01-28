from typing import Hashable, Iterable, Iterator, Any


class Dictionary:

    def __init__(self) -> None:
        self._length = 0
        self._capacity = 8
        self._threshold = int(self._capacity * (2 / 3))
        self._hash_table = [None] * self._capacity

    def __getitem__(self, key: Hashable) -> Any:
        index = hash(key) % self._capacity
        item = self._hash_table[index]

        while item:
            if item[0] == key and item[1] == hash(key):
                return item[2]
            index = (index + 1) % self._capacity
            item = self._hash_table[index]

        raise KeyError(f"Dictionary doesn't have such key: {key}")

    def __setitem__(self, key: Hashable, value: Any) -> None:
        index = hash(key) % self._capacity
        node = (key, hash(key), value)

        while True:
            if not self._hash_table[index]:
                self._hash_table[index] = node
                self._length += 1
                break
            if (
                    self._hash_table[index][0] == key
                    and self._hash_table[index][1] == hash(key)
            ):
                self._hash_table[index] = node
                break

            index = (index + 1) % self._capacity

        if self._length > self._threshold:
            self._resize_hash_table()

    def _resize_hash_table(self) -> None:
        self._capacity *= 2
        self._threshold = int(self._capacity * (2 / 3))
        resized_table = [None] * self._capacity

        for item in self._hash_table:
            if item:
                index = item[1] % self._capacity
                if not resized_table[index]:
                    resized_table[index] = item
                else:
                    while True:
                        index = (index + 1) % self._capacity
                        if not resized_table[index]:
                            resized_table[index] = item
                            break

        self._hash_table = resized_table

    def __len__(self) -> int:
        return self._length

    def clear(self) -> None:
        self._capacity = 8
        self._hash_table = [None] * self._capacity

    def __delitem__(self, key: Hashable) -> None:
        index = hash(key) % self._capacity
        item = self._hash_table[index]

        while item and item[0] != key:
            index = (index + 1) % self._capacity
            item = self._hash_table[index]

        self._hash_table[index] = None
        self._length -= 1

    def get(self, key: Hashable, value: Any = None) -> Any:
        index = hash(key) % self._capacity
        item = self._hash_table[index]

        while item:
            if item[0] == key and item[1] == hash(key):
                return item[2]
            index = (index + 1) % self._capacity
            item = self._hash_table[index]

        return value

    def pop(self, key: Hashable, value: Any = None) -> Any:
        index = hash(key) % self._capacity
        item = self._hash_table[index]

        while item:
            if item[0] == key and item[1] == hash(key):
                value = item[2]
                self.__delitem__(key)
                return value
            index = (index + 1) % self._capacity
            item = self._hash_table[index]

        if value:
            return value
        raise KeyError(f"Dictionary doesn't have such key: {key}")

    def update(self, iterable: Iterable) -> None:
        if isinstance(iterable, dict):
            for key, value in iterable.items():
                self.__setitem__(key, value)
        else:
            try:
                for key, value in iterable:
                    self.__setitem__(key, value)
            except TypeError:
                raise TypeError(
                    "Your iterable object should contain key - value pairs"
                )

    def __iter__(self) -> Iterator:
        return iter(
            [item[0] for item in self._hash_table if item]
        )
