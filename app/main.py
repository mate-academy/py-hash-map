from typing import Any


class HashTable:
    def __init__(self, key: Any, value: any, hash_num: int) -> None:
        self.key = key
        self.value = value
        self.hash_num = hash_num


class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.size = 0
        self.table = [None] * self.capacity
        self.load_factor = 0.75

    def __str__(self) -> str:
        return f"{self.table}"

    def __setitem__(self, key: Any, value: Any) -> None:
        if not hash(key):
            raise TypeError("Dictionary key must be immutable")

        index = self.get_index(key)

        while self.table[index] is not None:
            if self.table[index].key == key:
                self.table[index].value = value
                return
            index = (index + 1) % self.capacity

        self.table[index] = HashTable(key, value, hash(key))
        self.size += 1
        if self.size / self.capacity >= self.load_factor:
            self.resize()

    def __getitem__(self, key: Any) -> Any:
        index = self.get_index(key)
        index = self.find_index(index, key)

        if index is None:
            raise KeyError(f"Requested key '{key}' "
                           f"is not found in a dictionary")

        return self.table[index].value

    def __len__(self) -> int:
        return self.size

    def __delitem__(self, key: Any) -> None:
        index = self.get_index(key)
        self.find_index(index, key)

        if index:
            self.table[index] = None
            self.size -= 1
            self.rehash()
        else:
            raise KeyError("Сan`t delete a key that "
                           "does not exist in a dictionary")

    def get_index(self, key: Any) -> int:
        return hash(key) % self.capacity

    def find_index(self, index: int, key: Any) -> int | None:
        while self.table[index] is not None:
            if self.table[index].key == key:
                return index
            index = (index + 1) % self.capacity
        return None

    def resize(self) -> None:
        old_table = self.table[:]
        self.capacity *= 2
        self.table = [None] * self.capacity
        self.size = 0

        for node in old_table:
            if node is not None:
                self.__setitem__(node.key, node.value)

    def rehash(self) -> None:
        old_table = self.table[:]
        self.table = [None] * self.capacity
        self.size = 0

        for node in old_table:
            if node is not None:
                self.__setitem__(node.key, node.value)

    def __iter__(self) -> list:
        return [node.key for node in self.table if node is not None]

    def update(self, other: Any) -> None:
        if hasattr(other, "items"):
            items = other.items()
        else:
            items = other

        try:
            for key, value in items:
                self.__setitem__(key, value)
        except TypeError:
            raise ValueError("The input must be a dictionary "
                             "or an iterable of key-value pairs")

    def pop(self, key: Any) -> Any:
        index = self.get_index(key)
        self.find_index(index, key)

        if index:
            value = self.table[index].value
            self.table[index] = None
            self.size -= 1
            self.rehash()
            return value

        raise KeyError(f"Requested key '{key}' is not found in a dictionary")

    def clear(self) -> None:
        self.table = [None] * self.capacity
