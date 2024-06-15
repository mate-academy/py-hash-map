from __future__ import annotations

from typing import Hashable, Any


class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.size = 0
        self.dictionary = [None] * self.capacity

    def hash_func(self, key: Any) -> int:
        return hash(key) % self.capacity

    def resize_dict(self) -> None:
        self.capacity = self.capacity * 2
        temp_list = self.dictionary[:]
        self.dictionary = [None] * self.capacity
        self.size = 0
        for item in temp_list:
            if item:
                self.__setitem__(item[0], item[2])

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.size + 1 > self.capacity * 2 / 3:
            self.resize_dict()
        hash_for_key = self.hash_func(key)

        if (not self.dictionary[hash_for_key]
                or self.dictionary[hash_for_key] == "deleted"):
            self.dictionary[hash_for_key] = [key, hash_for_key, value]
            self.size += 1
            return
        elif self.dictionary[hash_for_key][0] == key:
            self.dictionary[hash_for_key][2] = value
            return
        else:
            temp_counter = hash_for_key
            while ((self.dictionary[temp_counter]
                    or self.dictionary[hash_for_key] == "deleted")
                   and self.dictionary[temp_counter][0] != key):
                temp_counter = (temp_counter + 1) % self.capacity

            if (not self.dictionary[temp_counter]
                    or self.dictionary[temp_counter] == "deleted"):
                self.dictionary[temp_counter] = [key, hash_for_key, value]
                self.size += 1
            else:
                self.dictionary[temp_counter][2] = value

    def __getitem__(self, item: Any) -> Any:
        hash_for_key = self.hash_func(item)
        if not self.dictionary[hash_for_key]:
            raise KeyError

        temp_counter = hash_for_key

        while ((self.dictionary[temp_counter]
                or self.dictionary[temp_counter] != "deleted")
               and self.dictionary[temp_counter][0] != item):
            temp_counter = (temp_counter + 1) % self.capacity

        if (not self.dictionary[temp_counter]
                or self.dictionary[temp_counter] == "deleted"):
            raise KeyError
        return self.dictionary[temp_counter][2]

    def __delitem__(self, key: Any) -> None:
        hash_for_key = self.hash_func(key)
        if not self.dictionary[hash_for_key]:
            raise KeyError

        temp_counter = hash_for_key
        while ((self.dictionary[temp_counter]
                or self.dictionary[temp_counter] != "deleted")
               and self.dictionary[temp_counter][0] != key):
            temp_counter = (temp_counter + 1) % self.capacity

        if not self.dictionary[temp_counter]:
            raise KeyError

        self.dictionary[temp_counter] = "deleted"

    def __iter__(self) -> DictIterator:
        return DictIterator(self.dictionary, self.capacity)

    def clear(self) -> None:
        self.capacity = 8
        self.size = 0
        self.dictionary = [None] * self.capacity

    def __len__(self) -> int:
        return self.size


class DictIterator:
    def __init__(self, dictionary: list, size: int) -> None:
        self.dictionary = dictionary
        self._size = size
        self._index = 0

    def __iter__(self) -> DictIterator:
        return self

    def __next__(self) -> Any:
        while self._index < self._size:
            value = self.dictionary[self._index]
            self._index += 1
            if value and value != "deleted":
                return value[0]

        raise StopIteration
