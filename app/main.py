from __future__ import annotations
from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.loadfactor = 2 / 3
        self.size = 0
        self.hash_table = [None] * self.capacity
        self.keys = []

    def add_hash_node(self, key: Any, value: Any) -> None:
        hash_slot = hash(key) % self.capacity
        if self.hash_table[hash_slot] is None:
            self.hash_table[hash_slot] = (key, hash(key), value)
        else:
            for i in range(self.capacity):
                if self.hash_table[i] is None:
                    self.hash_table[i] = (key, hash(key), value)
                    break

    def resize_hash_table(self) -> None:
        self.hash_table += [None] * self.capacity
        self.capacity = self.capacity * 2
        for index, hash_node in enumerate(self.hash_table):
            if hash_node is not None:
                key, hash_num, value = hash_node
                self.hash_table[index] = None
                self.add_hash_node(key, value)

    def __setitem__(self, key: Any, value: Any) -> None:
        try:
            hash_slot = self.search_key(key)
            self.hash_table[hash_slot] = (key, hash(key), value)
        except KeyError:
            self.size += 1
            if self.size <= self.capacity * self.loadfactor:
                self.add_hash_node(key, value)
            else:
                self.resize_hash_table()
                self.add_hash_node(key, value)
            self.keys.append(key)

    def search_key(self, key: Any) -> int:
        if key in self.keys:
            hash_slot = hash(key) % self.capacity
            node = self.hash_table[hash_slot]
            if node is not None and node[0] == key:
                return hash_slot
            for index, node in enumerate(self.hash_table):
                if node is not None and node[0] == key:
                    return index
        raise KeyError("Key is not in a dictionary")

    def __getitem__(self, key: Any) -> Any:
        try:
            hash_slot = self.search_key(key)
        except KeyError:
            raise KeyError("Key is not in a dictionary")
        return self.hash_table[hash_slot][2]

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
            self.__getitem__(key)
        except KeyError:
            if value is None:
                return None
            self.__setitem__(key, value)
        return self.__getitem__(key)

    def clear(self) -> None:
        self.capacity = 8
        self.size = 0
        self.hash_table = [None] * self.capacity
        self.keys = []
