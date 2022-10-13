from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.size = 0
        self._capacity = 8
        self.threshold = int(self._capacity / 3 * 2)
        self.value = [[None, None, None]] * self._capacity

    def __setitem__(self, key: Any, value: Any) -> None:
        if isinstance(key, (dict, set, list)):
            raise TypeError(f"unhashable type: '{type(key)}'")

        index = hash(key) % self._capacity
        while True:

            if self.value[index][2] is None:
                self.size += 1
                self.value[index] = [key, value, hash(key)]
                if self.size > self.threshold:
                    self._resize()
                break

            if self.value[index][0] == key:
                self.value[index] = [key, value, hash(key)]
                break

            index += 1
            if index == self._capacity:
                index = 0

    def __getitem__(self, item: Any) -> Any:
        if isinstance(item, (dict, set, list)):
            raise TypeError(f"unhashable type: '{type(item)}'")

        index = hash(item) % self._capacity
        start = index
        if not self.value[index][0]:
            raise KeyError(f"there is no such key {item}")

        while self.value[index][0] != item:
            index += 1
            if index == self._capacity:
                index = 0
            if index == start:
                raise KeyError(f"there is no such key {item}")

        return self.value[index][1]

    def __len__(self) -> int:
        return self.size

    def _resize(self) -> None:
        self._capacity *= 2
        self.threshold = int(self._capacity / 3 * 2)
        new = [[None, None, None]] * self._capacity
        for element in self.value:
            if element[2] is None:
                continue
            index = hash(element[0]) % self._capacity
            while new[index][2] is not None:
                index += 1
                if index == self._capacity:
                    index = 0

            new[index] = [element[0], element[1], hash(element[0])]
        self.value = new
