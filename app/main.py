import random
from copy import deepcopy
from typing import Hashable, List


class Node:
    def __init__(self, key: Hashable, value: object) -> None:
        self.key = key
        self.value = value
        self.next = []

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key_value):
        if not isinstance(key_value, Hashable):
            raise TypeError(f"{key_value} is not hashable")
        self._key = key_value

    # def __hash__(self):
    #     return hash(self.key)

    def __repr__(self) -> str:
        return f"{self.key}: {self.value}"


class Dictionary:

    def __init__(self, initial_capacity: int = 8) -> None:
        self.initial_capacity = initial_capacity
        self.load_factor = int(self.initial_capacity * (2 / 3))
        self.bucket = [None] * self.initial_capacity
        self.empty_indexes = list(range(self.initial_capacity))

    def find_index(self, key: Hashable) -> int:
        return hash(key) % self.initial_capacity

    def __setitem__(self, key: Hashable, value: object) -> None:
        hash_table_index = self.find_index(key)

        # if index inside list is None:
        if self.bucket[hash_table_index] is None:
            self.bucket[hash_table_index] = Node(key, value)
            self.empty_indexes.remove(hash_table_index)

        # if index inside is occupied
        if self.bucket[hash_table_index] is not None:
            if self.bucket[hash_table_index].key == key:
                self.bucket[hash_table_index] = Node(key, value)
            else:
                random_index = random.choice(self.empty_indexes)
                self.empty_indexes.remove(random_index)
                self.bucket[hash_table_index].next.append(random_index)
                self.bucket[random_index] = Node(key, value)

        if len(self.empty_indexes) + 1 <= self.initial_capacity - self.load_factor:
            self.resize()

    def __getitem__(self, key: Hashable) -> None:
        if not isinstance(key, Hashable):
            raise TypeError(f"{key} is not hashable")

        hash_table_index = self.find_index(key)

        if self.bucket[hash_table_index] is None:
            raise KeyError("Current key does not exist")

        if self.bucket[hash_table_index].key == key:
            return self.bucket[hash_table_index].value

        for index in self.bucket[hash_table_index].next:
            if self.bucket[index].key == key:
                return self.bucket[index].value

    def resize(self) -> None:
        self.initial_capacity *= 2
        self.load_factor = int(self.initial_capacity * (2 / 3))
        self.empty_indexes = list(range(self.initial_capacity))
        old_bucket = deepcopy(self.bucket)
        self.bucket = [None] * self.initial_capacity

        for node in old_bucket:
            if node is not None:
                self.__setitem__(node.key, node.value)

    def __len__(self) -> int:
        return len(self.bucket) - len(self.empty_indexes)


if __name__ == '__main__':
    d = Dictionary()

    d[1] = "one"
    d[2] = "two"
    d["str"] = "string"
    d[6] = 6
    d[8] = 8
    print(d.bucket)