from typing import Any, List, Tuple


class Dictionary:
    def __init__(
            self,
            initial_capacity: int = 8,
            load_factor: float = 0.67
    ) -> None:
        self.table: List[List[Tuple]] = [[] for _ in range(initial_capacity)]
        self.size: int = 0
        self.load_factor: float = load_factor
        self.threshold: int = int(initial_capacity * load_factor)

    def __setitem__(self, key: Any, value: Any) -> None:
        index = hash(key) % len(self.table)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                break
        else:
            self.table[index].append((key, value))
            self.size += 1
            if self.size > self.threshold:
                self.resize()

    def __getitem__(self, key: Any) -> Any:
        index = hash(key) % len(self.table)
        for k, v in self.table[index]:
            if k == key:
                return v
        raise KeyError(key)

    def __len__(self) -> int:
        return self.size

    def resize(self) -> None:
        new_table = [[] for _ in range(len(self.table) * 2)]
        for bucket in self.table:
            for key, value in bucket:
                index = hash(key) % len(new_table)
                new_table[index].append((key, value))
        self.table = new_table
        self.threshold = int(len(self.table) * self.load_factor)
