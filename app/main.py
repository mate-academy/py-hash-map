from typing import Hashable, Any
from app.point import Point
from dataclasses import dataclass


@dataclass
class Node:
    key: int
    hash: int
    value: int
    next: "Node" = None

    def __iter__(self):
        self.current = self
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            result = self.current
            self.current = self.current.next
            return result


class Dictionary:
    def __init__(self):
        self.size = 8
        self.length = 0
        self.load_factor = 0.66
        self.hash_table = [None] * self.size
        self.resize = int(self.size * self.load_factor)

    def _resize(self):
        new_capacity = self.size * 2
        new_hash_table = [None] * new_capacity

        for node in self.hash_table:
            while node is not None:
                new_index = self._get_index(node.key, new_capacity)
                if new_hash_table[new_index] is None:
                    new_hash_table[new_index] = node
                else:
                    cur_new_index = new_hash_table[new_index]
                    while cur_new_index.next is not None:
                        cur_new_index = cur_new_index.next
                    cur_new_index.next = node

                if node is not None and node.next is not None:
                    node = node.next
                else:
                    break

        self.hash_table = new_hash_table
        self.size = new_capacity
        self.resize = int(self.size * self.load_factor)

    def _get_index(self, key: Hashable) -> int:
        hash_key = hash(key)
        return hash_key % self.size

    def __getitem__(self, key):
        index = self._get_index(key)
        node = self.hash_table[index]

        while node is not None:
            if node.key == key:
                return node.value
            node = node.next
        raise KeyError("This is not found, please, try again")

    def __setitem__(self, key, value):
        index = self._get_index(key)
        node = Node(key, hash(key), value)

        if self.hash_table[index] is None:
            self.hash_table[index] = node
            self.length += 1
        else:
            cur_index = self.hash_table[index]
            while cur_index is not None:
                if cur_index.key == key:
                    cur_index.value = value
                    return
                if cur_index.key == key:
                    break
                cur_index = cur_index.next

            cur_index.next = node
            self.length += 1

        if self.length >= self.resize:
            self.resize()

    def __len__(self):
        return self.length
