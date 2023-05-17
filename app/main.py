from typing import Hashable, Any


class Dictionary:
    def __init__(self) -> None:
        self.initial_capacity = 8
        self.load_factor = 0.6
        self.hash_table = [None] * self.initial_capacity
        self.size = 0

    def resize(self) -> None:
        nodes = [key_and_value for key_and_value in self.hash_table if key_and_value is not None]
        self.initial_capacity *= 2
        self.hash_table = [None] * self.initial_capacity
        self.size = 0
        [self.__setitem__(node[0], node[-1]) for node in nodes]

    def __setitem__(self, key: Hashable, value: Hashable) -> None:
        index = hash(key) % self.initial_capacity
        while self.hash_table[index] is not None:
            if self.hash_table[index][0] == key:
                self.hash_table[index][-1] = value
                break
            index = (index + 1) % self.initial_capacity
        else:
            self.hash_table[index] = [key, value]
            self.size += 1
            if self.size > int(self.initial_capacity * self.load_factor):
                self.resize()

    def __getitem__(self, key: Hashable) -> Any:
        index = hash(key) % self.initial_capacity
        while self.hash_table[index] is not None:
            if self.hash_table[index][0] == key:
                return self.hash_table[index][-1]
            index = (index + 1) % self.initial_capacity
        raise KeyError

    def __len__(self) -> int:
        return self.size

    def clear(self) -> None:
        self.initial_capacity = 8
        self.hash_table = [None] * self.initial_capacity
        self.size = 0

    def __delitem__(self, key: Hashable):
        index = hash(key) % self.initial_capacity
        while self.hash_table[index] is not None:
            if self.hash_table[index][0] == key:
                self.hash_table[index] = None
                self.size -= 1
            break
