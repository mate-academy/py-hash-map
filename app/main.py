from typing import Any


class Node:
    def __init__(self, key: str, _hash: int, value: str) -> None:
        self._key = key
        self._hash = _hash
        self._value = value

    @property
    def key(self) -> str:
        return self._key

    @key.setter
    def key(self, key: str) -> None:
        self._key = key

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, value: str) -> None:
        self._value = value

    @property
    def hash(self) -> int:
        return self._hash

    @hash.setter
    def hash(self, _hash: int) -> None:
        self._hash = _hash


class Dictionary:
    def __init__(self) -> None:
        self._length: int = 0
        self._hash_table: list[Node | None] = [None] * 8
        self._capacity: int = 8
        self._load_factor: float = 2 / 3

    def _resize(self) -> None:
        old_hash_table = self._hash_table
        self._capacity *= 2
        self._hash_table = [None] * self._capacity
        self._length = 0
        for node in old_hash_table:
            if node is not None:
                self.__setitem__(node.key, node.value)

    def __setitem__(self, key: Any, value: Any) -> None:
        index = hash(key) % self._capacity
        if self._hash_table[index] is None:
            self._hash_table[index] = Node(key, hash(key), value)
            self._length += 1
        elif self._hash_table[index].key == key:
            self._hash_table[index].value = value
        else:
            while True:
                index = (index + 1) % self._capacity
                if self._hash_table[index] is None:
                    self._hash_table[index] = Node(key, hash(key), value)
                    self._length += 1
                    break
                elif self._hash_table[index].key == key:
                    self._hash_table[index].value = value
                    break

        if (self._length / self._capacity) >= self._load_factor:
            self._resize()

    def __getitem__(self, key: str) -> str:
        index = hash(key) % self._capacity
        if self._hash_table[index] is None:
            raise KeyError
        elif self._hash_table[index].key != key:
            while True:
                index = (index + 1) % self._capacity
                if self._hash_table[index] is None:
                    raise KeyError
                elif self._hash_table[index].key == key:
                    return self._hash_table[index].value
        else:
            return self._hash_table[index].value

    def __delitem__(self, key: str) -> None:
        index = hash(key) % self._capacity
        if self._hash_table[index] is None:
            return
        elif self._hash_table[index].key != key:
            while True:
                index = (index + 1) % self._capacity
                if self._hash_table[index] is None:
                    return
                elif self._hash_table[index].key == key:
                    self._hash_table[index] = None
                    self._length -= 1
                    break
        else:
            self._hash_table[index] = None
            self._length -= 1

    def clear(self) -> None:
        self._hash_table = [None] * self._capacity
        self._length = 0

    def get(self, key: str) -> str:
        return self.__getitem__(key)

    def pop(self) -> str | None:
        if self._length == 0:
            return None
        else:
            index = self._capacity - 1
            while True:
                if self._hash_table[index] is not None:
                    self._length -= 1
                    node = self._hash_table[index]
                    self._hash_table[index] = None
                    return node.value
                else:
                    index -= 1

    def __iter__(self) -> iter:
        for node in self._hash_table:
            if node is not None:
                yield node.key

    def update(self, other: dict = None, **kwargs: str) -> None:
        """
        Update the dictionary with
        key-value pairs from `other` or keyword arguments.
        """
        if other is not None:
            if hasattr(other, "items"):
                for key, value in other.items():
                    self.__setitem__(key, value)
            else:
                for key, value in other:
                    self.__setitem__(key, value)

        for key, value in kwargs.items():
            self.__setitem__(key, value)

    def __len__(self) -> int:
        return self._length
