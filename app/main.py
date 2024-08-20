from typing import Any, Hashable
from copy import deepcopy


class Dictionary:
    class Node:
        def __init__(self, key: Hashable, value: Any, my_hash: int) -> None:
            self.key = key
            self.value = value
            self.my_hash = my_hash

        def __repr__(self) -> str:
            return f"Node(key={self.key}, value={self.value})"

    def __init__(self) -> None:
        self.__capacity = 8
        self.__load_factor = 2 / 3
        self.__size = 0
        self.__arr = [0 for _ in range(self.__capacity)]

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.__ready_to_resize():
            self.__resize()

        index = self.__find_index(key)
        if self.__arr[index] == 0:
            self.__size += 1
        self.__add_node(index, key, value)

    def __getitem__(self, key: Hashable) -> Any:
        index = self.__find_index(key)
        if self.__arr[index] == 0:
            raise KeyError(f"Value for key '{key}' not found")

        return self.__arr[index].value

    def __delitem__(self, key: Hashable) -> None:
        index = self.__find_index(key)
        if self.__arr[index] == 0:
            raise KeyError(f"Value for key '{key}' not found")

        self.__arr[index] = 0
        self.__size -= 1

    def __len__(self) -> int:
        return self.__size

    def __repr__(self) -> str:
        return str(self.__arr)

    def __find_index(self, key: Hashable) -> int:
        index = hash(key) % self.__capacity
        while self.__arr[index] != 0 and self.__arr[index].key != key:
            index = (index + 1) % self.__capacity

        return index

    def clear(self) -> None:
        self.__init__()

    def __ready_to_resize(self) -> bool:
        return self.__size >= self.__capacity * self.__load_factor

    def __resize(self) -> None:
        self.__capacity = self.__capacity * 2
        self.__size = 0
        copy_arr: list = deepcopy(self.__arr)
        self.__arr: list = [0 for _ in range(self.__capacity)]

        for values in copy_arr:
            if values != 0:
                self.__setitem__(values.key, values.value)

    def __add_node(self, index: int, key: Any, value: Any) -> None:
        self.__arr[index] = Dictionary.Node(key, value, hash(key))
