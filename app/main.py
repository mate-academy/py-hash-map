from typing import Any, Hashable
from fractions import Fraction
from app.node import Node


class Dictionary:
    def __init__(self) -> None:
        self._length: int = 0
        self._hash_table: list = [None] * 8
        self._hash_size: int = 8
        self._resize_factor: Fraction = Fraction(2, 3)
        self._resize_multiplier: int = 2

    def __setitem__(self, key: Hashable, value: Any) -> None:
        self._hash_size_check_increase()
        key_exists, key_hash_position = self._while_key_hash_occupied(
            action="set", key=key, value=value
        )
        if not key_exists:
            node = Node(hash_=hash(key), key=key, value=value)
            self._hash_table[key_hash_position] = node
            self._length += 1

    def __getitem__(self, key: Hashable) -> Any | None:
        key_exists, return_value = self._while_key_hash_occupied(
            action="get", key=key
        )
        if key_exists:
            return return_value
        raise KeyError("Key is not found in the Dictionary")

    def __len__(self) -> int:
        return self._length

    def __repr__(self) -> str:
        result = [f"{item.key}:{item.value}"
                  for item in self._hash_table
                  if item is not None]
        return "{" + ", \n".join(result) + "}"

    def __delitem__(self, key: Hashable) -> None:
        key_hash_position = self._find_key_position(key)
        index_len = 0

        while index_len <= self._hash_size:
            if (self._hash_table[key_hash_position]
                    and self._hash_table[key_hash_position].key == key):
                self._hash_table[key_hash_position] = None
                self._length -= 1
                return

            key_hash_position += 1
            index_len += 1

        raise KeyError("Key is not found in the Dictionary")

    def pop(self, key: Hashable) -> Any:
        result = self[key]
        del self[key]
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

    def _hash_size_check_increase(self) -> None:
        """Supporting func to check and increase hash_table size when needed"""
        if len(self) == int(self._hash_size * self._resize_factor):
            self._hash_size *= self._resize_multiplier
            temp_hash_table = [None] * self._hash_size
        else:
            return

        for item in self._hash_table:
            if item is not None:
                item_key_hash_position = hash(item.key) % self._hash_size

                while temp_hash_table[item_key_hash_position] is not None:
                    item_key_hash_position = ((item_key_hash_position + 1)
                                              % self._hash_size)

                temp_hash_table[item_key_hash_position] = item
        self._hash_table = temp_hash_table

    def _while_key_hash_occupied(self,
                                 action: str,
                                 key: Hashable,
                                 value: Any = None) -> tuple:

        key_hash_position = self._find_key_position(key)
        decision_condition = False
        table = self._hash_table

        while table[key_hash_position] is not None:
            if table[key_hash_position].key == key:
                if action == "set":
                    table[key_hash_position].value = value
                    decision_condition = True
                    return decision_condition, key_hash_position
                elif action == "get":
                    decision_condition = True
                    return decision_condition, table[key_hash_position].value
            key_hash_position = (key_hash_position + 1) % self._hash_size

        return decision_condition, key_hash_position
