from typing import Hashable, Any


class Dictionary:
    def __init__(self) -> None:
        self.__capacity = 8
        self.__length = 0
        self.__threshold = int(self.__capacity * 2 / 3)
        self.__hash_table: list[Any] = [None] * self.__capacity

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if not isinstance(key, Hashable):
            raise KeyError("Key must be hashable")

        index = self.__find_available_slot_index(key)

        if not self.__hash_table[index]:
            if self.__length >= self.__threshold:
                self.__resize()
                index = self.__find_available_slot_index(key)

            self.__length += 1

        self.__hash_table[index] = (key, hash(key), value)

    def __getitem__(self, key: Hashable) -> Any:
        index = self.__find_available_slot_index(key)
        if not self.__hash_table[index]:
            raise KeyError(f"{key} is not found")
        return self.__hash_table[index][2]

    def __len__(self) -> int:
        return self.__length

    def __find_available_slot_index(self, key: Hashable) -> int:
        index = hash(key) % self.__capacity

        while self.__hash_table[index] and self.__hash_table[index][0] != key:
            index = (index + 1) % self.__capacity

        return index

    def __resize(self) -> None:
        self.__capacity *= 2
        old_hash_table = self.__hash_table
        self.__length = 0
        self.__threshold = int(self.__capacity * 2 / 3)
        self.__hash_table = [None] * self.__capacity

        for element in old_hash_table:
            if element is not None:
                self[element[0]] = element[2]
