from typing import Any


class Dictionary:

    def __init__(self, capacity: int = 8, length: int = 0) -> None:
        self.capacity = capacity
        self.hash_table = [[] for _ in range(self.capacity)]
        self.load_factor = int(2 / 3 * self.capacity)
        self.length = length

    def resize_dict(self) -> None:
        hash_table_copy = self.hash_table
        self.length = 0
        self.capacity *= 2
        self.load_factor = int(2 / 3 * self.capacity)
        self.hash_table = [[] for _ in range(self.capacity)]

        for ind in hash_table_copy:
            if len(ind) != 0:
                self.__setitem__(ind[0], ind[1])

    def __setitem__(self, key: Any, value: Any) -> None:
        if isinstance(key, list | set):
            raise KeyError(f"Opps, key {key} must be immutable :(")

        if self.length == self.load_factor:
            self.resize_dict()

        hash_key = hash(key)
        index = hash_key % self.capacity

        if len(self.hash_table[index]) == 0:
            self.hash_table[index] = [key, value, index]
            self.length += 1

        else:
            while True:
                if key == self.hash_table[index][0] and \
                        hash_key == self.hash_table[index][2]:
                    self.hash_table[index][1] = value
                    break
                index = (index + 1) % self.capacity

    def __getitem__(self, key: Any) -> Any:
        hash_key = hash(key)
        index = hash_key % self.capacity

        if len(self.hash_table[index]) == 0:
            raise KeyError(f"Opps, key {key} does not exist :(")

        else:
            while True:
                if key == self.hash_table[index][0] and \
                        hash_key == self.hash_table[index][2]:
                    return self.hash_table[index][1]
                index = (index + 1) % self.capacity

    def __len__(self) -> int:
        return self.length
