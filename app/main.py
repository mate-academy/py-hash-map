from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.hash_size = 8
        self.hash_table = [[] for _ in range(self.hash_size)]
        self.threshold = int(self.hash_size * 2 / 3)

    def resize_hash(self) -> None:
        old_hash_table = self.hash_table
        self.hash_size *= 2
        self.threshold = int(self.hash_size * 2 / 3)
        self.length = 0
        self.hash_table = [[] for _ in range(self.hash_size)]
        for item in old_hash_table:
            if item:
                self.__setitem__(item[0], item[2])

    def __setitem__(self, key: (str, int, tuple), value: Any) -> None:
        if self.length == self.threshold:
            self.resize_hash()
        key_hash = hash(key)
        index = key_hash % self.hash_size

        while True:
            if not self.hash_table[index]:
                self.hash_table[index] = [key, key_hash, value]
                self.length += 1
                return
            if self.hash_table[index][0] == key and \
                    self.hash_table[index][1] == key_hash:
                self.hash_table[index][2] = value
                return
            index = (index + 1) % self.hash_size

    def __getitem__(self, key: (str, int, tuple)) -> object:
        key_hash = hash(key)
        index = key_hash % self.hash_size
        while self.hash_table[index]:
            if self.hash_table[index][0] == key and \
                    self.hash_table[index][1] == key_hash:
                return self.hash_table[index][2]
            index = (index + 1) % self.hash_size
        raise KeyError(f"Key {key} does not exist")

    def __len__(self) -> int:
        return self.length

    def clear(self) -> None:
        self.hash_size = 8
        self.threshold = int(self.hash_size * 2 / 3)
        self.length = 0
        self.hash_table = [[] for _ in range(self.hash_size)]

    def __delitem__(self, key: (str, int, tuple)) -> None:
        key_hash = hash(key)
        index = key_hash % self.hash_size
        while self.hash_table[index]:
            if self.hash_table[index][0] == key and \
                    self.hash_table[index][1] == key_hash:
                self.hash_table[index] = []
                return
            index = (index + 1) % self.hash_size
        raise KeyError(f"Key {key} does not exist")
