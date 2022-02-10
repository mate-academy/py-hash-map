from dataclasses import dataclass
from typing import Any, List, Optional


@dataclass
class Node:
    hash: int
    key: Any
    value: Any


class Dictionary:
    _DEFAULT_lENGHT = 8
    _LENGTH_RESIZE_COEF = 2 / 3
    _RESIZE_MULT_COEF = 2

    def __init__(self):
        self._table: \
            List[Optional[Node]] = \
            [None for _ in range(Dictionary._DEFAULT_lENGHT)]
        self._size = 0
        self._capacity = Dictionary._DEFAULT_lENGHT

    def _resize(self):
        existing_nodes = [node for node in self._table if node is not None]
        self._capacity *= Dictionary._RESIZE_MULT_COEF
        self._table = [None for _ in range(self._capacity)]
        self._size = 0

        for node in existing_nodes:
            self.__setitem__(node.key, node.value)

    def __setitem__(self, key, value):
        hash_ = hash(key)

        index = hash_ % self._capacity

        while self._table[index] is not None:
            current_node = self._table[index]

            if hash_ == current_node.hash and key == current_node.key:
                current_node.value = value
                return

            index = (index + 1) % self._capacity

        self._table[index] = Node(hash_, key, value)

        self._size += 1
        if (self._size + 1) > Dictionary._LENGTH_RESIZE_COEF * self._capacity:
            self._resize()

    def __getitem__(self, key):
        hash_ = hash(key)

        index = hash_ % self._capacity

        while self._table[index] is not None:
            current_node = self._table[index]

            if hash_ == current_node.hash and key == current_node.key:
                return current_node.value

            index = (index + 1) % self._capacity

        raise KeyError(key)

    def __len__(self):
        return self._size
