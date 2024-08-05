from __future__ import annotations
from typing import Any, Iterator


class Node:
    def __init__(self, key: Any, key_hash: int, value: Any) -> None:
        self.key = key
        self.key_hash = key_hash
        self.value = value


class Dictionary:
    def __init__(self, capacity: int = 8) -> None:
        self.capacity = capacity
        self.load_factor = 2 / 3
        self.threshold = self.capacity * self.load_factor
        self.nodes = [None] * self.capacity
        self.size = 0

    def __setitem__(self, key: Any, value: Any) -> None:
        if self.size >= self.threshold:
            self.resize()

        key_hash = hash(key)
        index = key_hash % self.capacity

        while self.nodes[index]:
            if self.nodes[index].key == key:
                self.nodes[index].value = value
                return

            index = (index + 1) % self.capacity
            if self.nodes[index] is None:
                break

        if self.nodes[index] is None:
            self.nodes[index] = Node(key, key_hash, value)
            self.size += 1

    def __getitem__(self, key: Any) -> Any:
        index = hash(key) % self.capacity

        while self.nodes[index] and self.nodes[index].key != key:
            index = (index + 1) % self.capacity

        if self.nodes[index] is None:
            raise KeyError(f"Key {key} is not in the dict")

        return self.nodes[index].value

    def __len__(self) -> int:
        return self.size

    def clear(self) -> None:
        self.__init__()

    def __delitem__(self, key: Any) -> None:
        index = hash(key) % self.capacity
        count_loops = 0

        while self.nodes[index] is None or self.nodes[index].key != key:
            index = (index + 1) % self.capacity
            count_loops += 1
            if count_loops >= self.capacity:
                raise KeyError(f"Key {key} is not in the dict")

        self.nodes[index] = None
        self.size -= 1

        if self.size < self.threshold:
            self.resize()

    def get(self, key: Any) -> Any:
        try:
            value = self.__getitem__(key)
        except KeyError:
            return None

        return value

    def pop(self, key: Any) -> Any:
        value = self.__getitem__(key)
        self.__delitem__(key)
        return value

    def update(self, other: Dictionary) -> None:
        for node in other.nodes:
            if node:
                self.__setitem__(node.key, node.value)

    def __iter__(self) -> Iterator[Any]:
        return iter([node.key for node in self.nodes if node])

    def resize(self) -> None:
        old_dict = self.nodes
        if self.size >= self.threshold:
            self.__init__(self.capacity * 2)
        else:
            self.__init__(self.capacity // 2)

        for node in old_dict:
            if node:
                self.__setitem__(node.key, node.value)
