from typing import Any, Hashable


class Dictionary:
    def __init__(self) -> None:
        self._size = 0
        self._capacity = 8
        self._threshold = int(self._capacity / 3 * 2)
        self._hash_table = [[] for _ in range(self._capacity)]

    def __setitem__(self, key: Hashable, value: Any) -> None:
        hashed_key = hash(key)
        index = hashed_key % self._capacity

        if self._hash_table[index]:
            for each in self._hash_table[index]:
                if each[0] == key:
                    each[1] = value
                    return

        self._hash_table[index].append([key, value, hashed_key])
        self._size += 1

        if self._size > self._threshold:
            self._resize()

    def __getitem__(self, item: Hashable) -> Any:

        index = hash(item) % self._capacity

        if self._hash_table[index]:
            for cell in self._hash_table[index]:
                if cell[0] == item:
                    return cell[1]

        raise KeyError(f"there is no such key '{item}'")

    def __len__(self) -> int:
        return self._size

    def _resize(self) -> None:
        self._capacity *= 2
        self._threshold = int(self._capacity / 3 * 2)
        new = [[] for _ in range(self._capacity)]

        for cell in self._hash_table:
            if cell:
                for element in cell:
                    index = element[2] % self._capacity
                    new[index].append(element)
        self._hash_table = new

    def clear(self) -> None:
        self._capacity = 8
        self._size = 0
        self._hash_table = [[] for _ in range(self._capacity)]

    def __delitem__(self, item: Hashable) -> None:

        index = hash(item) % self._capacity

        if self._hash_table[index]:
            for i, cell in enumerate(self._hash_table[index]):
                if cell[0] == item:
                    del self._hash_table[index][i]
                    return
        raise KeyError(f"there is no such key '{item}'")

    def get(self, key: Hashable, value: Any = None) -> Any:
        try:
            return self.__getitem__(key)
        except KeyError:
            return value

    def pop(self, item: Hashable) -> Any:
        value = self[item]
        del self[item]
        return value
