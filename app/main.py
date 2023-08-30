from typing import Hashable, Any


class Dictionary:

    COEFFICIENT_FOR_RESIZE = 2
    LOAD_FACTOR = 2 / 3

    def __init__(self) -> None:
        self.capacity = 8
        self.length = 0
        self.table = [None for _ in range(self.capacity)]

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.length == int(self.capacity * self.LOAD_FACTOR):
            self.resize()

        hash_value = hash(key)
        index = hash_value % self.capacity

        while self.table[index]:
            if key == self.table[index][0]:
                self.table[index] = [key, hash_value, value]
                return

            index += 1
            index %= self.capacity

        self.length += 1
        self.table[index] = [key, hash_value, value]

    def __getitem__(self, key: Hashable) -> Any:
        hash_value = hash(key)
        index = hash_value % self.capacity

        while self.table[index] is not None:
            set_key, hash_key, value = self.table[index]
            if set_key == key:
                return value

            index += 1
            index %= self.capacity

        raise KeyError(f"there is no key - {key}")

    def __len__(self) -> int:
        return self.length

    def resize(self) -> None:
        previous_table = self.table[:]
        self.length = 0
        self.capacity *= self.COEFFICIENT_FOR_RESIZE
        self.table = [None for _ in range(self.capacity)]

        for element in previous_table:
            if element is not None:
                self.__setitem__(element[0], element[2])
