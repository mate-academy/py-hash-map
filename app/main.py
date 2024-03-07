from __future__ import annotations
from typing import Any, List, Hashable


class Node:
    def __init__(
            self,
            key: Hashable,
            value: Any,
            next: Node | None = None
    ) -> None:
        self.key = key
        self.value = value
        self.next = next
    # TODO: Need to rewrite all methods for use Node like "next"


class Dictionary:
    def __init__(self) -> None:
        self._capacity = 8
        self._factor = 2 / 3
        self._size = 0
        self._table: List[Node | None] = [None] * self._capacity

    def __str__(self):
        items = [(node.key, node.value) for node in self._table if
                 node is not None]
        return "{" + ", ".join(f"{key}: {value}" for key, value in items) + "}"

    @staticmethod
    def validation_for_key(key: Any) -> None:
        if not isinstance(key, Hashable):
            raise TypeError(f"{type(key)} invalid data type for dictionary")

    def _add_new_node(self, key: Hashable, value: Any) -> None:
        index = self._get_index(key)

        if self._table[index] is None:
            self._table[index] = Node(key, value)
            self._size += 1
            self._check_resize()
        elif self._table[index].key == key:
            self._table[index].value = value
            return
        else:
            index_to_next_node = self._table[index].next
            while index_to_next_node is not None:
                if self._table[index_to_next_node].key == key:
                    self._table[index_to_next_node].value = value
                    return
                index_to_next_node = self._table[index_to_next_node].next

            for i in range(self._capacity):
                new_index = (index + i) % self._capacity
                if self._table[new_index] is None:
                    self._table[new_index] = Node(key, value)
                    self._table[index].next = new_index
                    self._size += 1
                    self._check_resize()
                    break
                index = new_index

    def __setitem__(self, key: Hashable, value: Any) -> None:
        self.validation_for_key(key)

        self._add_new_node(key, value)

    def __getitem__(self, key: Hashable) -> Any:
        self.validation_for_key(key)
        index = self._get_index(key)

        if self._table[index] is None:
            raise KeyError(f"Element {key} not in dictionary")

        elif self._table[index].key == key:
            return self._table[index].value
        else:
            index_to_next_node = self._table[index].next
            while index_to_next_node is not None:
                if self._table[index_to_next_node].key == key:
                    return self._table[index_to_next_node].value
                index_to_next_node = self._table[index_to_next_node].next
        raise KeyError(f"Element {key} not in dictionary")

    def __len__(self):
        return self._size

    def _get_index(self, key: Hashable) -> int:
        return hash(key) % self._capacity

    def _resize(self) -> None:
        old_table = [node for node in self._table if node is not None]
        self._capacity = self._capacity * 2
        self._table = [None] * self._capacity
        self._size = 0

        for node in old_table:
            self._add_new_node(node.key, node.value)

    def _check_resize(self) -> None:
        if self._size > self._capacity * self._factor:
            self._resize()

    def clear(self) -> None:
        self._table = [None] * self._capacity
        self._size = 0
