from typing import Any


class Dictionary:

    def __init__(self, initial_capacity: int = 10) -> None:
        self.capacity = initial_capacity
        self.size = 0
        self.table = [None] * initial_capacity

    def __setitem__(self, key: Any, value: Any) -> None:
        index = hash(key) % self.capacity
        if self.table[index] is None:
            self.table[index] = []
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                self.table[index][i] = (key, value)
                break
        else:
            self.table[index].append((key, value))
            self.size += 1

    def __getitem__(self, key: Any) -> Any:
        index = hash(key) % self.capacity
        if self.table[index] is not None:
            for i in self.table[index]:
                if i[0] == key:
                    return i[1]
        raise KeyError

    def __len__(self) -> int:
        return self.size
