from __future__ import annotations
from typing import Any, Hashable

INITIAL_CAPACITY = 8
LOAD_FACTOR = 2 / 3
RESIZE_FACTOR = 2


class Node:
    def __init__(self, key: Hashable, value: Any) -> None:
        self.key = key
        self.value = value
        self.hash_key = hash(key)


class Dictionary:

    def __init__(self, **kwargs: Any) -> None:
        self.length = 0
        self.dict_keys: list = []
        self.dict_values: list = []
        self.capacity: int = INITIAL_CAPACITY
        self.hash_table: list = [None] * self.capacity
        for key, value in kwargs.items():
            self.__setitem__(key, value)

    def __str__(self) -> str:
        result_str = "{"

        for i in range(len(self.hash_table)):

            if self.hash_table[i] is not None:
                result_str += (f"'{self.hash_table[i].key}': "
                               f"{self.hash_table[i].value}, ")

        return f"{result_str}"[:-2] + "}"

    def __setitem__(self, key: Hashable, value: Any) -> None:
        node = Node(key, value)
        index = node.hash_key % self.capacity

        if (index == len(self.hash_table)
                and self.hash_table[index] is not None
                and self.hash_table[index].key != key):
            index = 0

        while (self.hash_table[index] is not None
               and self.hash_table[index].key != key):
            index = (index + 1) % self.capacity

        if self.hash_table[index] is None:
            self.length += 1

        self.hash_table[index] = node

        if self.length / self.capacity >= LOAD_FACTOR:
            self._resize()

    def __getitem__(self, key: Hashable) -> Any:
        key_hash = hash(key)
        index = key_hash % self.capacity

        while (self.hash_table[index] is not None
               and self.hash_table[index].key != key):
            index = (index + 1) % self.capacity

        if self.hash_table[index] is None:
            raise KeyError(key)

        return self.hash_table[index].value

    def __len__(self) -> int:
        return self.length

    def __delitem__(self, key: Hashable) -> None:
        for i in range(self.length):
            if (self.hash_table[i] is not None
                    and self.hash_table[i].key == key):
                self.hash_table[i] = None

    def keys(self) -> Any:
        for i in range(len(self.hash_table)):
            if self.hash_table[i] is not None:
                self.dict_keys.append(self.hash_table[i].key)
        return self.dict_keys

    def values(self) -> Any:
        for i in range(len(self.hash_table)):
            if self.hash_table[i] is not None:
                self.dict_values.append(self.hash_table[i].value)
        return self.dict_values

    def items(self) -> list:
        return [(self.hash_table[i].key, self.hash_table[i].value) for i in
                range(len(self.hash_table)) if self.hash_table[i] is not None]

    def clear(self) -> None:
        self.hash_table = []
        self.dict_keys = []
        self.dict_values = []
        self.length = 0

    def get(self, key: Hashable) -> Any:
        return self.__getitem__(key)

    def pop(self, _key: Any) -> Any:
        for i in range(len(self.hash_table)):

            if (self.hash_table[i] is not None
                    and self.hash_table[i].key == _key):
                return self.hash_table[i].value

    def update(self, new_dict: Dictionary) -> Dictionary:
        for key, value in new_dict.items():
            for i in range(len(self.hash_table)):

                if (self.hash_table[i] is not None
                        and self.hash_table[i].key == key):
                    self.hash_table[i].value = value

                if (self.hash_table[i] is not None
                        and self.hash_table[i].key != key):
                    self.__setitem__(key, value)

        return self

    def __iter__(self) -> Any:
        for i in range(len(self.hash_table)):
            if self.hash_table[i] is not None:
                yield self.hash_table[i]

    def _resize(self) -> None:
        self.capacity *= RESIZE_FACTOR
        new_table = [None] * self.capacity

        for node in self.hash_table:
            if node is not None:
                index = node.hash_key % self.capacity

                while (new_table[index] is not None
                       and new_table[index].key != node.key):
                    index = (index + 1) % self.capacity

                new_table[index] = node

        self.hash_table = new_table
