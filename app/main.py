from dataclasses import dataclass
from typing import Any, Hashable


@dataclass
class Node:
    key: Hashable
    value: Any
    hash_of_key: int


class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.size = 0
        self.threshold = round(self.capacity * 2 / 3)
        self.hash_table = [None] * self.capacity

    def collision(self, node: Node, node_ind: int) -> int:
        current_id = node_ind
        while True:
            if current_id < len(self.hash_table):
                if (not self.hash_table[current_id]
                        or self.hash_table[current_id].key == node.key):
                    return current_id
            else:
                current_id = 0
                continue
            current_id += 1

    def resize(self) -> None:
        self.capacity *= 2
        self.threshold = round(self.capacity * 2 / 3)
        old_table = self.hash_table.copy()
        self.hash_table = [None] * self.capacity
        self.size = 0
        for elem in old_table:
            if elem:
                self.__setitem__(elem.key, elem.value)

    def __setitem__(self, key: Hashable, value: Any) -> None:
        new_node = Node(key, value, hash(key))
        self.size += 1
        if self.size <= self.threshold:
            index = new_node.hash_of_key % self.capacity
            if self.hash_table[index]:
                index = self.collision(new_node, index)
            self.hash_table[index] = new_node
            new_node.hash_of_key = index
        else:
            self.resize()
            self.__setitem__(key, value)

    def __str__(self) -> str:
        print_str = ""
        for node in self.hash_table:
            if isinstance(node, str):
                print_str += " " + node
            else:
                print_str += " " + str(node.key) + str(node.value)
        return print_str

    def __getitem__(self, key: Hashable) -> Node:
        for node in self.hash_table:
            if node:
                if node.key == key:
                    return node.value
        raise KeyError

    def __len__(self) -> int:
        len_ = 0
        for node in self.hash_table:
            if node:
                len_ += 1
        return len_

    def clear(self) -> None:
        self.size = 0
        self.hash_table = [None] * self.capacity

    def __delitem__(self, key: Hashable) -> None:
        self.hash_table[key] = None
        self.size -= 1
