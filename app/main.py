from typing import Hashable, Any


class Dictionary:
    def __init__(self) -> None:
        self.size = 8
        self.threshold = int(self.size * 2 / 3)
        self.hash_table = [None for _ in range(self.size)]

    def resize_table(self, old_hash_table: list) -> None:
        self.size *= 2
        self.threshold = int(self.size * 2 / 3)
        self.hash_table = [None for _ in range(self.size)]
        for data in old_hash_table:
            if data is not None:
                self.__setitem__(data[0], data[1])

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.__len__() == self.threshold:
            self.resize_table(self.hash_table)

        if isinstance(key, list | set | dict):
            raise TypeError("Key must be Hashable")

        key_hash = hash(key)
        table_index = key_hash % self.size
        if self.hash_table[table_index] is not None:
            for _ in range(self.size):
                if self.hash_table[table_index] is None:
                    self.hash_table[table_index] = [key, value, key_hash]
                    break
                if (self.hash_table[table_index][0] == key
                        and key_hash == self.hash_table[table_index][2]):
                    self.hash_table[table_index][1] = value
                    break
                table_index = (table_index + 1) % self.size
        self.hash_table[table_index] = [key, value, key_hash]

    def __getitem__(self, key: Hashable) -> Any:
        key_hash = hash(key)
        table_index = key_hash % self.size
        while True:
            if self.hash_table[table_index] is None:
                raise KeyError
            if key_hash == self.hash_table[table_index][2] and \
                    key == self.hash_table[table_index][0]:
                return self.hash_table[table_index][1]
            table_index = (table_index + 1) % self.size

    def __len__(self) -> int:
        length = 0
        for i in self.hash_table:
            if i is not None:
                length += 1
        return length
