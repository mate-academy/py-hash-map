from typing import Any, Hashable


class Node:
    def __init__(self, hash_key: int, key: Hashable, value: Any) -> None:
        self.hash_key = hash_key
        self.key = key
        self.value = value


class Dictionary:
    def __init__(self) -> None:
        self._capacity = 8
        self._size_dict = 0
        self.hash_cell = [None] * self._capacity

    def clear(self) -> None:
        self.hash_cell = [None] * self._capacity
        self._size_dict = 0

    def get_hash(self, key: Hashable) -> int:
        hash_key = hash(key) % self._capacity
        i = 1
        while (self.hash_cell[hash_key] is not None
               and self.hash_cell[hash_key].key != key):
            hash_key = (hash_key + i) % self._capacity
            i += 1
        return hash_key

    def __setitem__(self, key: Any, value: Any) -> None:
        hash_key = self.get_hash(key)
        if self.hash_cell[hash_key] is None:
            self._size_dict += 1
            self.hash_cell[hash_key] = Node(hash_key, key, value)
        else:
            self.hash_cell[hash_key].value = value
        if self._size_dict > self._capacity * (2 / 3):
            self.management_hash_cell()

    def update(self, new_dict: dict) -> None:
        for key, value in new_dict.items():
            self.__setitem__(key, value)

    def __delitem__(self, key: Any) -> None:
        hash_key = self.get_hash(key)
        self.hash_cell[hash_key] = None
        self._size_dict -= 1

    def __getitem__(self, key: Any) -> Any:
        hash_key = self.get_hash(key)
        if self.hash_cell[hash_key] is None:
            raise KeyError("key does not exist")
        else:
            return self.hash_cell[hash_key].value

    def pop(self, key: Any) -> Any:
        value = self.__getitem__(key)
        self.__delitem__(key)
        return value

    def management_hash_cell(self) -> None:
        temporaries = self.hash_cell
        self._capacity *= 2
        self.clear()
        for node in temporaries:
            if node:
                self.__setitem__(node.key, node.value)

    def __len__(self) -> int:
        return self._size_dict
