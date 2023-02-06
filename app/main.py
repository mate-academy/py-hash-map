from typing import Callable


class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.load_factor = 2 / 3
        self.resize = 2
        self.hash_table = [None] * self.capacity

    def __setitem__(self, key: Callable, value: Callable) -> None:
        index = hash(key) % self.capacity
        while self.hash_table[index] is not None:
            if self.hash_table[index][0] == key:
                self.hash_table[index] = (key, value)
                break
            index = (index + 1) % self.capacity
        self.hash_table[index] = (key, value)
        if len(self) > self.load_factor * self.capacity:
            self.capacity *= self.resize
            old_hash_table = self.hash_table
            self.hash_table = [None] * self.capacity
            for item in old_hash_table:
                if item is not None:
                    key, value = item
                    self.__setitem__(key, value)

    def __getitem__(self, key: Callable) -> Callable:
        index = hash(key) % self.capacity
        while self.hash_table[index] is not None:
            current_key, value = self.hash_table[index]
            if current_key == key:
                return value
            index = (index + 1) % self.capacity
        raise KeyError

    def __len__(self) -> int:
        length = 0
        for item in self.hash_table:
            if item is not None:
                length += 1
        return length
