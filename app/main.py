from typing import Any


class Dictionary:

    def __init__(self) -> None:
        self.capacity = 8
        self.load_factor = 0.66
        self.hash_table = [None] * self.capacity

    def __setitem__(self, key: Any, value: Any) -> None:
        if self.hash_table.count(None) < int(self.capacity * self.load_factor):
            self.resize()
        index = self.get_index(key)
        while True:
            if not self.hash_table[index]:
                self.hash_table[index] = (key, hash(key), value)
                break
            else:
                if self.hash_table[index][0] == key:
                    self.hash_table[index] = (key, hash(key), value)
                    break
                index = index + 1 if index < self.capacity - 1 else 0

    def __getitem__(self, item: Any) -> Any:
        index = self.get_index(item)
        cnt = 0
        while cnt < self.capacity:
            if self.hash_table[index]:
                if self.hash_table[index][0] == item:
                    return self.hash_table[index][2]
            index = index + 1 if index < self.capacity - 1 else 0
            cnt += 1
        raise KeyError

    def resize(self) -> None:
        old_table = self.hash_table
        self.capacity *= 2
        self.hash_table = [None] * self.capacity
        for item in old_table:
            if item:
                self.__setitem__(item[0], item[2])

    def __len__(self) -> int:
        return self.capacity - self.hash_table.count(None)

    def get_index(self, key: Any) -> int:
        return hash(key) % self.capacity
