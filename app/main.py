from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.hash_table = [[] for _ in range(8)]
        self.current_size = 0

    def __setitem__(self, key: Any, value: Any) -> None:

        capacity = len(self.hash_table)
        threshold = int(0.66 * capacity)

        if self.current_size + 1 > threshold:
            old_hash_table = self.hash_table
            self.hash_table = [[] for _ in range(capacity * 2)]
            capacity = len(self.hash_table)
            self.current_size = 0
            self.update(old_hash_table)

        index = hash(key) % capacity
        for i, el in enumerate(self.hash_table):
            if el and el[0] == key and el[1] == hash(key):
                self.hash_table[i][2] = value
                break
        else:
            while True:
                if not self.hash_table[index]:
                    self.hash_table[index] = [key, hash(key), value]
                    self.current_size += 1
                    break
                index = (index + 1) % capacity

    def __getitem__(self, item: Any) -> Any:
        for el in self.hash_table:
            if el and el[0] == item and el[1] == hash(item):
                return el[2]
        raise KeyError(item)

    def __len__(self) -> int:
        return self.current_size

    def clear(self) -> None:
        self.hash_table = [[] for _ in range(len(self.hash_table))]

    def __delitem__(self, key: Any) -> None:
        for el in self.hash_table:
            if el and el[0] == key and el[1] == hash(key):
                return el[2]
        raise KeyError(key)

    def get(self, key: Any, default_value: Any = "some value") -> Any:
        try:
            self.__getitem__(key)
        except KeyError:
            return default_value

    def pop(self, key: Any) -> Any:
        value = self.__getitem__(key)
        return [key, value]

    def update(self, other: list[tuple] | list[list]) -> None:
        try:
            for key, value in other:
                self.__setitem__(key, value)
        except ValueError:
            for el in other:
                if el:
                    self.__setitem__(el[0], el[2])

    def __iter__(self) -> object:
        self.current_element = 0
        return self

    def __next__(self) -> Any:
        if self.current_element >= self.current_size:
            raise StopIteration

        result = self.hash_table[self.current_element][0]
        self.current_element += 1
        return result
