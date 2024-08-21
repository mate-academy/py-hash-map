from typing import Any


class Dictionary:

    def __init__(self) -> None:
        self.length = 0
        self.hash_table = [None] * 8
        self.length_hash_table = 8

    def update(self) -> None:
        self.length_hash_table *= 2
        index = 0
        old_hash = self.hash_table
        self.hash_table = [None] * self.length_hash_table

        for data in old_hash:
            print("Data", data)

            if data is not None:
                key, value = data[0], data[1]
                index = hash(key) % self.length_hash_table

                while True:
                    if self.hash_table[index] is None:
                        break
                    if index == self.length_hash_table - 1:
                        index = 0
                        continue
                    index += 1

                self.hash_table[index] = [key, value, hash(key)]

    def __setitem__(self, key: Any, value: Any) -> None:

        if self.length > self.length_hash_table * 2 / 3:
            self.update()

        index = hash(key) % self.length_hash_table

        while True:
            if ((self.hash_table[index] is None)
                    or (self.hash_table[index][0] == key)):
                break
            if index == self.length_hash_table - 1:
                index = 0
                continue
            index += 1
        try:
            if self.hash_table[index][0] != key:
                self.length += 1
        except Exception:
            self.length += 1

        self.hash_table[index] = [key, value, hash(key)]

    def __getitem__(self, key: Any) -> Any:
        index = hash(key) % self.length_hash_table
        try:
            while True:
                if self.hash_table[index][0] == key:
                    break
                if index == self.length_hash_table - 1:
                    index = 0
                    continue
                index += 1

            return self.hash_table[index][1]

        except Exception:
            raise KeyError

    def __len__(self) -> int:
        return self.length
