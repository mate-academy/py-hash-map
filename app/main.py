from typing import Hashable, Any


class Dictionary:

    class Node:

        def __init__(self, key: Hashable, value: Any, hash_key: int) -> None:
            self.key = key
            self.value = value
            self.hash_key = hash_key

    def __init__(self) -> None:
        self.load_factor = 2 / 3
        self.number_of_elements = 0
        self.capacity = 8
        self.size = 0
        self.hash_table = [None] * self.capacity

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.size >= self.capacity * self.load_factor:
            self.resize()

        index = self.find_index(key)
        if self.hash_table[index] is None:
            self.size += 1

        self.hash_table[index] = Dictionary.Node(key, value, hash(key))

    def __getitem__(self, key: Hashable) -> Any:
        index = self.find_index(key)
        if self.hash_table[index] is None:
            raise KeyError(f"Value for key '{key}' not found")

        return self.hash_table[index].value

    def get(self, key: Hashable, default: Any = None) -> None:
        try:
            return self[key]
        except KeyError:
            return default

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        return str(self.hash_table)

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        self.size = 0
        new_table: list[None | Dictionary.Node] = [None] * self.capacity

        new_table: list[None | Dictionary.Node] = [None] * self.capacity

        old_table = self.hash_table
        self.hash_table = new_table

        for bucket in old_table:
            if bucket is not None:
                if isinstance(bucket, list):
                    for node in bucket:
                        if node is not None:
                            self.__setitem__(node.key, node.value)
                else:
                    self.__setitem__(bucket.key, bucket.value)

    def find_index(self, key: Hashable) -> int:
        index = hash(key) % self.capacity
        while (self.hash_table[index] is not None
                and self.hash_table[index].key != key):
            index = (index + 1) % self.capacity

        return index
