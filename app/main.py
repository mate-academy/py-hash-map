from __future__ import annotations
import random
from typing import Any


class Node:

    def __init__(self, key: Any, value: Any) -> None:
        self._key = key
        self._value = value
        self.hash = hash(key)

    def get_key(self) -> Any:
        return self._key

    def get_value(self) -> Any:
        return self._value

    def set_value(self, value: Any):
        self._value = value

    def remove(self) -> None:
        del self

    def __hash__(self) -> int:
        if isinstance(self._key, (int, bool, float)):
            return self._key * 1452574 * ord(str(self._key)[-1]) + 5
        return 4869781 * ord(self._key[0]) * ord(self._key[-1]) * len(self._key) * (ord(self._key[0]) + 2) * 3 + 5

    def __repr__(self):
        return f"{self._key} -> {self._value}"


class Dictionary:
    keys = []

    def __init__(self) -> None:
        self.lentgh = 0
        self.capacity = 8
        self.hash_table = self.make_hash_table()

    def make_hash_table(self, lentgh: int = 8):
        hash_table = []
        for i in range(lentgh):
            hash_table.append(None)
        return hash_table

    def __setitem__(self, key: Any, value: Any) -> None:
        if isinstance(key, (dict, list)):
            raise ValueError(f"Не задавати такий ключ - [{type(key)}] для словника")

        node = Node(key, value)
        index = node.hash % self.capacity
        random.seed(611)

        if key not in self.keys:
            for _ in range(self.capacity * 2):
                if not self.hash_table[index]:
                    if self.lentgh == int(self.capacity * 2 / 3):
                        self.resize(node)
                        return

                    self.hash_table[index] = node
                    self.keys.append(key)
                    self.lentgh += 1
                    return

                index = random.randint(0, self.capacity - 1)

        if self.hash_table[index].get_key() == key:
            self.hash_table[index].set_value(value)
            return

        else:
            random.seed(611)
            for _ in range(self.capacity * 2):
                index = random.randint(0, self.capacity - 1)
                if self.hash_table[index].get_key() == key:
                    self.hash_table[index].set_value(value)
                    return

            random.seed(611)
            for _ in range(10):
                index = random.randint(0, self.capacity - 1)
                if not self.hash_table[index]:
                    self.hash_table[index] = node
                    return

    def resize(self, new_node: Node):
        temp_hash_table = self.hash_table.copy()
        print(self.hash_table)
        self.hash_table = self.make_hash_table(self.capacity * 2)
        print(self.hash_table)
        for node in temp_hash_table:
            if node:
                self.__setitem__(node.get_key(), node.get_value())
        self.__setitem__(new_node.get_key(), new_node.get_value())



if __name__ == '__main__':
    dictionar = Dictionary()
    dictionar[5] = 2
    dictionar[2] = 2
    dictionar["ss"] = 113
    dictionar["aass"] = 113
    dictionar["dsa"] = 113

    print(dictionar.hash_table)

    print(hash(2))
    print(hash(5))