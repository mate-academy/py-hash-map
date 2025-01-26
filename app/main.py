from dataclasses import dataclass
from typing import Any


class Dictionary:
    @dataclass
    class Node:
        key: Any
        value: Any
        key_hash: int

        def __eq__(self, other: type) -> bool:
            if isinstance(other, Dictionary.Node):
                return self.key == other.key
            else:
                return self.key == other

        def get_key_hash(self) -> int:
            return self.key_hash

    def __init__(self) -> None:
        self._capacity: int = 8
        self._load_factor: int = int(self._capacity * (2 / 3))
        self._occupied = 0
        self._hash_table = [None for _ in range(self._capacity)]

    def __setitem__(self, key: Any, value: Any) -> None:
        self._change_capacity()
        self._set_key(key, value)

    def __getitem__(self, item: Any) -> Any:
        index, _ = self._calculate_index_and_hash(item)

        if self._hash_table[index] is None:
            raise KeyError(f"No key: {item} in dict")

        if self._hash_table[index].key == item:
            return self._hash_table[index].value
        else:
            for _ in range(self._capacity - 1):
                index += 1
                index %= self._capacity

                if (self._hash_table[index] is not None
                        and self._hash_table[index] == item):
                    return self._hash_table[index].value
        raise KeyError(f"No key: {item} in dict")

    def __len__(self) -> int:
        return self._occupied

    def clear(self) -> None:
        self._hash_table = [None for _ in range(self._capacity)]
        self._occupied = 0

    def __delitem__(self, item: Any) -> None:
        index, _ = self._calculate_index_and_hash(item)

        if self._hash_table[index] is None:
            raise KeyError(f"There's no key: {item}. When trying to delete!")

        if self._hash_table[index].key == item:
            self._hash_table[index] = None
            return
        else:
            for _ in range(self._capacity - 1):
                index += 1
                index %= self._capacity

                if (self._hash_table[index] is not None
                        and self._hash_table[index] == item):
                    self._hash_table[index] = None
                    return
        raise KeyError(f"There's no key: {item}. When trying to delete!")

    def _calculate_index_and_hash(self, key: Any) -> (int, int):
        key_hash = hash(key)
        index = key_hash % self._capacity
        return index, key_hash

    def _set_key(self, key: Any, value: Any) -> None:
        index, key_hash = self._calculate_index_and_hash(key)
        empty_index = 0
        if self._hash_table[index] is None:
            empty_index = index
            self._occupied += 1
        else:
            for _ in range(self._capacity):
                if self._hash_table[index] is None:
                    empty_index = index
                    self._occupied += 1
                    break
                elif self._hash_table[index] == key:
                    empty_index = index
                    break
                index += 1
                index %= self._capacity

        self._hash_table[empty_index] = self.Node(key, value, key_hash)

    def _change_capacity(self) -> None:
        if self._occupied >= self._load_factor:
            self._capacity *= 2
            self._load_factor: int = int(self._capacity * (2 / 3))
            self._occupied = 0

            old_hash_table = self._hash_table
            self._hash_table = [None for _ in range(self._capacity)]

            for node in old_hash_table:
                if node is not None:
                    self._set_key(node.key, node.value)
