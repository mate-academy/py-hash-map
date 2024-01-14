from __future__ import annotations
import random
from typing import Any


class Node:

    def __init__(self, key: Any, value: Any) -> None:
        self._key = key
        self._value = value
        self.hash = hash(self)

    def get_key(self) -> Any:
        return self._key

    def get_value(self) -> Any:
        return self._value

    def set_value(self, value: Any) -> None:
        self._value = value

    def remove(self) -> None:
        del self

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Node):
            if self._key == other.get_key():
                return True
        if self.hash == (hash(other)):
            return True
        return False

    def __hash__(self) -> int:
        # if isinstance(self._key, (int, bool, float)):
        #     return int(self._key * 1452574 * ord(str(self._key)[-1]) + 5)
        # if isinstance(self._key, str):
        #     return (4869781 * ord(self._key[0]) * ord(self._key[-1])
        #             * len(self._key) * (ord(self._key[0]) + 2) * 3 + 5)
        return hash(self._key)

    def __repr__(self) -> str:
        return str(self._value)


class Dictionary:
    keys = []

    def __init__(self) -> None:
        self.lentgh = 0
        self.capacity = 8
        self.hash_table = self.make_hash_table()

    def items(self) -> list[tuple[Any, Any]]:
        items = []
        for node in self.hash_table:
            if node:
                items.append((node.get_key(), node.get_value()))
        return items

    def __repr__(self) -> str:
        str_dict = ""
        for key, value in self.items():
            if isinstance(key, str):
                str_dict += f"'{key}': {value}, "
            else:
                str_dict += f"{key}: {value}, "

        return "{" + str_dict[:-2] + "}"

    def __len__(self) -> int:
        return self.lentgh

    @classmethod
    def make_hash_table(cls, lentgh: int = 8) -> list[None]:
        hash_table = []
        for i in range(lentgh):
            hash_table.append(None)
        return hash_table

    def __setitem__(self, key: Any, value: Any) -> None:
        if isinstance(key, (dict, list)):
            raise ValueError(f"Не можна задавати такий ключ - "
                             f"[{type(key)}] для словника")

        node = Node(key, value)
        index = node.hash % self.capacity

        if key not in self.keys:
            if self.lentgh == int(self.capacity * 2 / 3):
                self.resize(node)
                return

            if not self.hash_table[index]:
                self.hash_table[index] = node
                self.keys.append(key)
                self.lentgh += 1
                return

            random.seed(611)
            for _ in range(self.capacity * 2):
                index = random.randint(0, self.capacity - 1)
                if not self.hash_table[index]:
                    self.hash_table[index] = node
                    self.keys.append(key)
                    self.lentgh += 1
                    return

        else:
            index = node.hash % self.capacity
            if self.hash_table[index]:
                if self.hash_table[index].get_key() == key:
                    self.hash_table[index].set_value(value)
                    return

            random.seed(611)
            for _ in range(self.capacity * 2):
                index = random.randint(0, self.capacity - 1)
                if self.hash_table[index]:
                    if self.hash_table[index].get_key() == key:
                        self.hash_table[index].set_value(value)
                        return

            random.seed(611)
            for _ in range(self.capacity * 2):
                index = random.randint(0, self.capacity - 1)
                if not self.hash_table[index]:
                    self.hash_table[index] = node
                    return

    def __getitem__(self, key: Any) -> Any:
        if key not in self.keys:
            raise KeyError(f"Немає такого ключа - [{key}] в словнику")

        node = Node(key, None)
        index = node.hash % self.capacity
        if self.hash_table[index]:
            if self.hash_table[index].get_key() == key:
                return self.hash_table[index].get_value()

        random.seed(611)
        for _ in range(self.capacity * 2):
            index = random.randint(0, self.capacity - 1)
            if self.hash_table[index].get_key() == key:
                return self.hash_table[index].get_value()

        random.seed(611)
        for _ in range(self.capacity * 2):
            index = random.randint(0, self.capacity - 1)
            if not self.hash_table[index]:
                return self.hash_table[index].get_value()

    def resize(self, new_node: Node) -> None:
        temp_hash_table = self.hash_table.copy()

        self.hash_table = self.make_hash_table(self.capacity * 2)
        self.capacity *= 2
        self.keys = []
        self.lentgh = 0

        for node in temp_hash_table:
            if node:
                self.__setitem__(node.get_key(), node.get_value())
        self.__setitem__(new_node.get_key(), new_node.get_value())
