from typing import Any, Hashable


class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.capacity = 8
        self.resize_threshold = self.capacity * (2 / 3)
        self.hash_table = [None] * self.capacity

    def get_index_of_cell(self, key: Hashable) -> int:
        return hash(key) % self.capacity

    def __setitem__(self, key: Hashable, value: Any) -> None:
        index = self.get_index_of_cell(key)

        while True:
            if self.hash_table[index] is None:
                self.hash_table[index] = (key, hash(key), value)
                self.length += 1
                break
            if self.hash_table[index][0] == key:
                self.hash_table[index] = (key, hash(key), value)
                break
            index = (index + 1) % self.capacity
        if self.length > self.resize_threshold:
            self.resize_hash_table()

    def __getitem__(self, key: Hashable) -> Any:
        index = self.get_index_of_cell(key)
        while self.hash_table[index] is not None:
            if (
                self.hash_table[index][0] == key
                and len(self.hash_table[index]) < 4
            ):
                return self.hash_table[index][2]
            index = (index + 1) % self.capacity
        raise KeyError("Invalid key")

    def resize_hash_table(self) -> None:
        self.length = 0
        self.capacity *= 2
        old_hash_table = self.hash_table.copy()
        self.resize_threshold = self.capacity * (2 / 3)
        self.hash_table = [None] * self.capacity
        for node in old_hash_table:
            if node:
                self.__setitem__(node[0], node[2])

    def __len__(self) -> int:
        return self.length

    def get(self, key: Hashable, value: Any = None) -> Any:
        try:
            return self.__getitem__(key)
        except KeyError:
            return value

    def clear(self) -> None:
        self.length = 0
        self.capacity = 8
        self.resize_threshold = self.capacity * (2 / 3)
        self.hash_table = [None] * self.capacity

    def __delitem__(self, key: Hashable) -> None:
        index = self.get_index_of_cell(key)
        while self.hash_table[index] is not None:
            if self.hash_table[index][0] == key:
                self.hash_table[index] = (
                    self.hash_table[index][0],
                    self.hash_table[index][1],
                    self.hash_table[index][2],
                    "Deleted"
                )
                return
            index = (index + 1) % self.capacity
        raise KeyError("Invalid key")

    def pop(self, key: Hashable, default: Any = None) -> Any:
        try:
            value = self.__getitem__(key)
            self.__delitem__(key)
            return value
        except KeyError:
            if default:
                return default
            if default is None:
                return None
            if default is False:
                return False
