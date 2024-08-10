from typing import Hashable, Any


class Dictionary:
    def __init__(
            self,
            keys: list[Hashable] | None = None,
            values: list[Any] | None = None
    ) -> None:
        self.__capacity = 8
        self.__size = 0
        self.__threshold = int((2 / 3) * self.__capacity)
        self.__table = [(None,)] * self.__capacity

        if keys and values:
            for key, value in zip(keys, values):
                self.__setitem__(key, value)

    def __repr__(self) -> str:
        items = ", ".join(f"{key}: {value}" for key, value in self.items())
        return f"{{{items}}}"

    def __setitem__(self, key: Hashable, value: Any) -> None:
        key_hash, index = self.__get_key_hash_and_index(key)

        while self.__table[index][0] is not None:
            if self.__table[index][0] == key:
                self.__table[index] = (key, key_hash, value)
                return
            index += 1
            if index == self.__capacity:
                index = 0

        self.__table[index] = (key, key_hash, value)
        self.__size += 1

        if self.__size > self.__threshold:
            self.__resize()

    def __getitem__(self, key: Hashable) -> Any:
        key_hash, index = self.__get_key_hash_and_index(key)
        start_index = index

        while (
                self.__table[index][0] is not None
                or "Deleted" in self.__table[index]
        ):
            if self.__table[index][0] == key:
                return self.__table[index][2]
            index += 1
            if index == self.__capacity:
                index = 0
            if index == start_index:
                break

        raise KeyError(key)

    def __delitem__(self, key: Hashable) -> None:
        key_hash, index = self.__get_key_hash_and_index(key)
        while (
                self.__table[index][0] is not None
                or "Deleted" in self.__table[index]
        ):
            if self.__table[index][0] == key:
                self.__table[index] = (None, "Deleted")
                self.__size -= 1
                return
            index += 1
            if index == self.__capacity:
                index = 0

        raise KeyError(key)

    def __len__(self) -> int:
        return self.__size

    def __iter__(self) -> "Dictionary":
        self.__current_index = 0
        self.__keys = [element[0] for element in self.__table if element[0]]
        return self

    def __next__(self) -> Any:
        if self.__current_index >= self.__size:
            raise StopIteration
        result_to_return = self.__keys[self.__current_index]
        self.__current_index += 1
        return result_to_return

    def clear(self) -> None:
        self.__table = [(None,)] * self.__capacity
        self.__size = 0

    def get(self, key: Hashable, value: Any = None) -> Any | None:
        try:
            return self.__getitem__(key)
        except KeyError:
            return value

    def pop(self, key: Hashable, defaultvalue: Any = None) -> Any:
        try:
            value_to_return = self.__getitem__(key)
            self.__delitem__(key)
            return value_to_return
        except KeyError:
            if defaultvalue:
                return defaultvalue
            raise

    def update(self, keys: list[Hashable], values: list[Any]) -> None:
        for key, value in zip(keys, values):
            self.__setitem__(key, value)

    def items(self) -> list:
        return [
            (element[0], element[2])
            for element in self.__table
            if element[0] is not None
        ]

    def keys(self) -> list:
        return [
            element[0]
            for element in self.__table
            if element[0] is not None
        ]

    def values(self) -> list:
        return [
            element[2]
            for element in self.__table
            if element[0] is not None
        ]

    def copy(self) -> "Dictionary":
        return Dictionary(self.keys(), self.values())

    def __resize(self) -> None:
        self.__capacity *= 2
        self.__size = 0
        self.__threshold = int((2 / 3) * self.__capacity)
        self.__table_before_resize = self.__table
        self.__table = [(None,)] * self.__capacity

        for element in self.__table_before_resize:
            if element[0] is not None:
                self.__setitem__(element[0], element[2])

        del self.__table_before_resize

    def __get_key_hash_and_index(self, key: Hashable) -> tuple:
        return hash(key), hash(key) % self.__capacity
