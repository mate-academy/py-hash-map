from typing import Any
from dataclasses import dataclass


@dataclass
class Node:
    key: Any
    value: Any
    next = None


class Dictionary:
    def __init__(
        self,
        initial_capacity: int = 8,
        load_factor: float = 0.66
    ) -> None:
        self.capacity = initial_capacity
        self.load_factor = load_factor
        self.table = [None] * self.capacity
        self.table_size = 0

    def __setitem__(self, key: Any, value: Any) -> None:
        index = self.__get_index(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
            self.table_size += 1
        else:
            current = self.table[index]
            while True:
                if current.key == key:
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = Node(key, value)
            self.table_size += 1

        if self.table_size >= self.capacity * self.load_factor:
            self.__resize_table()

    def __getitem__(self, key: Any) -> Any:
        index = self.__get_index(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError(f"Key '{key}' does not exist in the dictionary!")

    def __resize_table(self) -> None:
        self.capacity *= 2
        new_table = [None] * self.capacity

        for i in range(len(self.table)):
            current = self.table[i]
            while current:
                index = self.__get_index(current.key)
                if new_table[index] is None:
                    new_table[index] = Node(current.key, current.value)
                else:
                    new_current = new_table[index]
                    while new_current.next:
                        new_current = new_current.next
                    new_current.next = Node(current.key, current.value)
                current = current.next

        self.table = new_table

    def __get_index(self, key: Any) -> int:
        return hash(key) % self.capacity

    def __len__(self) -> int:
        return self.table_size
