from __future__ import annotations

from typing import Any, Iterator, Tuple, Optional


class Dictionary:
    def __init__(self) -> None:
        self.__capacity = 7
        self.__create_hash_table()
        self.__len = 0

    def __setitem__(self, key: Any, value: Any) -> None:
        hashed_value = hash(key)
        index = hashed_value % self.__capacity

        while True:
            if self.__is_cell_empty(index):
                if self.__is_need_resize():
                    self.__resize_hash_table()
                    index = hashed_value % self.__capacity
                    continue
                self.__insert_new_item(index, (key, hashed_value, value))
                break
            saved_key, saved_hash, saved_value = self.hash_table[index]
            if key == saved_key and hashed_value == saved_hash:
                self.hash_table[index] = (key, hashed_value, value)
                break
            index = (index + 1) % self.__capacity

    def __is_cell_empty(self, index: int) -> bool:
        return self.hash_table[index] is None

    def __is_need_resize(self) -> bool:
        return self.__len + 1 > self.__get_threshold()

    def __insert_new_item(self, index: int, item_value: tuple) -> None:
        self.hash_table[index] = item_value
        self.__len += 1
        if self.__is_need_resize():
            self.__resize_hash_table()

    def __getitem__(self, key: Any) -> Any:
        hashed_value = hash(key)
        index = hashed_value % self.__capacity
        if self.hash_table[index] is None:
            raise KeyError(f"'{key}' not found")
        while True:
            saved_key, saved_hash, saved_value = self.hash_table[index]
            if key == saved_key and hashed_value == saved_hash:
                return saved_value
            index = (index + 1) % self.__capacity

    def __len__(self) -> int:
        return self.__len

    def __get_threshold(self) -> int:
        return int(self.__capacity * 0.75)

    def __create_hash_table(self) -> None:
        self.hash_table = [None for _ in range(self.__capacity + 1)]
        self.__len = 0

    def __resize_hash_table(self) -> None:
        old_capacity = self.__capacity
        self.__capacity = (self.__capacity + 1) * 2 - 1
        old_hash_table = self.hash_table
        self.__create_hash_table()
        for index in range(old_capacity + 1):
            if old_hash_table[index] is not None:
                key, hash, value = old_hash_table[index]
                self.__setitem__(key, value)

    def clear(self) -> None:
        self.__create_hash_table()

    def __delitem__(self, key: Any) -> None:
        hashed_value = hash(key)
        index = hashed_value % self.__capacity
        if self.hash_table[index] is None:
            raise KeyError(f"'{key}' not found")
        while True:
            saved_key, saved_hash, saved_value = self.hash_table[index]
            if key == saved_key and hashed_value == saved_hash:
                self.hash_table[index] = None
                self.__len -= 1
                break
            index = (index + 1) % self.__capacity

    def get(self, key: Any, default: Any = None) -> Any:
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    def pop(self, key: Any, **kwargs) -> Any:
        try:
            value = self.__getitem__(key)
            self.__delitem__(key)
            return value
        except KeyError as e:
            if "default" in kwargs:
                return kwargs["default"]
            raise KeyError(e)

    def update(self, other_dict: Dictionary) -> None:
        for key, value in other_dict:
            self.__setitem__(key, value)

    def __iter__(self) -> Iterator[Tuple[Optional[Any], Optional[Any]]]:
        for index in range(self.__capacity):
            if self.hash_table[index] is not None:
                key, hash, value = self.hash_table[index]
                yield key, value

    def __repr__(self) -> str:
        result = "{"
        for index in range(self.__capacity):
            if self.hash_table[index] is not None:
                key, hash, value = self.hash_table[index]
                result += f"{key}: {value}, "
        result += "}"
        return result
