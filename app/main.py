import dataclasses
from typing import Hashable, Any


@dataclasses.dataclass
class Node:
    key: Hashable
    key_hash: int
    value: Any


class Dictionary:
    __load_factor = 2 / 3

    def __init__(self) -> None:
        self.__hashtable = [None] * 8

    def __setitem__(self, key: Hashable, value: Any) -> None:
        hashed_key = hash(key)
        node = Node(key, hashed_key, value)
        self.__choose_cell(node)
        self.__check_overload()

    def __getitem__(self, key: Hashable) -> object:
        hashed_key = hash(key)
        length = len(self.__hashtable)
        preferred_cell = hashed_key % length
        for i in range(preferred_cell, length):
            if self.__hashtable[i] and self.__hashtable[i].key == key:
                return self.__hashtable[i].value
        for i in range(0, preferred_cell):
            if self.__hashtable[i] and self.__hashtable[i].key == key:
                return self.__hashtable[i].value
        raise KeyError("Key not found")

    def __len__(self) -> int:
        return len([node for node in self.__hashtable if node is not None])

    def clear(self) -> None:
        self.__hashtable = [None] * 8

    def __delitem__(self, key: Hashable) -> None:
        hashed_key = hash(key)
        length = len(self.__hashtable)
        preferred_cell = hashed_key % length
        for i in range(preferred_cell, length):
            if self.__hashtable[i] and self.__hashtable[i].key == key:
                self.__hashtable[i] = None
                return
        for i in range(0, preferred_cell):
            if self.__hashtable[i] and self.__hashtable[i].key == key:
                self.__hashtable[i] = None
                return
        raise KeyError("Key not found")

    def get(self, key: object) -> object:
        try:
            return self.__getitem__(key)
        except KeyError:
            return -1

    def update(self, second_dict: "Dictionary") -> None:
        for node in second_dict.__dict__["_Dictionary__hashtable"]:
            if node:
                self.__setitem__(node.key, node.value)
            self.__setitem__(node.key, node.value)

    def __iter__(self) -> list:
        self.index = 0
        return self.__hashtable

    def __next__(self) -> Hashable:
        try:
            self.index += 1
            while self.__hashtable[self.index] is None:
                self.index += 1
            return self.__hashtable[self.index].key
        except IndexError:
            raise StopIteration

    def pop(self, key: Hashable, default_value: Any) -> object:
        try:
            item = self.__getitem__(key)
            self.__delitem__(key)
            return item
        except KeyError:
            if default_value is not None:
                return default_value
            raise

    def __check_overload(self) -> None:
        """
        Do not use this function, it calculates when hashtable should
        be multiplied automatically
        """
        length = len(self.__hashtable)
        if self.__len__() > length * self.__load_factor:
            self.__multiply_hashtable()

    def __multiply_hashtable(self) -> None:
        """
        Do not use this function, it multiplies hashtable
        """
        items = [node for node in self.__hashtable if node is not None]
        self.__hashtable = [None] * (len(self.__hashtable) * 2)
        for item in items:
            self.__choose_cell(item)

    def __choose_cell(self, node: "Node") -> None:
        """
        Do not use this function, it chose where to mark data
        according to its hash. We use len + cell to go to the 0
        if we are in top border
        """
        length = len(self.__hashtable)
        preferred_cell = node.key_hash % length
        for i in range(preferred_cell, length + preferred_cell):
            if i >= len(self.__hashtable):
                i -= length
            if self.__hashtable[i] and self.__hashtable[i].key == node.key:
                self.__hashtable[i] = node
                return
            if self.__hashtable[i] is None:
                self.__hashtable[i] = node
                return
