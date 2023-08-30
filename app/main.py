from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.load_factor = 2 / 3
        self.size = 0
        self.storage = [None] * self.capacity

    def __setitem__(self, key: Any, value: Any) -> None:
        idx = hash(key) % self.capacity
        while True:
            if self.storage[idx] is None:
                self.storage[idx] = [key, hash(key), value]
                self.size += 1
                break
            if self.storage[idx] is not None:
                if key == self.storage[idx][0]:
                    self.storage[idx][2] = value
                    break
            idx = (idx + 1) % self.capacity
        if self.size >= self.capacity * self.load_factor:
            self.resize()

    def __getitem__(self, key: Any) -> None:
        for key_value_pair in self.storage:
            if key_value_pair is not None and key_value_pair[0] == key:
                return key_value_pair[2]
        else:
            raise KeyError(key)

    def __len__(self) -> int:
        return self.size

    def resize(self) -> None:
        old_storage = self.storage
        self.capacity *= 2
        self.size = 0
        self.clear()
        for item in old_storage:
            if item is not None:
                self.__setitem__(item[0], item[2])

    def clear(self) -> None:
        self.storage = [None] * self.capacity

    def __delitem__(self, key: Any) -> None:
        for idx in range(self.capacity):
            if self.storage[idx] is not None and self.storage[idx][0] == key:
                self.storage[idx] = None
                break
        else:
            raise KeyError(key)

    def get(self, key: Any, default: Any = None) -> None:
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    def pop(self, key: Any) -> None:
        try:
            print(self.__getitem__(key))
            self.__delitem__(key)
        except KeyError:
            raise KeyError(key)

    def __iter__(self) -> None:
        for item in self.storage:
            if item is not None:
                yield item[2]
