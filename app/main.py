from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.hash_table: list = [None] * 8
        self.load_factor = 2 / 3

    def _reorganize(self) -> None:
        old_table = self.hash_table
        new_capacity = len(old_table) * 2
        self.hash_table = [None] * new_capacity
        self.length = 0

        for node in old_table:
            while node:
                self.__setitem__(node.key, node.value)
                node = node.next

    def __setitem__(self, key: Any, value: Any) -> None:
        if self.length >= int(self.load_factor * len(self.hash_table)):
            self._reorganize()

        new_node = Node(key, value)
        key_hash = hash(key)
        index = key_hash % len(self.hash_table)

        if self.hash_table[index]:
            node = self.hash_table[index]
            while node:
                if node.key == key:
                    node.value = value
                    return
                if not node.next:
                    break
                node = node.next
            node.next = new_node
        else:
            self.hash_table[index] = new_node

        self.length += 1

    def __getitem__(self, key: Any) -> Any:
        key_hash = hash(key)
        index = key_hash % len(self.hash_table)
        node = self.hash_table[index]
        if node is None:
            raise KeyError("Unknown key")
        while node:
            if node.key == key:
                return node.value
            node = node.next
        raise KeyError("Unknown key")

    def __len__(self) -> int:
        return self.length

    def __delitem__(self, key: Any) -> None:
        key_hash = hash(key)
        index = key_hash % len(self.hash_table)
        node = self.hash_table[index]
        node_prev = None

        while node:
            if node.key == key:
                if node_prev is None:
                    self.hash_table[index] = node.next
                else:
                    node_prev.next = node.next
                self.length -= 1
                return
            node_prev = node
            node = node.next

        raise KeyError(f"Key {key} not found")

    def clear(self) -> None:
        self.hash_table = {}


class Node:
    def __init__(self, key: Any, value: Any) -> None:
        self.key = key
        self.value = value
        self.next = None
