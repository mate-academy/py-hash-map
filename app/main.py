from typing import Any, Hashable


class Dictionary:

    LOAD_FACTOR = 2 / 3

    def __init__(self) -> None:
        self.length = 0
        self.hash_table = [None] * 8
        self.capacity = len(self.hash_table)

    def __setitem__(self, key: Hashable, value: Any) -> None:
        index = self.count_index(key)

        while self.hash_table[index]:
            table_key, _, _ = self.hash_table[index]
            if table_key == key:
                self.hash_table[index] = (key, hash(key), value)
                return
            index = (index + 1) % self.capacity

        self.length += 1
        self.hash_table[index] = (key, hash(key), value)
        self.resize()

    def __getitem__(self, key: Hashable) -> Any:
        index = self.count_index(key)

        while self.hash_table[index]:
            table_key, _, value = self.hash_table[index]
            if table_key == key:
                return value
            index = (index + 1) % self.capacity

        raise KeyError

    def __len__(self) -> int:
        return self.length

    def resize(self) -> None:
        threshold = self.capacity * self.LOAD_FACTOR

        if self.length <= threshold:
            return

        self.capacity *= 2
        old_dictionary = self.hash_table

        self.hash_table = [None] * self.capacity
        self.length = 0

        for element in old_dictionary:
            if element:
                key, _, value = element
                self.__setitem__(key, value)

    def count_index(self, new_key: Hashable) -> int:
        return hash(new_key) % self.capacity
