from __future__ import annotations
from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.loadfactor = 2 / 3
        self.size = 0
        self.hash_table = [None] * self.capacity
        self.keys = []

    def __add_hash_node(self, key: Any, value: Any) -> None:
        hash_num = hash(key)
        slot = hash_num % self.capacity
        if self.hash_table[slot] is None:
            self.hash_table[slot] = (key, hash_num, value)
        else:
            while self.hash_table[slot] is not None:
                slot = slot + 1 if slot < self.capacity - 1 else 0
            self.hash_table[slot] = (key, hash_num, value)

    def __resize_hash_table(self) -> None:
        self.hash_table += [None] * self.capacity
        self.capacity = self.capacity * 2
        for index, hash_node in enumerate(self.hash_table):
            if hash_node is not None:
                key, hash_num, value = hash_node
                self.hash_table[index] = None
                self.__add_hash_node(key, value)

    def __setitem__(self, key: Any, value: Any) -> None:
        hash_num = hash(key)
        try:
            self.__getitem__(key)
        except KeyError:
            self.size += 1
            if self.size > self.capacity * self.loadfactor:
                self.__resize_hash_table()
            self.__add_hash_node(key, value)
            self.keys.append(key)
        old_value = self.__getitem__(key)
        node_index = self.hash_table.index((key, hash_num, old_value))
        self.hash_table[node_index] = (key, hash_num, value)

    def __getitem__(self, key: Any) -> Any:
        if key in self.keys:
            hash_slot = hash(key) % self.capacity
            node = self.hash_table[hash_slot]
            if node is not None and node[0] == key:
                return node[2]
            for index, node in enumerate(self.hash_table):
                if node is not None and node[0] == key:
                    return node[2]
        raise KeyError("Key is not in a dictionary")

    def __len__(self) -> int:
        return self.size

    def __iter__(self) -> Dictionary:
        self.index = 0
        return self

    def __next__(self) -> Any:
        index = self.index
        if index >= len(self.keys):
            raise StopIteration
        self.index += 1
        return self.keys[index]

    def get(self, key: Any, value: Any = None) -> Any:
        try:
            dict_value = self.__getitem__(key)
        except KeyError:
            return value
        return dict_value

    def clear(self) -> None:
        self.capacity = 8
        self.size = 0
        self.hash_table = [None] * self.capacity
        self.keys = []
