from typing import Hashable, Any


class Dictionary:
    def __init__(
            self,
            capacity: int = 8,
            load_factor: float = 2 / 3
    ) -> None:
        self.capacity = capacity
        self.load_factor = load_factor
        self.size = 0
        self.table = [None] * self.capacity

    def index_(self, key: Hashable) -> int:
        index = hash(key) % self.capacity
        while self.table[index] and self.table[index][1] != key:
            index += 1
            index %= self.capacity
        return index

    def __getitem__(self, key: Hashable) -> Any:
        index = self.index_(key)
        if not self.table[index]:
            raise KeyError(f"Key {key} is not in dictionary")
        return self.table[index][2]

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.size > self.capacity * self.load_factor:
            self.resize()

        index = self.index_(key)
        if not self.table[index]:
            self.size += 1
        self.table[index] = [hash(key), key, value]

    def __delitem__(self, key: Hashable) -> None:
        index = self.index_(key)
        if self.table[index]:
            self.table[index] = [None]
            self.size -= 1

    def resize(self) -> None:
        temp_table = self.table
        self.capacity *= 2
        self.table = [None] * self.capacity
        self.size = 0
        for element in temp_table:
            if element:
                self.__setitem__(element[1], element[2])

    def clear_(self) -> None:
        self.load_factor = 2 / 3
        self.capacity = 8
        self.size = 0
        self.table = [None] * self.capacity

    def __len__(self) -> int:
        return self.size

    def __iter__(self) -> None:
        for content in self.table:
            if content is not None:
                yield content[0], content[1]
