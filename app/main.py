from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from typing import Hashable, Any, Iterator, Optional, Iterable


class Dictionary:
    @dataclass
    class Node:
        key: Hashable
        value: Any
        key_hash: int

    INITIAL_CAPACITY = 8
    RESIZE_THRESHOLD = Fraction(2, 3)
    CAPACITY_MULTIPLIER = 2

    def __init__(self, capacity: int = INITIAL_CAPACITY) -> None:
        self.capacity = capacity
        self.size = 0
        self.hash_table: list[Dictionary.Node | None] = [None] * self.capacity

    def _calculate_index(self, key: Hashable) -> int:
        index = hash(key) % self.capacity

        while (
            self.hash_table[index] is not None
            and self.hash_table[index].key != key
        ):
            index = (index + 1) % self.capacity

        return index

    @property
    def current_max_size(self) -> int:
        return int(self.capacity * self.RESIZE_THRESHOLD)

    def _resize(self) -> None:
        old_hash_table = self.hash_table

        self.__init__(self.capacity * self.CAPACITY_MULTIPLIER)

        for node in old_hash_table:
            if node is not None:
                self.__setitem__(node.key, node.value)

    def __setitem__(self, key: Hashable, value: Any) -> None:
        index = self._calculate_index(key)
        key_hash = hash(key)

        if self.hash_table[index] is None:
            if self.size + 1 >= self.current_max_size:
                self._resize()
                index = self._calculate_index(key)
            self.size += 1

        self.hash_table[index] = Dictionary.Node(key, value, key_hash)

    def __getitem__(self, key: Hashable) -> Any:
        index = self._calculate_index(key)

        if self.hash_table[index] is None:
            raise KeyError(f"Cannot find value for key: {key}")

        return self.hash_table[index].value

    def __delitem__(self, key: Hashable) -> None:
        index = self._calculate_index(key)

        if self.hash_table[index] is None:
            raise KeyError(f"Cannot delete value for key: {key}")

        self.hash_table[index] = None
        self.size -= 1

    def __iter__(self) -> Iterator[tuple[Hashable, Any]]:
        for node in self.hash_table:
            if node is not None:
                yield node.key, node.value

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        items = [
            f"{node.key}: {node.value}"
            for node in self.hash_table
            if node is not None
        ]
        return "{" + ", ".join(items) + "}"

    def get(self, key: Hashable, default: Optional[Any] = None) -> Any:
        """
        Get the value for the given key.
        If the key does not exist, return the default value.

        Default value is optional.
        If it was not provided, method will raise KeyError.
        """
        try:
            return self[key]
        except KeyError:
            if default is not None:
                return default
            else:
                raise KeyError(
                    f"Cannot find value for key: {key}"
                    "and no default value is provided"
                )

    def pop(self, key: Hashable) -> Any:
        value = self[key]
        self.__delitem__(key)
        return value

    def _update_from_node(self, data: Node) -> None:
        """
        Updates the dictionary with a Node object.
        """
        self.__setitem__(data.key, data.value)

    def _update_from_dict(self, data: Dictionary) -> None:
        for node in data.hash_table:
            if node is not None:
                self.__setitem__(node.key, node.value)

    def _update_from_builtin_dict(self, data: dict) -> None:
        """
        Updates the dictionary with key-value pairs from builtin dictionary.
        """
        for key, value in data.items():
            self.__setitem__(key, value)

    def _update_from_tuple(self, data: tuple) -> None:
        """
        Updates the dictionary with a key-value pair from a tuple.
        """
        if len(data) != 2:
            raise ValueError("Tuple must have 2 elements (key, value)")

        key, value = data

        if not isinstance(key, Hashable):
            raise TypeError("Key must be Hashable")

        self.__setitem__(key, value)

    def update(
            self,
            data: Dictionary | list[Node | dict | tuple] | Node | dict | tuple
    ) -> None:
        """
        Updates Dictionary with various types of data.
        """
        if isinstance(data, Dictionary):
            self._update_from_dict(data)
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, Dictionary.Node):
                    self._update_from_node(item)
                elif isinstance(item, dict):
                    self._update_from_builtin_dict(item)
                elif isinstance(item, tuple):
                    self._update_from_tuple(item)

        elif isinstance(data, Dictionary.Node):
            self._update_from_node(data)
        elif isinstance(data, dict):
            self._update_from_builtin_dict(data)
        elif isinstance(data, tuple):
            self._update_from_tuple(data)

    def copy(self) -> Dictionary:
        """
        Creates a copy of the dictionary.
        """
        new_dict = Dictionary(self.capacity)

        for node in self.hash_table:
            if node is not None:
                new_dict.__setitem__(node.key, node.value)

        return new_dict

    def clear(self) -> None:
        """
        Resets the dictionary to its initial state.
        """
        self.__init__(self.INITIAL_CAPACITY)

    @staticmethod
    def from_keys(keys: Iterable, value: Any = None) -> Dictionary:
        """
        Static method to create a new dictionary from keys.
        """
        new_dict = Dictionary(Dictionary.INITIAL_CAPACITY)

        for key in keys:
            new_dict.__setitem__(key, value)

        return new_dict
