from typing import Any
from app.point import Point


class Dictionary:
    def __init__(self, threshold: float = 2 / 3, **kwargs) -> None:
        self.threshold = threshold
        self.hash_table = [[] for _ in range(8)]

    def __setitem__(self, key, value) -> None:
        if len(self) == round(len(self.hash_table) * self.threshold):
            self.hash_table = self._double_hash_table()

        value_updated = False
        key_hash = hash(key)
        index = key_hash % len(self.hash_table)
        if self.hash_table[index]:
            while self.hash_table[index]:
                if self.hash_table[index][1] == key:
                    self.hash_table[index][2] = value
                    value_updated = True
                    break
                if index == len(self.hash_table) - 1:
                    index = 0
                index += 1
            if not value_updated:
                self.hash_table[index].extend([key_hash, key, value])
        else:
            self.hash_table[index].extend([key_hash, key, value])

    def _double_hash_table(self) -> list:
        new_table = [[] for _ in range(len(self.hash_table) * 2)]
        for element in self.hash_table:
            if element:
                key_hash, key, value = element
                index = key_hash % len(new_table)
                if new_table[index]:
                    while new_table[index]:
                        if index == len(new_table) - 1:
                            index = 0
                        index += 1
                new_table[index].extend([key_hash, key, value])
        return new_table

    def __getitem__(self, item) -> Any:
        item_hash = hash(item)
        index = item_hash % len(self.hash_table)
        if self.hash_table[index]:
            while self.hash_table[index][1] != item:
                if index == len(self.hash_table) - 1:
                    index = 0
                index += 1
            return self.hash_table[index][2]
        raise KeyError(f"No such key '{item}' in a dictionary")

    def __len__(self) -> int:
        size = 0
        for index in self.hash_table:
            if index:
                size += 1
        return size
items = [
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
    (Point(1, 1), "A"),]

dictionary = Dictionary()
for key, value in items:
    print(f"{key=}, {value=}")
    dictionary[key] = value
    print(dictionary.hash_table)
    print(dictionary[key])
