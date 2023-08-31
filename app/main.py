from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self._capacity = 8
        self._load_factor = 2 / 3
        self._size = 0
        self._storage = [None] * self._capacity

    def __setitem__(self, key: Any, value: Any) -> None:
        idx = hash(key) % self._capacity
        while True:
            if self._storage[idx] is None:
                self._storage[idx] = [key, hash(key), value]
                self._size += 1
                break
            if (
                key == self._storage[idx][0]
                and hash(key) == self._storage[idx][1]
            ):
                self._storage[idx][2] = value
                break
            idx = (idx + 1) % self._capacity
        if self._size >= self._capacity * self._load_factor:
            self.resize()

    def __getitem__(self, key: Any) -> None:
        idx = hash(key) % self._capacity
        end_idx = idx - 1
        while True:
            if (
                self._storage[idx] is not None
                and key == self._storage[idx][0]
                and hash(key) == self._storage[idx][1]
            ):
                return self._storage[idx][2]
            if idx == end_idx:
                raise KeyError
            idx = (idx + 1) % self._capacity

    def __delitem__(self, key: Any) -> None:
        for idx in range(self._capacity):
            if self._storage[idx] is not None and self._storage[idx][0] == key:
                self._storage[idx] = None
                break
        else:
            raise KeyError(key)

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> None:
        for item in self._storage:
            if item is not None:
                yield item[2]

    def resize(self) -> None:
        old_storage = self._storage
        self._capacity *= 2
        self._size = 0
        self.clear()
        for item in old_storage:
            if item is not None:
                self.__setitem__(item[0], item[2])

    def clear(self) -> None:
        self._storage = [None] * self._capacity

    def get(self, key: Any, default: Any = None) -> None:
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    def pop(self, key: Any) -> None:
        try:
            print(self.__getitem__(key))
            self.__delitem__(key)
        except KeyError:
            raise KeyError(key)
