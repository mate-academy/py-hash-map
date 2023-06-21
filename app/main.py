import random
from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.__size = 0
        self.__capacity = 8
        self.__table = [None] * self.__capacity
        self.__universal_a = random.randint(1, self.__capacity - 1)
        self.__universal_b = random.randint(0, self.__capacity - 1)

    def __shift_hash_value(self, hash_value: int, probe: int, key: Any) -> int:
        return (hash_value + probe**2) % self.__capacity

    def __universal_hash(self, key: Any) -> int:
        return (
            (self.__universal_a * hash(key) + self.__universal_b)
            % self.__capacity
        ) % self.__capacity

    def insert(self, key: Any, value: Any) -> None:
        if self.__load_factor() >= 2 / 3:
            self.__expand()
        hash_value = self.__universal_hash(key)
        probe = 1
        while self.__table[hash_value] is not None:
            if self.__table[hash_value][0] == key:
                self.__table[hash_value] = (key, value)
                return
            hash_value = self.__shift_hash_value(hash_value, probe, key)
            probe += 1
        self.__table[hash_value] = (key, value)
        self.__size += 1

    def get(self, key: Any) -> Any:
        hash_value = self.__universal_hash(key)
        probe = 1
        while self.__table[hash_value] is not None:
            if self.__table[hash_value][0] == key:
                return self.__table[hash_value][1]
            hash_value = self.__shift_hash_value(hash_value, probe, key)
            probe += 1
        raise KeyError("Key not found")

    def __expand(self) -> None:
        self.__capacity *= 2
        new_table = [None] * self.__capacity
        for item in self.__table:
            if item is not None:
                key, value = item
                hash_value = self.__universal_hash(key)
                probe = 1
                while new_table[hash_value] is not None:
                    hash_value = self.__shift_hash_value(
                        hash_value, probe, key
                    )
                    probe += 1
                new_table[hash_value] = (key, value)
        self.__table = new_table

    def __load_factor(self) -> float:
        return self.__size / self.__capacity

    def contains(self, key: Any) -> bool:
        return self.get(key) is not None

    def remove(self, key: Any) -> None:
        hash_value = self.__universal_hash(key)
        probe = 1
        while self.__table[hash_value] is not None:
            if self.__table[hash_value][0] == key:
                self.__table[hash_value] = None
                self.__size -= 1
                return
            hash_value = self.__shift_hash_value(hash_value, probe, key)
            probe += 1

    def __contains__(self, key: Any) -> bool:
        return self.contains(key)

    def __getitem__(self, key: Any) -> Any:
        return self.get(key)

    def __setitem__(self, key: Any, value: Any) -> None:
        self.insert(key, value)

    def __delitem__(self, key: Any) -> None:
        self.remove(key)

    def __len__(self) -> int:
        return self.__size
