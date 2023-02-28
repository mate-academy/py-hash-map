from typing import Hashable, Iterator, Any


class Node:
    def __init__(self, key: Hashable, value: Any) -> None:
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self) -> str:
        return f"{self.key}:{self.value}(next-{self.next})"


class Dictionary:
    def __init__(self, capacity: int = 8, load_factor: float = 2 / 3) -> None:
        self.capacity = capacity
        self.load_factor = load_factor
        self.size = 0
        self.table = [None] * capacity

    def __str__(self) -> str:
        return str(self.table)

    def __setitem__(self, key: Hashable, value: Any) -> None:
        index = hash(key) % self.capacity
        node = self.table[index]
        while node is not None:
            if node.key == key:
                node.value = value
                return
            node = node.next
        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node
        self.size += 1
        if self.size > self.capacity * self.load_factor:
            self._resize()

    def __getitem__(self, key: Hashable) -> Any:
        index = hash(key) % self.capacity
        node = self.table[index]
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next
        raise KeyError(key)

    def __delitem__(self, key: Hashable) -> None:
        index = hash(key) % self.capacity
        node = self.table[index]
        prev = None
        while node is not None:
            if node.key == key:
                if prev is None:
                    self.table[index] = node.next
                else:
                    prev.next = node.next
                self.size -= 1
                return
            prev = node
            node = node.next
        raise KeyError(key)

    def __len__(self) -> int:
        return self.size

    def __iter__(self) -> Iterator:
        for node in self.table:
            while node is not None:
                yield node.key
                node = node.next

    def clear(self) -> None:
        self.capacity = 16
        self.size = 0
        self.table = [None] * self.capacity

    def get(self, key: Hashable) -> Any:
        try:
            return self[key]
        except KeyError:
            return None

    def pop(self, key: Hashable) -> Any:
        try:
            value = self[key]
            del self[key]
            return value
        except KeyError:
            return None

    def update(self, other: dict | list) -> None:
        for key, value in other.items():
            self[key] = value

    def _resize(self) -> None:
        old_table = self.table
        self.capacity *= 2
        self.size = 0
        self.table = [None] * self.capacity
        for node in old_table:
            while node is not None:
                self[node.key] = node.value
                node = node.next


if __name__ == "__main__":
    d = Dictionary()
    d[15] = "A"
    d[3] = "B"
    d[5] = "C"
    d[13] = "D"
    d[9] = "E"
    d[14] = "K"
    d[30] = "F"
    print(d)
    print(d[30])
