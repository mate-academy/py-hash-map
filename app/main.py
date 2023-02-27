from typing import Any
from copy import deepcopy


class Dictionary:
    def __init__(self, load_factor: float = 0.75, capacity: int = 8) -> None:
        self.size = 0
        self.capacity = capacity
        self.load_factor = load_factor
        self.table = [[] for _ in range(self.capacity)]

    def __setitem__(self, key: Any, value: Any) -> None:
        hashed = hash(key)
        threshold = int(self.capacity * self.load_factor)
        if self.size == threshold:
            self.resize()
        index = hashed % self.capacity
        while True:
            if not self.table[index]:
                self.table[index] = [key, value, hashed]
                self.size += 1
                return
            if key == self.table[index][0]:
                if hashed == self.table[index][2]:
                    self.table[index][1] = value
                    return
            index = (index + 1) % self.capacity

    def __getitem__(self, key: Any) -> object:
        hashed = hash(key)
        index = hashed % self.capacity
        while self.table[index]:
            if self.table[index][0] == key:
                if self.table[index][2] == hashed:
                    return self.table[index][1]
            index = (index + 1) % self.capacity
        raise KeyError

    def __len__(self) -> int:
        return self.size

    def resize(self) -> None:
        new_copy = deepcopy(self.table)
        self.size = 0
        self.capacity *= 2
        self.table = [[] for _ in range(self.capacity + 1)]
        for item in new_copy:
            if item:
                self.__setitem__(item[0], item[1])
