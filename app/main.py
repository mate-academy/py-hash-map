import copy
from abc import ABC

from app.point import Point


class DictionaryMember:
    def __init__(
            self,
            key: int | str | tuple | float,
            value: any,
            index: int = None
    ) -> None:
        self.key = key
        self.value = value
        self.index = index


class Dictionary:

    def __init__(
            self,
            capacity: int = 10,
            load_factor: float = 0.7
    ) -> None:

        self.size = 0
        self.capacity = capacity
        self.load_factor = load_factor
        self.table = [None] * self.capacity

    def _index(
            self,
            key: int | str | tuple | float
    ) -> int:

        index = hash(key) % self.capacity

        if (
                self.table[index] is None
                or self.table[index].key == key
        ):
            return index

        else:
            try:
                while (
                        self.table[index] is not None
                        and self.table[index].key != key
                ):
                    index += 1
                    if index > len(self.table):
                        index = 0
                return index
            except IndexError:
                index = 0
                while (
                        self.table[index] is not None
                        and self.table[index].key != key
                ):
                    index += 1
                    if index > len(self.table):
                        index = 0
            return index

    def __len__(self):
        return self.size

    def _resize(self):
        old_table = copy.deepcopy(self.table)
        self.capacity *= 2
        self.table = [None] * self.capacity
        self.size = 0

        for member in old_table:
            try:
                self.__setitem__(
                    key=member.key,
                    value=member.value)
            except AttributeError:
                pass

    def __setitem__(
            self,
            key: int | str | tuple | float,
            value: any
    ) -> None:

        key_index = self._index(key)

        if self.table[key_index] is None:
            self.table[key_index] = DictionaryMember(key=key,
                                                     value=value)
            self.size += 1
            print("Data wrote")
        else:
            self.table[key_index].value = value
            print("Data rewrote")

        if self.size / self.capacity > self.load_factor:
            self._resize()

    def __getitem__(
            self,
            key: int | str | tuple | float
    ) -> any:

        index = self._index(key)
        current = self.table[index]

        if current is None:
            raise KeyError

        else:
            return current.value

    def _clear(self) -> None:
        self.table = [None] * self.capacity
        print("All data in this dict was deleted")

    def __delitem__(
            self,
            key: int | str | tuple | float
    ) -> None:

        try:
            element = self.__getitem__(key)
        except AttributeError:
            print("This key not exist in this dictionary")
        else:
            element_index = self.table.index(element)
            self.table[element_index] = None
            print(f"Item with key {key} was destroyed")


l = [
    (8, "8"),
    (16, "16"),
    (32, "32"),
    (64, "64"),
    (128, "128"),
    ("one", 2),
    ("two", 2),
    (Point(1, 1), "a"),
    ("one", 1),
    ("one", 11),
    ("one", 111),
    ("one", 1111),
    (145, 146),
    (145, 145),
    (145, -1),
    ("two", 22),
    ("two", 222),
    ("two", 2222),
    ("two", 22222),
    (Point(1, 1), "A"),
]

my_dict = Dictionary()

for element in l:
    my_dict[element[0]] = element[1]
    print("wroted_element: ", element)
    print("dict_len: ", my_dict.__len__())
