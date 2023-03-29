from typing import Any


class Dictionary:

    def __init__(self) -> None:
        self.capacity: int = 8
        self.current_table = [[] for _ in range(self.capacity)]
        self.taken_columns: int = 0

    def __setitem__(self, key: Any, value: Any) -> None:
        index_ = hash(key) % self.capacity
        while True:
            if not self.current_table[index_]:
                self.current_table[index_] = [key, value]
                self.taken_columns += 1
                break
            elif self.current_table[index_][0] == key:
                self.current_table[index_][1] = value
                break
            else:
                index_ = (index_ + 1) % self.capacity
        if self.taken_columns > self.capacity * 2 / 3:
            self.resize()

    def __getitem__(self, key: Any) -> Any:
        index_ = hash(key) % self.capacity
        for _ in self.current_table:
            if self.current_table[index_] and \
                    self.current_table[index_][0] == key:
                return self.current_table[index_][1]
            else:
                index_ = (index_ + 1) % self.capacity
        raise KeyError(f"Key: {key} is not in dictionary")

    def __len__(self) -> int:
        return self.taken_columns

    def resize(self) -> None:
        self.taken_columns = 0
        self.capacity *= 2
        recent_table = self.current_table
        self.current_table = [[] for _ in range(self.capacity)]
        for items in recent_table:
            if items:
                self[items[0]] = items[1]
