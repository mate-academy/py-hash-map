from dataclasses import dataclass
from fractions import Fraction
from typing import Any, Hashable


class Dictionary:
    def __init__(self) -> None:
        self._length: int = 0
        self._hash_table: list = [None] * 8
        self._hash_size: int = 8
        self._resize_factor: Fraction = Fraction(2, 3)
        self._resize_multiplier: int = 2

    def __setitem__(self, key: Hashable, value: Any) -> None:
        self._hash_size_check_increase()

        hash_key = self._find_key_position(key)
        while self._hash_table[hash_key] is not None:
            if self._hash_table[hash_key].key == key:
                self._hash_table[hash_key].value = value
                return
            hash_key = self._move_table_right(hash_key)

        node = self.Node(hash_=hash(key), key=key, value=value)
        self._hash_table[hash_key] = node
        self._length += 1

    def __getitem__(self, key: Hashable) -> Any:
        index = self._find_key_in_table(key=key)
        return self._hash_table[index].value

    def __delitem__(self, key: Hashable) -> None:
        index = self._find_key_in_table(key=key)
        self._hash_table[index] = None
        self._length -= 1

    def __len__(self) -> int:
        return self._length

    def __repr__(self) -> str:
        result = [f"{item.key}:{item.value}"
                  for item in self._hash_table
                  if item is not None]
        return "{" + ", \n".join(result) + "}"

    def pop(self, key: Hashable, default: Any = None) -> Any:
        """
        func returns/removes value/item if key exists,
        otherwise return/raise default/KeyError
        """
        try:
            result = self[key]
            del self[key]
        except KeyError:
            if default:
                return default
            raise KeyError(f"Key '{key}' is not found in dictionary")
        return result

    def get(self, key: Hashable, default: Any = None) -> Any | None:
        """
        Works same as __getitem__ but
        doesn't return KeyError if key doesn't exist
        """
        try:
            return self[key]
        except KeyError:
            return default

    def clear(self) -> None:
        self._hash_table = [None] * 8
        self._hash_size = 8
        self._length = 0

    def _find_key_position(self, key: Hashable) -> int:
        return hash(key) % self._hash_size

    def _move_table_right(self, hashed_key: int) -> int:
        return (hashed_key + 1) % self._hash_size

    def _hash_size_check_increase(self) -> None:
        """
        Supporting func to check and increase hash_table size when needed
        """
        if len(self) == int(self._hash_size * self._resize_factor):
            self._hash_size *= self._resize_multiplier
            temp_hash_table = [None] * self._hash_size
        else:
            return

        for item in self._hash_table:
            if item is not None:
                item_key_hash = hash(item.key) % self._hash_size

                while temp_hash_table[item_key_hash] is not None:
                    item_key_hash = (item_key_hash + 1) % self._hash_size

                temp_hash_table[item_key_hash] = item
        self._hash_table = temp_hash_table

    def _find_key_in_table(self, key: Hashable) -> int:
        index = self._find_key_position(key)
        table = self._hash_table

        for _ in range(self._hash_size):
            if table[index] is not None and table[index].key == key:
                return index
            index = self._move_table_right(index)
        raise KeyError(f"Key '{key}' is not found in dictionary")

    @dataclass
    class Node:
        hash_: int
        key: Hashable
        value: Any
