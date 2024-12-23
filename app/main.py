from typing import Any


class Dictionary:
    class Node:
        def __init__(self, key: Any, value: Any) -> None:
            self.key = key
            self.hash = hash(key)
            self.value = value

        def __repr__(self) -> str:
            return f"({self.key}, {self.hash}, {self.value})"

    def __init__(self,
                 initial_capacity: int = 8,
                 load_factor: float = 2 / 3) -> None:
        self.capacity = initial_capacity
        self.load_factor = load_factor
        self.table = [None] * initial_capacity
        self.size = 0

    def index(self, key: Any) -> int:
        return hash(key) % self.capacity

    def resize(self) -> None:
        old_table = self.table
        self.capacity = self.capacity * 2
        self.table = [None] * self.capacity
        self.size = 0

        for node in old_table:
            if node is not None:
                self.__setitem__(node.key, node.value)

    def __setitem__(self, key: Any, value: Any) -> None:
        if (self.size + 1) / self.capacity > self.load_factor:
            self.resize()

        index = self.index(key)

        while self.table[index] is not None:
            if self.table[index].key == key:
                self.table[index].value = value
                return

            index = (index + 1) % self.capacity

        self.table[index] = self.Node(key, value)
        self.size += 1

        print(self.table)

    def __getitem__(self, key: Any) -> Any:
        index = self.index(key)

        while self.table[index] is not None:
            if self.table[index].key == key:
                return self.table[index].value
            index = (index + 1) % self.capacity

        raise KeyError(f"Key {key} not found.")

    def __len__(self) -> int:
        return self.size
