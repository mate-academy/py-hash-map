import dataclasses
from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.size: int = 0
        self.capacity: int = 8
        self.node = [None] * self.capacity

    def __len__(self) -> int:
        return self.size

    def __setitem__(self, key: Any, value: Any) -> Any:
        index = hash(key) % self.capacity
        treshold = self.capacity * 2 / 3
        while self.node[index] is not None:
            if self.node[index].key == key:
                self.node[index].value = value
                return key, value
            index = (index + 1) % self.capacity
        if self.size > treshold:
            self.capacity *= 2
            items = [item for item in self.node if item is not None]
            self.size = 0
            self.node = [None] * self.capacity
            for item in items:
                self.__setitem__(item.key, item.value)
            self.__setitem__(key=key, value=value)
            return key, value
        self.size += 1
        self.node[index] = Node(key=key, value=value, hash_=hash(key))

    def __getitem__(self, key: Any) -> None:
        index = hash(key) % self.capacity
        while self.node[index] is not None:
            if self.node[index].key == key:
                return self.node[index].value
            index = (index + 1) % self.capacity
        raise KeyError("Dictionary key is not found")


@dataclasses.dataclass
class Node:
    key: Any
    value: Any
    hash_: Any
