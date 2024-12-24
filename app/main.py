from typing import Any

INITIAL_CAPACITY = 8
RESIZE_THRESHOLD = 2 / 3


class Node:
    def __init__(self, key: Any, value: Any) -> None:
        self.value = value
        self.key = key
        self.hash = hash(key)


class Dictionary:
    def __init__(self, capacity: int = INITIAL_CAPACITY) -> None:
        self.capacity = capacity
        self.size = 0
        self.hashtable: list[None | Node] = [None] * self.capacity

    def calculate_index(self, key: Any) -> int:
        index = hash(key) % self.capacity
        while (
                self.hashtable[index] is not None
                and self.hashtable[index].key != key
        ):
            index = (index + 1) % self.capacity
        return index

    def __setitem__(self, key: Any, value: Any) -> None:
        index = self.calculate_index(key)

        if self.hashtable[index] is None:
            if self.size + 1 > self.capacity * RESIZE_THRESHOLD:
                old_hash_table = self.hashtable
                self.__init__(self.capacity * 2)

                for node in old_hash_table:
                    if node is not None:
                        self.__setitem__(node.key, node.value)

                return self.__setitem__(key, value)

            self.size += 1

        self.hashtable[index] = Node(key, value)

    def __getitem__(self, key: Any) -> Any:
        index = self.calculate_index(key)

        if self.hashtable[index] is None:
            raise KeyError(f"key {key} is not present in dictionary")

        return self.hashtable[index].value

    def __len__(self) -> int:
        return self.size
