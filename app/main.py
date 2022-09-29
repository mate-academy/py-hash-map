from __future__ import annotations
from typing import Any, Hashable, Iterator


class Dictionary:
    initial_capacity = 8
    load_factor = 2 / 3

    def __init__(self) -> None:
        self.capacity = self.initial_capacity
        self.threshold = int(self.capacity * self.load_factor)
        self.indices = [None] * self.capacity
        self.nodes = []

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if len(self.nodes) >= self.threshold:
            self._resize()

        key_hash = hash(key)
        index, node_index = self._index_lookup(key_hash, key)

        # Add new item
        if node_index is None:
            self.indices[index] = len(self.nodes)
            self.nodes.append((key_hash, key, value))

        # Reassign existing item
        else:
            self.nodes[node_index] = (key_hash, key, value)

    def __getitem__(self, key: Hashable) -> Any:
        key_hash = hash(key)
        index, node_index = self._index_lookup(key_hash, key)

        if node_index is None:
            raise KeyError(key)

        return self.nodes[node_index][2]

    def __delitem__(self, key: Hashable) -> None:
        key_hash = hash(key)
        index, node_index = self._index_lookup(key_hash, key)

        if node_index is None:
            raise KeyError(key)

        self.nodes.pop(node_index)
        self.indices[index] = None

    def __len__(self) -> int:
        return len(self.nodes)

    def __iter__(self) -> Iterator:
        return iter(self.keys())

    def _resize(self) -> None:
        # Increase size
        self.capacity *= 2
        self.threshold = int(self.capacity * self.load_factor)

        # Store data temporarily
        nodes = self.nodes

        # Re-create nodes and indices with new capacity
        self.nodes = []
        self.indices = [None] * self.capacity

        # Add old data to new nodes
        for node in nodes:
            self[node[1]] = node[2]

    def _index_lookup(
            self, key_hash: int, key: Hashable
    ) -> tuple[int, int | None]:
        index = key_hash % self.capacity

        while True:
            node_index = self.indices[index]

            # Not sure if it's okay to break lines like this
            if node_index is None or (self.nodes[node_index][0] == key_hash
                                      and self.nodes[node_index][1] == key):
                return index, node_index

            # Formula from CPython dict implementation :)
            # In short, it generates a pseudo-random sequence of numbers
            index = ((5 * index) + 1) % self.capacity

    def clear(self) -> None:
        self.capacity = self.initial_capacity
        self.indices = [None] * self.capacity
        self.nodes.clear()

    def get(self, key: Hashable) -> Any:
        try:
            return self[key]
        except KeyError:
            return None

    def pop(self, key: Hashable) -> Any:
        value = self[key]
        del self[key]
        return value

    def items(self) -> list[tuple]:
        # Needed for update() method
        return [(node[1], node[2]) for node in self.nodes]

    def keys(self) -> list[Any]:
        # Needed for __iter__() method
        return [node[1] for node in self.nodes]

    def update(self, other: Dictionary | dict) -> None:
        for key, value in other.items():
            self[key] = value
