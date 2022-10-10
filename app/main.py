from typing import Hashable, Any


class Dictionary:
    def __init__(self) -> None:
        self.size = 0
        self.capacity = 8
        self.threshold = int(self.capacity * 0.666)
        self.hash_table = [None for _ in range(self.capacity)]

    def resize(self) -> None:
        old_hash_table = self.hash_table
        self.size = 0
        self.capacity *= 2
        self.threshold = int(self.capacity * 0.666)
        self.hash_table = [None for _ in range(self.capacity)]
        for el in old_hash_table:
            if el:
                self.__setitem__(el[1], el[2])

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.size == self.threshold:
            self.resize()

        hash_key = hash(key)
        hash_index = hash_key % self.capacity

        while True:
            if not self.hash_table[hash_index]:
                self.hash_table[hash_index] = [hash_key, key, value]
                self.size += 1
                break
            if self.hash_table[hash_index][0] == hash_key and \
                    self.hash_table[hash_index][1] == key:
                self.hash_table[hash_index][2] = value
                break
            hash_index = (hash_index + 1) % self.capacity

    def __getitem__(self, key: Hashable) -> Any:
        for el in self.hash_table:
            if el and el[1] == key:
                return el[2]
        raise KeyError(key)

    def __len__(self) -> int:
        return self.size
