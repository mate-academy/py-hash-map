from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.capacity = 8
        self.load_factor = 2 / 3
        self.hash_table: list = [None] * self.capacity

    def __len__(self) -> int:
        return self.length

    def __setitem__(self, key: Any, value: Any) -> None:
        hash_key = hash(key) % self.capacity
        for _ in range(len(self.hash_table)):
            if self.hash_table[hash_key] is None:
                self.hash_table[hash_key] = [key, value]
                self.length += 1
                return
            if self.hash_table[hash_key] is not None:
                if self.hash_table[hash_key][0] == key:
                    self.hash_table[hash_key][1] = value
                    return

            if hash_key == len(self.hash_table) - 1:
                hash_key = -1
            hash_key += 1

        if None not in self.hash_table:
            self.hash_table.append([key, value])
            self.length += 1

    def __getitem__(self, input_key: Any) -> Any:
        for value in self.hash_table:
            if value is not None:
                if value[0] == input_key:
                    return value[1]
        raise KeyError

    def clear(self) -> None:
        for index in range(len(self.hash_table)):
            self.hash_table[index] = None

    def get(self, input_key: Any, message: str = "Not found") -> Any:
        for value in self.hash_table:
            if value is not None:
                if value[0] == input_key:
                    return value[1]
        print(message)

    def pop(self, input_key: Any) -> Any:
        for index in range(len(self.hash_table)):
            if self.hash_table[index] is not None:
                if self.hash_table[index][0] == input_key:
                    result = self.hash_table[index][1]
                    self.hash_table[index] = None
                    return result
        raise KeyError

    def update(self, dictionary: dict) -> None:
        for key, value in dictionary.items():
            self.__setitem__(key, value)

    def __delitem__(self, input_key: Any) -> None:
        for index in range(len(self.hash_table)):
            if self.hash_table[index] is not None:
                if self.hash_table[index][0] == input_key:
                    self.hash_table[index] = None
                    return
        raise KeyError

    def __iter__(self) -> None:
        return self
