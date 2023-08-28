from typing import Hashable, Any


class Node:
    def __init__(self, key: Hashable, hash_value: int, value: Any) -> None:
        self.key = key
        self.hash_value = hash_value
        self.value = value


class Dictionary:
    def __init__(self, capacity: int = 8, load_factor: float = 0.67) -> None:
        self.capacity = capacity
        self.load_factor = load_factor
        self.size = 0
        self.table = [None] * self.capacity

    def __setitem__(self, key: Hashable, value: Any) -> None:
        hash_value = hash(key)
        index = hash_value % self.capacity

        if self.table[index] is None:
            self.table[index] = [Node(key, hash_value, value)]
        else:
            for node in self.table[index]:
                if node.key == key:
                    node.value = value
                    return
            self.table[index].append(Node(key, hash_value, value))
        self.size += 1

        if self.size >= self.capacity * self.load_factor:
            self._resize()

    def __getitem__(self, key: Hashable) -> None:
        hash_value = hash(key)
        index = hash_value % self.capacity

        if self.table[index] is not None:
            for node in self.table[index]:
                if node.key == key:
                    return node.value
        raise KeyError(key)

    def __len__(self) -> int:
        return self.size

    def _resize(self) -> None:
        new_capacity = self.capacity * 2
        new_table = [None] * new_capacity

        for i in range(self.capacity):
            if self.table[i] is not None:
                for node in self.table[i]:
                    new_index = node.hash_value % new_capacity
                    if new_table[new_index] is None:
                        new_table[new_index] = [node]
                    else:
                        new_table[new_index].append(node)

        self.table = new_table
        self.capacity = new_capacity
