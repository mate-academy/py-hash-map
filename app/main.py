from typing import Any, Hashable


BASE_CAPACITY = 8


class Dictionary:

    def __init__(self) -> None:
        self.__capacity = BASE_CAPACITY
        self.__load_factor = 2 / 3
        self.__hash_table = [None] * self.__capacity
        self.__count = 0

    def __setitem__(self, key: Hashable, value: Any) -> None:
        index = self.calculate_index(key)
        if not self.__hash_table[index]:
            self.__count += 1
            if self.__count >= int(self.__capacity * self.__load_factor):
                self.resize_and_rehash()
                index = self.calculate_index(key)
        self.__hash_table[index] = (key, hash(key), value)

    def __getitem__(self, key: Hashable) -> Any:
        index = self.calculate_index(key)

        if not self.__hash_table[index]:
            raise KeyError(f"Key {key} is not in dict")

        return self.__hash_table[index][2]

    def __len__(self) -> int:
        return self.__count

    def clear(self) -> None:
        self.__hash_table = [None] * self.__capacity

    def __delitem__(self, key: Hashable) -> None:
        index = self.calculate_index(key)
        if not self.__hash_table[index]:
            raise KeyError
        self.__hash_table[index] = (key, hash(key), None)

    def get(self, key: Hashable) -> Any:
        return self.__getitem__(key)

    def pop(self, key: Hashable) -> None:
        index = self.calculate_index(key)
        if not self.__hash_table[index]:
            raise KeyError(f"Key {key} is not in dict")
        self.__hash_table[index] = None

    def update(self, key: Hashable, value: Any) -> None:
        self.__setitem__(key, value)

    def resize_and_rehash(self) -> None:
        self.__capacity *= 2
        old_hash_table = self.__hash_table
        self.clear()
        for item in old_hash_table:
            if item:
                self.__hash_table[self.calculate_index(item[0])] = item

    def calculate_index(self, key: Hashable) -> int:
        index = hash(key) % self.__capacity
        while self.__hash_table[index] and self.__hash_table[index][0] != key:
            index = (index + 1) % self.__capacity
        return index
