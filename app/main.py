from __future__ import annotations

import copy
from typing import Any, Callable, Iterable, Hashable, NamedTuple


class Node(NamedTuple):
    key: Hashable
    k_hash: int
    value: Any


class Dictionary:

    def __init__(self) -> None:
        # added mainly to keep track of input order, iteration
        self._keys = []
        self._values = []

        self._initial_capacity = 8
        self._load_factor = 2 / 3

        self._capacity = self._initial_capacity
        self._hash_table = [[] for _ in range(self._capacity)]

    # didn't add formating for different types due to time complexity
    def __str__(self) -> str:
        pairs = []
        for key, value in zip(self._keys, self._values):
            pairs.append(f"{key}: {value}")
        result = "{" + ", ".join(pairs) + "}"
        return result

    def __getitem__(self, key: Hashable) -> Any:
        return self._data_handler(key)

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if not hash(key):
            raise TypeError(f"unhashable type: {type(key)}")

        if self.get_load():
            self._data_handler(key, value)
        else:
            self.resize()
            self.__setitem__(key, value)

    def __len__(self) -> int:
        return sum(1 for item in self._hash_table if item)

    def __delitem__(self, key: Hashable) -> None:
        if self.__getitem__(key):
            self._data_handler(key, delete=True)

    def keys(self) -> str:
        class DictKeys:
            def __init__(self, keys: list = None) -> None:
                self._keys = keys if keys else []

            def __iter__(self) -> Iterable:
                return iter(self._keys)

            def __repr__(self) -> str:
                return f"dict_keys({self._keys})"

        return DictKeys(self._keys)

    def values(self) -> str:
        class DictValues:
            def __init__(self, values: list = None) -> None:
                self._values = values if values else []

            def __iter__(self) -> Iterable:
                return iter(self._values)

            def __repr__(self) -> str:
                return f"dict_values({self._values})"

        return DictValues(self._values)

    def clear(self) -> None:
        self._hash_table = [[] for _ in range(self._capacity)]
        self._keys = []
        self._values = []

    def get(self, key: Hashable) -> Any:
        try:
            return self.__getitem__(key)
        except KeyError:
            return None

    def pop(self, key: Hashable) -> Any:
        value = self.__getitem__(key)
        self.__delitem__(key)
        return value

    def __iter__(self) -> Dictionary:
        self.current_key = 0
        return self

    def __next__(self) -> Hashable:
        while self.current_key < len(self._keys):
            key = self._keys[self.current_key]
            self.current_key += 1
            return key
        raise StopIteration

    def update(self, other: Dictionary) -> None:
        for item in other:
            self.__setitem__(item, other[item])

    def _data_handler(
            self,
            key: Hashable,
            value: Any = None,
            delete: bool = None
    ) -> None | Callable:
        k_hash = hash(key)
        index = k_hash % self._capacity

        if delete:
            return self._delete_item(key, index)

        if value is not None:
            self._add_item(
                key=key,
                value=value,
                k_hash=k_hash,
                index=index
            )
        else:
            return self._find_item(key=key, index=index)

    def get_load(self) -> int | bool:
        threshold = self._capacity * self._load_factor
        load = sum(1 for node in self._hash_table if node)
        if load < threshold:
            return int(threshold - load)
        return False

    def resize(self) -> None:
        self._capacity *= 2
        old_table = copy.deepcopy(self._hash_table)

        self._keys = []
        self._values = []

        self._hash_table = [[] for _ in range(self._capacity)]
        for item in old_table:
            if item:
                self._data_handler(item.key, item.value)

    def _add_item(
            self,
            key: Hashable,
            value: Any,
            k_hash: int,
            index: int
    ) -> None:
        node = self._hash_table[index]

        if node and node.key == key:
            node.value = value
            return

        if not node:
            self._hash_table[index] = Node(key, k_hash, value)
            self._keys.append(key)
            self._values.append(value)
            return

        if node and node.key != key:
            i = index
            while self._hash_table[i]:
                i = (i + 1) % self._capacity
            self._hash_table[i] = Node(key, k_hash, value)
            self._keys.append(key)
            self._values.append(value)

    def _find_item(self, key: Hashable, index: int) -> Any:
        node = self._hash_table[index]
        # handling empty nodes left after removing collided elements
        if not node:
            if index < len(self._hash_table) - 1:
                i = index
            else:
                i = 0
            while self._hash_table[i] != index:

                if self._hash_table[i] and self._hash_table[i].key == key:
                    return self._hash_table[i].value

                i = (i + 1) % self._capacity

        if node and node.key == key:
            return node.value

        if node and node.key != key:
            i = index
            while self._hash_table[i]:

                if self._hash_table[i].key == key:
                    return self._hash_table[i].value

                i = (i + 1) % self._capacity

        raise KeyError(f"{key}")

    def _delete_item(self, key: Hashable, index: int) -> None:
        node = self._hash_table[index]

        if node and node.key == key:
            self._hash_table[index] = []

            key_index = self._keys.index(key)
            self._keys.pop(key_index)
            self._values.pop(key_index)
            return

        if node and node.key != key:
            i = index
            while self._hash_table[i]:

                if self._hash_table[i].key == key:
                    self._hash_table[i] = []

                    key_index = self._keys.index(key)
                    self._keys.pop(key_index)
                    self._values.pop(key_index)

                    return
                i = (i + 1) % self._capacity
