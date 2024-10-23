from __future__ import annotations

from typing import Any, Hashable, Iterator


class Dictionary:

    def __init__(self) -> None:
        self.__len = 8
        self.dictionary = [None] * self.__len

    def __setitem__(self, key: Hashable, *value: Any) -> None:
        if len(value) == 1:
            value = value[0]
        key_index = hash(key) % self.__len
        is_writen = False
        for i in range(key_index, self.__len):
            if self.dictionary[i] is None or self.dictionary[i][0] == key:
                self.dictionary[i] = [key, value]
                is_writen = True
                break
        if not is_writen:
            for i in range(0, key_index):
                if self.dictionary[i] is None or self.dictionary[i][0] == key:
                    self.dictionary[i] = [key, value]
                    break

        if len(self) > int(self.__len * (2 / 3)):
            self.__resize()

    def __getitem__(self, key: Hashable) -> Any:
        key_index = hash(key) % self.__len
        for i in range(key_index, self.__len):
            if self.dictionary[i] is not None and self.dictionary[i][0] == key:
                return self.dictionary[i][1]
        for i in range(0, key_index):
            if self.dictionary[i] is not None and self.dictionary[i][0] == key:
                return self.dictionary[i][1]
        raise KeyError

    def __len__(self) -> int:
        return sum(1 for item in self.dictionary if item is not None)

    def __delitem__(self, key: Hashable) -> None:
        key_index = hash(key) % self.__len
        for i in range(key_index, self.__len):
            if self.dictionary[i] is not None and self.dictionary[i][0] == key:
                self.dictionary[i] = None
                return
        for i in range(0, key_index):
            if self.dictionary[i] is not None and self.dictionary[i][0] == key:
                self.dictionary[i] = None
                return
        raise KeyError

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

    def __resize(self) -> None:
        old_dictionary = self.dictionary
        self.__len *= 2
        self.dictionary = [None] * self.__len
        for el in old_dictionary:
            if el is not None:
                key, value = el
                self[key] = value

    def get(self, key: Hashable, *default_value: Any) -> Any:
        value = None
        value_switched = False
        if len(default_value) == 1:
            value = default_value[0]
            value_switched = True
        if len(default_value) > 1:
            raise TypeError("Expected at most two argument")
        try:
            item = self[key]
        except KeyError:
            if value_switched:
                return value
            return None
        else:
            return item

    def pop(self, key: Hashable, *default_value: Any) -> Any:
        value = None
        value_switched = False
        if len(default_value) == 1:
            value = default_value[0]
            value_switched = True
        if len(default_value) > 1:
            raise TypeError("Expected at most two argument")
        key_index = hash(key) % self.__len
        for i in range(key_index, self.__len):
            if self.dictionary[i] is not None and self.dictionary[i][0] == key:
                value = self[key]
                self.dictionary[i] = None
                return value
        for i in range(0, key_index):
            if self.dictionary[i] is not None and self.dictionary[i][0] == key:
                value = self[key]
                self.dictionary[i] = None
                return value
        if value_switched:
            return value
        raise KeyError

    def update(self, other: dict | Dictionary) -> None:
        for key in other:
            self[key] = other.get(key)

    def clear(self) -> None:
        self.dictionary = [None] * self.__len
