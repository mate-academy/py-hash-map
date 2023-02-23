from typing import Any

import hashable as hashable


class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.hash_table: list = [None] * 8
        self.hash_capacity = 8

    def __len__(self) -> int:
        return self.length

    def __setitem__(self, key: hashable, value: Any) -> None:
        if self.length < round(self.hash_capacity * 2 / 3):
            index = hash(key) % self.hash_capacity
            if self.hash_table[index] is None:
                self.hash_table[index] = (key, value, hash(key))
                self.length += 1
            elif self.hash_table[index][0] == key:
                self.hash_table[index] = (key, value, hash(key))
            else:
                for i in range(len(self.hash_table)):
                    if self.hash_table[i] is None:
                        self.hash_table[i] = (key, value, hash(key))
                        self.length += 1
                        break
                    elif self.hash_table[i][0] == key:
                        self.hash_table[i] = (key, value, hash(key))
                        break
        else:
            self.resize()
            self[key] = value

    def resize(self) -> None:
        self.hash_capacity *= 2
        hash_table = self.hash_table.copy()
        self.hash_table = [None] * self.hash_capacity
        self.length = 0
        for place in hash_table:
            if place:
                self[place[0]] = place[1]

    def __getitem__(self, key: hashable) -> Any:
        index = hash(key) % self.hash_capacity
        if self.hash_table[index] is None:
            raise KeyError(f"There is no element with this key: {key}")
        elif self.hash_table[index][0] == key:
            return self.hash_table[index][1]
        else:
            for i in range(len(self.hash_table)):
                if self.hash_table[i] and self.hash_table[i][0] == key:
                    return self.hash_table[i][1]
            raise KeyError(f"There is no element with this key: {key}")

    def clear(self) -> None:
        self.hash_table = [None] * 8
        self.length = 0

    def __delitem__(self, key: hashable) -> None:
        if self[key]:
            index = hash(key) % self.hash_capacity
            if self.hash_table[index][0] == key:
                self.hash_table[index] = None
            else:
                for i in range(len(self.hash_table)):
                    if self.hash_table[i] and self.hash_table[i][0] == key:
                        self.hash_table[i] = None
        else:
            raise KeyError(f"Wrong key: {key}")

    def get(self, key: hashable) -> Any:
        try:
            return self[key]
        except KeyError:
            return

    def pop(self, key: hashable, *args: str) -> Any:
        try:
            return self[key]
        except KeyError:
            if not args:
                raise
            else:
                default, = args
                return default

    def update(self, key: hashable, value: Any) -> None:
        self[key] = value

    def __iter__(self) -> hashable:
        for el in self.hash_table:
            if el:
                yield el[0]
