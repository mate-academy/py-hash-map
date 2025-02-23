class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class Dictionary:
    def __init__(self, capacity: int = 8, load_factor: float = 0.75):
        self.capacity = capacity
        self.load_factor = load_factor
        self.size = 0
        self.table = [None] * self.capacity

    def _hash(self, key) -> int:
        return hash(key) % self.capacity

    def _resize(self) -> None:
        new_capacity = self.capacity * 2
        new_table = [None] * new_capacity

        for node in self.table:
            while node:
                index = hash(node.key) % new_capacity
                new_node = Node(node.key, node.value)
                new_node.next = new_table[index]
                new_table[index] = new_node
                node = node.next

        self.capacity = new_capacity
        self.table = new_table

    def __setitem__(self, key, value) -> None:
        if self.size / self.capacity > self.load_factor:
            self._resize()

        index = self._hash(key)
        node = self.table[index]

        while node:
            if node.key == key:
                node.value = value
                return
            node = node.next

        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node
        self.size += 1

    def __getitem__(self, key):
        index = self._hash(key)
        node = self.table[index]

        while node:
            if node.key == key:
                return node.value
            node = node.next

        raise KeyError(f"Key {key} not found.")

    def __len__(self) -> int:
        return self.size
    