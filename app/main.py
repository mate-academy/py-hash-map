from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.length: int = 0
        self.capacity: int = 8
        self.load_factor: float = 0.66
        self.hash_table: list = [None] * self.capacity

    def __add_to_hash_table(self, key_hash: int, key: Any, value: Any) -> None:
        _index = key_hash % self.capacity
        while True:
            if not self.hash_table[_index]:
                self.hash_table[_index] = (key_hash, key, value)
                self.length += 1
                break
            elif self.hash_table[_index][1] == key:
                self.hash_table[_index] = (key_hash, key, value)
                break
            _index += 1
            if _index == len(self.hash_table):
                _index = 0

    def __resize_hash_table(self) -> None:
        temp_list = self.hash_table
        self.capacity *= 2
        self.length = 0
        self.hash_table = [None] * self.capacity
        for item in temp_list:
            if item:
                self.__add_to_hash_table(*item)

    def __setitem__(self, key: Any, value: Any) -> None:
        if self.length == int(self.capacity * self.load_factor):
            self.__resize_hash_table()
        key_hash = hash(key)
        self.__add_to_hash_table(key_hash, key, value)

    def __getitem__(self, key: Any) -> Any:
        key_hash = hash(key)
        key_index = key_hash % self.capacity
        if self.hash_table[key_index]:
            if self.hash_table[key_index][1] == key:
                return self.hash_table[key_index][2]
            elif self.hash_table[key_index][1] != key:
                for item in self.hash_table:
                    if item and item[1] == key:
                        return item[2]
        raise KeyError(f"No key: {key} in dictionary")

    def __len__(self) -> int:
        return self.length
