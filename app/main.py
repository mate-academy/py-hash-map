from __future__ import annotations

from typing import Any, Hashable, Iterator


class Dictionary:

    def __init__(self) -> None:
        self.__len = 8
        self.dictionary = [None] * self.__len

    def __setitem__(self, key: Hashable, *value: Any) -> None:
        if len(value) == 0:
            raise TypeError("expected 2 arguments, got 1")
        key_hash = hash(key)
        hash_index = self.__collision_to_write(key)
        if len(value) == 1:
            value = value[0]
        self.dictionary[hash_index] = (key, value, key_hash)

        if len(self) > int(self.__len * (2 / 3)):
            self.__resize()

    def __getitem__(self, key: Hashable) -> Any:
        hash_index = self.__collision_to_read(key)
        return self.dictionary[hash_index][1]

    def __len__(self) -> int:
        return sum(1 for item in self.dictionary if item is not None)

    def __delitem__(self, key: Hashable) -> None:
        hash_index = self.__collision_to_read(key)
        self.dictionary[hash_index] = None

    def __repr__(self) -> str:
        str_ = "{"
        for el in self:
            str_ += f"'{el}': {self.get(el)}, "
        return str_[:-2] + "}"

    def __iter__(self) -> Iterator:
        list_ = []
        for i in range(self.__len):
            if self.dictionary[i] is not None:
                list_.append(self.dictionary[i][0])
        return iter(list_)

    def get(self, key: Hashable, default_value: Any = None) -> Any:
        try:
            item = self[key]
            return item
        except KeyError:
            return default_value

    def pop(self, key: Hashable, *default_value: Any) -> Any:
        value = None
        value_switched = False
        if len(default_value) == 1:
            value = default_value[0]
            value_switched = True
        if len(default_value) > 1:
            raise TypeError("Expected at most two argument")
        try:
            hash_index = self.__collision_to_read(key)
            value = self.dictionary[hash_index]
            self.dictionary[hash_index] = None
            return value
        except KeyError:
            if value_switched:
                return value
            raise

    def update(self, other: dict | Dictionary) -> None:
        for key in other:
            self[key] = other.get(key)

    def clear(self) -> None:
        self.dictionary = [None] * self.__len

    def __collision_to_write(self, key: Hashable) -> int:
        key_hash = hash(key)
        hash_index = key_hash % self.__len
        for i in range(hash_index, self.__len):
            if (self.dictionary[i] is None
                    or self.dictionary[i][0] == key
                    and self.dictionary[i][2] == key_hash):
                return i
        for i in range(0, hash_index):
            if (self.dictionary[i] is None
                    or self.dictionary[i][0] == key
                    and self.dictionary[i][2] == key_hash):
                return i

    def __collision_to_read(self, key: Hashable) -> int:
        key_hash = hash(key)
        hash_index = key_hash % self.__len
        for i in range(hash_index, self.__len):
            if (self.dictionary[i] is not None
                    and self.dictionary[i][0] == key
                    and self.dictionary[i][2] == key_hash):
                return i
        for i in range(0, hash_index):
            if (self.dictionary[i] is not None
                    and self.dictionary[i][0] == key
                    and self.dictionary[i][2] == key_hash):
                return i
        raise KeyError

    def __resize(self) -> None:
        old_dictionary = self.dictionary
        self.__len *= 2
        self.dictionary = [None] * self.__len
        for el in old_dictionary:
            if el is not None:
                key, value = el[:2]
                self[key] = value
