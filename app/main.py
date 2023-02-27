from typing import Hashable


class Node:
    def __init__(self, key: Hashable, value: any) -> None:
        self.key = key
        self.value = value
        self.next = None


class Dictionary:
    def __init__(self, capacity: int = 8, load_factor: float = 2 / 3) -> None:
        self.capacity = capacity
        self.size = 0
        self.load_factor = load_factor
        self.table = [None] * capacity

    def __setitem__(self, key: Hashable, value: any) -> None:
        index = self.hash(key)
        node = self.table[index]
        if node is None:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            while node:
                if node.key == key:
                    node.value = value
                    break
                if node.next is None:
                    node.next = Node(key, value)
                    self.size += 1
                    break
                node = node.next

        if self.size / self.capacity >= self.load_factor:
            self.resize()

    def __getitem__(self, key: Hashable) -> str:
        index = self.hash(key)
        node = self.table[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        raise KeyError(f"Key {key} not found")

    def __len__(self) -> int:
        return self.size

    def clear(self) -> None:
        self.table = [None] * self.capacity
        self.size = 0

    def resize(self) -> None:
        self.capacity *= 2
        new_table = [None] * self.capacity
        for node in self.table:
            while node:
                index = self.hash(node.key)
                if new_table[index] is None:
                    new_table[index] = Node(node.key, node.value)
                else:
                    current = new_table[index]
                    while current.next:
                        current = current.next
                    current.next = Node(node.key, node.value)
                node = node.next
        self.table = new_table

    def __delitem__(self, key: Hashable) -> None:
        index = self.hash(key)
        node = self.table[index]
        if node is None:
            raise KeyError(f"Key {key} not found")
        if node.key == key:
            self.table[index] = node.next
            self.size -= 1
            return
        prev = node
        while node:
            if node.key == key:
                prev.next = node.next
                self.size -= 1
                return
            prev = node
            node = node.next
        raise KeyError(f"Key {key} not found")

    def get(self, key: Hashable, default: None = None) -> any:
        try:
            return self[key]
        except KeyError:
            return default

    def pop(self) -> tuple:
        for i, node in enumerate(self.table):
            if node is not None:
                self.table[i] = node.next
                self.size -= 1
                return node.key, node.value
        raise KeyError("Dictionary is empty")

    def update(self, other: dict) -> None:
        for key, value in other.items():
            self[key] = value

    def __iter__(self) -> any:
        for node in self.table:
            while node:
                yield node.key
                node = node.next

    def hash(self, key: Hashable) -> int:
        return hash(key) % self.capacity
