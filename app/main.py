from random import randrange
from typing import Any, Hashable


class Node:
    def __init__(self, key: Hashable, value: Any) -> None:
        self.key = key
        self.value = value
        self.hash = hash(key)

    def __repr__(self) -> str:
        key_string = f"'{self.key}'" if isinstance(self.key, str) else self.key
        value_string = \
            f"'{self.value}'" if isinstance(self.value, str) else self.value
        return f"{key_string}: {value_string}"


class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.hash_table: list = [None] * 8
        self.load_factor = 2 / 3
        self.capacity = 8

    def __str__(self) -> str:
        presentation = "{"
        for el in self.hash_table:
            if el:
                presentation += f"{el}, "
        presentation = presentation.strip(", ") + "}"
        return presentation

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.__len__() >= int(self.capacity * self.load_factor):
            self.extend_hash_table()

        node = Node(key, value)
        index = node.hash % self.capacity
        if self.hash_table[index]:
            if self.hash_table[index].key == key:
                self.hash_table[index].value = node.value
                return
            else:
                for index, el in enumerate(self.hash_table):
                    if el and el.key == key:
                        self.hash_table[index].value = node.value
                        return
        while self.hash_table[index]:
            index = randrange(self.capacity)
        self.hash_table[index] = node

    def __getitem__(self, key: Hashable) -> Any:
        index = hash(key) % self.capacity
        if self.hash_table[index] and self.hash_table[index].key == key:
            return self.hash_table[index].value
        for index, el in enumerate(self.hash_table):
            if el and el.key == key:
                return self.hash_table[index].value
        raise KeyError(key)

    def __len__(self) -> int:
        self.length = len([el for el in self.hash_table if el])
        return self.length

    def extend_hash_table(self) -> None:
        self.capacity *= 2
        new_hash_table = [None] * self.capacity
        for el in self.hash_table:
            if el:
                index = el.hash % self.capacity
                if new_hash_table[index]:
                    while new_hash_table[index]:
                        index = randrange(self.capacity)
                new_hash_table[index] = el
        self.hash_table = new_hash_table
