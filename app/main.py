from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.threshold = int(self.capacity * (2 / 3))
        self.hash_table = [None for _ in range(self.capacity)]
        self.length = 0

    def __setitem__(self, key: Any, value: Any) -> None:
        if self.length >= self.threshold:
            self.resize()
        hash_key = hash(key) % self.capacity
        while True:
            if self.hash_table[hash_key] is None:
                self.hash_table[hash_key] = [key, value, hash_key]
                self.length += 1
                break
            if self.hash_table[hash_key][0] == key and \
                    self.hash_table[hash_key][2] == hash_key:
                self.hash_table[hash_key][1] = value
                break
            hash_key = (hash_key + 1) % self.capacity

    def __getitem__(self, key: Any) -> Any:
        hash_key = hash(key) % self.capacity
        while True:
            if not self.hash_table[hash_key]:
                raise KeyError
            if self.hash_table[hash_key][0] == key:
                return self.hash_table[hash_key][1]
            hash_key = (hash_key + 1) % self.capacity

    def __len__(self) -> int:
        return self.length

    def resize(self) -> None:
        old_hash_table = self.hash_table
        self.capacity *= 2
        self.threshold = int(self.capacity * (2 / 3))
        self.hash_table = [None for _ in range(self.capacity)]
        self.length = 0

        for key_value in old_hash_table:
            if key_value:
                self.__setitem__(key_value[0], key_value[1])
