from __future__ import annotations
from typing import Any, Hashable


class Dictionary:
    def __init__(self) -> None:
        self.length: int = 0
        self.hash_table: list = [None] * 8

    @staticmethod
    def find_index_for_node(key: Hashable, hash_table: list) -> int:
        node_index = hash(key) % len(hash_table)

        while hash_table[node_index] and key != hash_table[node_index][1]:
            node_index += 1
            node_index %= len(hash_table)
        return node_index

    def node_filling(
            self,
            key: Hashable,
            value: Any,
            hash_table: list
    ) -> None:
        node_index = self.find_index_for_node(key, hash_table)
        if (
            not hash_table[node_index]
            and self.hash_table == hash_table
        ):
            self.length += 1

        hash_table[node_index] = [hash(key), key, value]

    def __setitem__(
            self,
            key: Hashable,
            value: Any
    ) -> None:
        node_index = self.find_index_for_node(key, self.hash_table)
        threshold = int(len(self.hash_table) * (2 / 3))

        if (
            self.length + 1 > threshold
            and self.hash_table[node_index] is None
        ):
            new_hash_table = [None] * len(self.hash_table) * 2

            for node in self.hash_table:
                if node:
                    self.node_filling(node[1], node[2], new_hash_table)

            self.hash_table = new_hash_table

        self.node_filling(key, value, self.hash_table)

    def __getitem__(self, key: Hashable) -> Any:
        node_index = self.find_index_for_node(key, self.hash_table)

        if self.hash_table[node_index] is None:
            raise KeyError
        return self.hash_table[node_index][-1]

    def __len__(self) -> int:
        return self.length

    def __delitem__(self, key: Hashable) -> None:
        node_index = self.find_index_for_node(key, self.hash_table)

        if self.hash_table[node_index] is None:
            raise KeyError

        self.hash_table[node_index] = None

    def get(self, key: Hashable) -> Any:
        node_index = self.find_index_for_node(key, self.hash_table)
        if self.hash_table[node_index] is None:
            return None

        return self.hash_table[node_index][-1]

    def clear(self) -> None:
        for index in range(len(self.hash_table)):
            self.hash_table[index] = None

    def pop(self, key: Hashable) -> Any:
        node_index = self.find_index_for_node(key, self.hash_table)
        if self.hash_table[node_index] is None:
            raise KeyError

        element_to_pop = self.hash_table[node_index]
        self.hash_table[node_index] = None
        return element_to_pop[-1]

    def update(self, other_dict: dict) -> None:
        for key, value in other_dict.items():
            self[key] = value
