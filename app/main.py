from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.capacity = 8
        self.hash_table = [None] * self.capacity

    def __setitem__(self, key: Any, value: Any) -> None:
        index = hash(key) % self.capacity
        if self.length >= round(self.capacity * 2 / 3) - 1:
            self.length = 0
            self.capacity *= 2
            hash_table = self.hash_table[:]
            self.hash_table = [None] * self.capacity
            for node in hash_table:
                if node:
                    self[node[0]] = node[2]
        if self.hash_table[index] is None:
            self.length += 1
            self.hash_table[index] = [key, hash(key), value]
        else:
            while True:
                if self.hash_table[index] is None:
                    self.length += 1
                    self.hash_table[index] = [key, hash(key), value]
                    break
                if self.hash_table[index][0] == key:
                    self.hash_table[index][2] = value
                    break
                index = index + 1
                index = index % self.capacity

    def __getitem__(self, key: Any) -> Any:
        index = hash(key) % self.capacity
        if self.hash_table[index] and self.hash_table[index][0] == key:
            return self.hash_table[index][2]
        else:
            for i in range(self.capacity + 1):
                index = index + 1
                index = index % self.capacity
                if self.hash_table[index]:
                    if self.hash_table[index][0] == key:
                        return self.hash_table[index][2]
            raise KeyError

    def __len__(self) -> int:
        return self.length
