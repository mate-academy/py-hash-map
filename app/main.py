from typing import Any


class Dictionary:
    def __init__(self, **kwargs) -> None:
        self.hash_table = [-1] * 8
        self.dictionary = []
        self.length = 0
        for key, value in kwargs.items():
            self.__setitem__(key, value)

    def __setitem__(self, key: Any, value: Any) -> None:
        if isinstance(key, list | dict | set):
            raise TypeError(f"<{key}> cannot be a dictionary key")

        if len(self.dictionary) >= int(self.get_load_factor()):
            self.resize()

        hash_code = hash(key)
        hash_index, dict_index = self.set_index(hash_code, key)
        if dict_index == -1:
            self.hash_table[hash_index] = len(self.dictionary)
            self.dictionary.append((hash_code, key, value))
            self.length += 1
        else:
            self.dictionary[dict_index] = (hash_code, key, value)

    def set_index(self, hash_code: int, key: Any) -> (int, int):
        hash_i = hash_code % self.get_capacity()
        while self.hash_table[hash_i] != -1:
            if self.hash_table[hash_i] == -2:
                hash_i = hash_i + 1 if hash_i < self.get_capacity() - 1 else 0
                continue
            dict_i = self.hash_table[hash_i]
            if self.dictionary[dict_i][:2] == (hash_code, key):
                return hash_i, dict_i
            hash_i = hash_i + 1 if hash_i < self.get_capacity() - 1 else 0
        return hash_i, self.hash_table[hash_i]

    def resize(self) -> None:
        self.hash_table = [-1] * (self.get_capacity() * 2)
        i = 0
        while i < len(self.dictionary):
            if self.dictionary[i]:
                hash_code, key, _ = self.dictionary[i]
                hash_index, _ = self.set_index(hash_code, key)
                self.hash_table[hash_index] = i
                i += 1
            else:
                self.dictionary.pop(i)

    def get_load_factor(self) -> float:
        return self.get_capacity() * 2 / 3

    def get_capacity(self) -> int:
        return len(self.hash_table)
