import dataclasses
from typing import Any


@dataclasses.dataclass()
class Node:
    key: Any
    value: Any


class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.size = 0
        self.threshold = round(self.capacity * 2/3)
        self.hash_table = ["_" for i in range(self.capacity)]

    def collision(self, node: Node, node_ind: int) -> int:
        curr_id = node_ind
        while True:
            if curr_id < len(self.hash_table):
                if self.hash_table[curr_id] == "_":
                    return curr_id
                if self.hash_table[curr_id].key == node.key:
                    return curr_id
            else:
                curr_id = 0
                continue
            curr_id += 1

    def resize(self) -> None:
        self.capacity *= 2
        self.threshold = round(self.capacity * 2 / 3)
        old_table = self.hash_table.copy()
        self.hash_table = ["_" for i in range(self.capacity)]
        self.size = 0
        for elem in old_table:
            if elem != "_":
                self.__setitem__(elem.key, elem.value)

    def __setitem__(self, key, value) -> None:
        new_node = Node(key, value)
        self.size += 1
        if self.size <= self.threshold:
            ind = hash(new_node.key) % self.capacity
            if self.hash_table[ind] != "_":
                ind = self.collision(new_node, ind)
            self.hash_table[ind] = new_node
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

    def __getitem__(self, key) -> Node:
        ind = hash(key) % self.capacity
        if self.hash_table[ind] == "_" or self.hash_table[ind].key != key:
            raise KeyError("There is no element with this key")
        return self.hash_table[ind]

    def __len__(self) -> int:
        len_ = 0
        for node in self.hash_table:
            if node != "_":
                len_ += 1
        return len_

    def clear(self) -> None:
        self.hash_table = ["_" for i in range(self.capacity)]

    def __delitem__(self, key) -> None:
        self.hash_table[key] = "_"

