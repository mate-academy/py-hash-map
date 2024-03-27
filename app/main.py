from typing import Any


class Dictionary:
    def __init__(self, initial_capacity: int = 8,
                 load_factor: int | float = 2 / 3,
                 resize: int = 2) -> None:
        self.items = [None] * initial_capacity
        self.count = 0
        self.capacity = initial_capacity
        self.load_factor = load_factor
        self.resize = resize

    def __setitem__(self, key: Any, value: Any) -> None:
        hash_value = hash(key)
        if self.count / self.capacity > self.load_factor:
            self.resizing()

        index = hash_value % self.capacity
        while self.items[index] and self.items[index][0] != key:
            index += 1
            index = 0 if index > self.capacity - 1 else index

        if not self.items[index]:
            self.count += 1
        self.items[index] = (key, hash_value, value)

    def __getitem__(self, key: Any) -> Any:
        hash_value = hash(key)
        index = hash_value % self.capacity

        while self.items[index]:
            if self.items[index][0] == key:
                return self.items[index][2]
            index = index + 1
            index = 0 if index > self.capacity - 1 else index

        raise KeyError(f"Key '{key}' not found")

    def __len__(self) -> int:
        return self.count

    def resizing(self) -> None:
        self.capacity *= self.resize
        temp = self.items
        self.items = [None] * self.capacity
        self.count = 0
        for item in temp:
            if item:
                self.__setitem__(item[0], item[2])

    def __repr__(self) -> str:
        return str({item[0]: item[2] for item in self.items if item})
