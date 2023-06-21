from typing import Any, Hashable


class Node:
    def __init__(self, key: Hashable, value: Any) -> None:
        self.key = key
        self.value = value


class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.capacity = 8
        self.hash_table: list = [None] * self.capacity
        self.load_capacity = 2/3

    def __setitem__(self, key: Hashable, value: Any) -> None:
        index = self.get_index(key)
        while self.hash_table[index] is not None:
            if self.hash_table[index].key == key:
                self.hash_table[index].value = value
                return
            index = (index + 1) % self.capacity
        if self.length + 1 > self.capacity * self.load_capacity:
            self.resize()
            return self.__setitem__(key, value)
        self.hash_table[index] = Node(key, value)
        self.length += 1

    def __getitem__(self, key: Hashable) -> Any:
        index = self.get_index(key)
        while self.hash_table[index] is not None and self.hash_table[index].key != key:
            index = (index + 1) % self.capacity
        if self.hash_table[index] is None:
            raise KeyError(f"Key {key} is not found")
        return self.hash_table[index].value

    def __len__(self) -> int:
        return self.length

    def resize(self) -> None:
        old_nodes = []
        for node in self.hash_table:
            if node is not None:
                old_nodes.append(node)
        self.capacity = self.capacity * 2
        new_hash_table = [None] * self.capacity
        for node in old_nodes:
            index = self.get_index(node.key)
            while new_hash_table[index] is not None:
                index = (index + 1) % self.capacity
            new_hash_table[index] = node
        self.hash_table = new_hash_table

    def get_index(self, key):
        return hash(key) % self.capacity
