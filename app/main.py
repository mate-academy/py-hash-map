import copy
from typing import Hashable, Any


class Node:
    def __init__(
            self,
            index: int,
            key: Hashable,
            value: Any
    ) -> None:
        self.key = key
        self.index = index
        self.value = value

    def __repr__(self) -> str:
        return (f"Node with key {self.key}, "
                f"value {self.value} at index {self.index}")


class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.hash_table: list[None | Node] = [None] * 8
        self.cur_hash_table: list = []

    def set(
            self,
            key: Hashable,
            value: Any,
            reset: bool = False
    ) -> None:
        """ Set new key/value pair to dict"""
        key_index = hash(key) % len(self.hash_table)
        while self.hash_table[key_index]:
            if self.hash_table[key_index].key == key:
                self.hash_table[key_index].value = value
                return
            key_index = (key_index + 1) % len(self.hash_table)

        self.hash_table[key_index] = Node(key_index, key, value)
        if not reset:
            self.length += 1

    def __setitem__(self, key: Hashable, value: Any) -> None:
        """Magik method for Dictionary, add new pair to Dictionary
        and controls count of cells in hash table"""
        self.set(key, value)
        if self.length > 0.66666 * len(self.hash_table):
            self.double_hash_table()

    def double_hash_table(self) -> None:
        """Increases count of cells in hash table and set
        new indexes for each key/value pair"""
        self.cur_hash_table = copy.copy(self.hash_table)
        self.hash_table = [None] * len(self.cur_hash_table) * 2
        for elem in self.cur_hash_table:
            if elem:
                self.set(elem.key, elem.value, True)
        self.cur_hash_table = []

    def find_table_index(self, key: Hashable) -> int:
        """Search key in hash table and returns its index
        in hash table"""
        hash_key = hash(key)
        key_index = hash_key % len(self.hash_table)
        counter = 0
        while True:
            if (self.hash_table[key_index]
                    and self.hash_table[key_index].key == key):
                return key_index
            key_index = (key_index + 1) % len(self.hash_table)
            counter += 1
            if counter == len(self.hash_table):
                break
        raise KeyError(f"This key `{key}` is not present here.")

    def __getitem__(self, key: Hashable) -> Any:
        """ Returns value of given key"""
        index = self.find_table_index(key)
        return self.hash_table[index].value

    def __len__(self) -> int:
        """ Returns count of records in Dictionary"""
        return self.length

    def __repr__(self) -> str:
        """String representation"""

        return f"{[node.__repr__() for node in self.hash_table if node]}"

    def __delitem__(self, key: Hashable) -> None:
        """Removes key/value pair from hash table by given key"""
        index = self.find_table_index(key)
        self.hash_table[index] = None
        self.length -= 1

    def clear(self) -> None:
        """Clear all records in Dictionary"""
        self.hash_table = [None] * 8
        self.length = 0

    def get(self, key: Hashable, default: Any = None) -> Any:
        """ Returns value of given key"""
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    def pop(self, key: Hashable) -> Any:
        """ Deletes key/value pair
        and returns value of given key"""
        index = self.find_table_index(key)
        elem = self.hash_table[index].value
        self.hash_table[index] = None
        self.length -= 1
        return elem

    def update(self, *args) -> None:
        """Reassign value of given key or
        iter through iterable to add or update key/value pairs"""
        if len(args) == 2:
            key, value = args[0], args[1]
            index = self.find_table_index(key)
            self.hash_table[index].value = value
        else:
            iterable = args[0]
            if isinstance(iterable, dict):
                for key, value in iterable.items():
                    self.__setitem__(key, value)
                return
            if hasattr(iterable, "__iter__"):
                for key, value in iterable:
                    self.__setitem__(key, value)

    def __iter__(self) -> Hashable:
        """Iter through keys in hash table"""
        for elem in self.hash_table:
            if elem:
                yield elem.key
