from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.size = 0
        self.threshold = int(self.capacity * 2 / 3)
        self.hash_table = [None for _ in range(self.capacity)]

    def __setitem__(self, key: Any, value: Any) -> None:
        if self.size == self.threshold:
            self.resize()
        hash_ = hash(key)
        index_ = hash_ % self.capacity
        if self.hash_table[index_] is None:
            self.hash_table[index_] = (key, hash_, value)
            self.size += 1
            return
        if self.hash_table[index_][0] == key:
            self.hash_table[index_] = (key, hash_, value)
            return
        for _ in range(self.capacity):
            index_ = (index_ + 1) % self.capacity
            if self.hash_table[index_] is None:
                self.hash_table[index_] = (key, hash_, value)
                self.size += 1
                return
            if self.hash_table[index_][0] == key:
                self.hash_table[index_] = (key, hash_, value)
                return

    def __getitem__(self, key: Any) -> Any:
        hash_ = hash(key)
        index_ = hash_ % self.capacity
        for _ in range(self.capacity):
            if self.hash_table[index_] is None:
                raise KeyError
            if self.hash_table[index_][0] == key:
                return self.hash_table[index_][2]
            index_ = (index_ + 1) % self.capacity
        raise KeyError

    def __len__(self) -> int:
        return self.size

    def resize(self) -> None:
        self.capacity *= 2
        self.size = 0
        self.threshold = int(self.capacity * 2 / 3)
        old_table = self.hash_table.copy()
        self.hash_table = [None for _ in range(self.capacity)]
        for tuple_ in old_table:
            if tuple_ is not None:
                self.__setitem__(tuple_[0], tuple_[2])
