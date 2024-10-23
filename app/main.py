from typing import Any
from collections.abc import Hashable


class Dictionary:
    def __init__(self) -> None:
        self.__len = 8
        self.dictionary = [None] * self.__len

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if "__hash__" not in self.__dir__():
            raise TypeError("Unhashable key")

        key_index = hash(key) % self.__len

        is_written = False
        for i in range(key_index, self.__len):
            if self.dictionary[i] is None or self.dictionary[i][0] == key:
                self.dictionary[i] = [key, value]
                is_written = True
                break

        if not is_written:
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

    def __resize(self) -> None:
        old_dictionary = self.dictionary
        self.__len *= 2
        self.dictionary = [None] * self.__len
        for el in old_dictionary:
            if el is not None:
                key, value = el
                self[key] = value
