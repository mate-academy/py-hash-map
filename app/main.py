from typing import Any, Hashable


class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.hash_table: list = [None] * 8
        self.load_factor = 2 / 3

    def __setitem__(self, key: Hashable, value: Any) -> None:
        hashed_key = hash(key)
        index = hashed_key % len(self.hash_table)
        while True:
            if not self.hash_table[index]:
                if (self.length + 1 > self.load_factor
                        * len(self.hash_table)):
                    self.resize()
                    index = hashed_key % len(self.hash_table)
                    continue
                self.length += 1
                self.hash_table[index] = (key, hashed_key, value)
                break
            elif self.hash_table[index][0] == key:
                self.hash_table[index] = (key, hashed_key, value)
                break
            index = (index + 1) % len(self.hash_table)

    def __getitem__(self, key: Hashable) -> Any:
        index = hash(key) % len(self.hash_table)
        counter = 0
        while counter < len(self):
            if (self.hash_table[index]
                    and self.hash_table[index][0] == key):
                return self.hash_table[index][2]
            index = (index + 1) % len(self.hash_table)
            counter += 1
        raise KeyError

    def __len__(self) -> int:
        return self.length

    def resize(self) -> None:
        table = self.hash_table
        self.hash_table = [None] * len(self.hash_table) * 2
        self.length = 0
        [self.__setitem__(bucket[0], bucket[2]) for bucket in table if bucket]
