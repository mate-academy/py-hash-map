from typing import Optional


class Node:
    def __init__(
            self, key: int, hash_value: int, value: str, next_node: any = None
    ) -> None:
        self.key = key
        self.hash_value = hash_value
        self.value = value
        self.next_node = next_node


class Dictionary:
    def __init__(self) -> None:
        self.length: int = 0
        self.capacity: int = 8
        self.load_factor: float = 0.75
        self.hash_table: list[Optional[Node]] = [None] * self.capacity

    def _hash_function(self, key: int) -> int:
        return hash(key)

    def __setitem__(self, key: int, value: str) -> None:
        hash_value: int = self._hash_function(key)
        index: int = hash_value % self.capacity
        node: Optional[Node] = self.hash_table[index]

        while node:
            if node.key == key:
                node.value = value
                return
            node = node.next_node

        new_node = Node(key, hash_value, value, self.hash_table[index])
        self.hash_table[index] = new_node
        self.length += 1

        if self.length > self.capacity * self.load_factor:
            self._resize()

    def __getitem__(self, key: int) -> str:
        hash_value: int = self._hash_function(key)
        index: int = hash_value % self.capacity
        node: Optional[Node] = self.hash_table[index]

        while node:
            if node.key == key:
                return node.value
            node = node.next_node

        raise KeyError(key)

    def __len__(self) -> int:
        return self.length

    def _resize(self) -> None:
        pass
