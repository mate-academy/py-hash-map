from random import randint
from typing import Any
from dataclasses import dataclass


@dataclass
class Node:
    node_key: int | float | str | tuple
    node_hash: int
    node_value: Any

    def set_value(self, value: Any) -> None:
        self.node_value = value


class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.hash_table: list = [None] * 8
        self.load_capacity = (2 / 3)
        self.capacity = 8

    def rearrange_dict(self) -> None:

        old_dict = self.hash_table
        self.capacity *= 2
        self.hash_table = [None] * self.capacity

        for node in old_dict:
            if node is not None:
                self.__setitem__(node.node_key, node.node_value)

    def __setitem__(self, key: int | float | str | tuple, value: Any) -> None:

        index = hash(key) % self.capacity

        if self.hash_table[index] is None:
            self.hash_table[index] = Node(key, hash(key), value)

        if self.check_for_presence(key):
            self.check_for_presence(key).set_value(value)

        else:
            index = self.get_random_index(index)
            self.hash_table[index] = Node(key, hash(key), value)

        self.save_space()

    def __getitem__(self, key: int | float | str | tuple) -> Any:

        if self.check_for_presence(key):
            return self.check_for_presence(key).node_value

        else:
            raise KeyError(key)

    def __len__(self) -> int:
        return len(self.hash_table) - self.hash_table.count(None)

    def check_for_presence(self,
                           key: int | float | str | tuple) -> Node | bool:

        for node in self.hash_table:

            if node is not None and node.node_key == key:
                return node

        return False

    def save_space(self) -> None:
        free_space = self.capacity - self.capacity * self.load_capacity
        if self.hash_table.count(None) <= free_space:
            self.rearrange_dict()

    def get_random_index(self, index: int) -> int:
        while self.hash_table[index] is not None:
            index = randint(0, self.capacity - 1)
        return index

    def print(self) -> None:
        print(self.hash_table)
