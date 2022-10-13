from typing import Any, Hashable


class Dictionary:
    def __init__(self) -> None:
        self.size = 0
        self._capacity = 8
        self.threshold = int(self._capacity / 3 * 2)
        self.hash_table = [[None, None, None]] * self._capacity

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if isinstance(key, (dict, set, list)):
            raise TypeError(f"unhashable type: '{type(key)}'")

        index = hash(key) % self._capacity
        while True:

            if self.hash_table[index][2] is None:
                self.size += 1
                self.hash_table[index] = [key, value, hash(key)]
                if self.size > self.threshold:
                    self._resize()
                break

            if self.hash_table[index][0] == key:
                self.hash_table[index] = [key, value, hash(key)]
                break

            index += 1
            if index == self._capacity:
                index = 0

    def __getitem__(self, item: Hashable) -> Any:
        if isinstance(item, (dict, set, list)):
            raise TypeError(f"unhashable type: '{type(item)}'")

        index = hash(item) % self._capacity
        start = index
        if not self.hash_table[index][0]:
            raise KeyError(f"there is no such key {item}")

        while self.hash_table[index][0] != item:
            index += 1
            if index == self._capacity:
                index = 0
            if index == start:
                raise KeyError(f"there is no such key {item}")

        return self.hash_table[index][1]

    def __len__(self) -> int:
        return self.size

    def _resize(self) -> None:
        self._capacity *= 2
        self.threshold = int(self._capacity / 3 * 2)

        new = [[None, None, None]] * self._capacity

        for element in self.hash_table:
            if element[2] is None:
                continue
            index = hash(element[0]) % self._capacity

            while new[index][2] is not None:
                index += 1
                if index == self._capacity:
                    index = 0

            new[index] = [element[0], element[1], hash(element[0])]
        self.hash_table = new
