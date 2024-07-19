from typing import Any
from copy import deepcopy


class Node:
    def __init__(self, key: Any, value: Any) -> None:
        self.key = key
        self.value = value

    def __repr__(self) -> str:
        return f"Node(key={self.key}, value={self.value})"


class Dictionary:
    def __init__(self) -> None:
        self.__capacity = 8
        self.__load_factor = 2 / 3
        self.__size = 0
        self.__arr: list[int | Node] = [0 for _ in range(self.__capacity)]

    def __setitem__(self, key: Any, value: Any) -> None:
        if self.__ready_to_resize():
            self.__resize()

        index = hash(key) % self.__capacity
        if self.__arr[index] != 0 and self.__arr[index].key == key:
            self.__arr[index].value = value
            return

        if self.__arr[index] == 0:
            self.__add_node(index, key, value)
        elif self.__arr[index] != 0 and self.__arr[index].key != key:
            for i in range(index, self.__capacity):
                if i == self.__capacity - 1:
                    for next_i in range(0, self.__capacity):
                        if self.__arr[next_i] == 0:
                            self.__add_node(next_i, key, value)
                            break
                if self.__arr[i] == 0:
                    self.__add_node(i, key, value)
                    break
                if self.__arr[i] != 0 and self.__arr[i].key == key:
                    self.__arr[i].value = value
                    break

    def __getitem__(self, key: Any) -> Any:
        for i in range(self.__capacity):
            if self.__arr[i] != 0 and self.__arr[i].key == key:
                return self.__arr[i].value

        raise KeyError(f"Value for key '{key}' not found")

    def __len__(self) -> int:
        return self.__size

    def __repr__(self) -> str:
        return str(self.__arr)

    def clear(self) -> None:
        self.__init__()

    def __ready_to_resize(self) -> bool:
        return self.__size == round(self.__capacity * self.__load_factor)

    def __resize(self) -> None:
        self.__capacity = self.__capacity * 2
        self.__size = 0
        copy_arr: list[int | Node] = deepcopy(self.__arr)
        self.__arr: list[int | Node] = [0 for _ in range(self.__capacity)]

        for values in copy_arr:
            if values != 0:
                self.__setitem__(values.key, values.value)

    def __add_node(self, index: int, key: Any, value: Any) -> None:
        self.__arr[index] = Node(key, value)
        self.__size += 1
