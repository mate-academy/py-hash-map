class Node:
    def __init__(self, key: object, value: object) -> None:
        self.key = key
        self.value = value
        self.hash = hash(key)


class Dictionary:
    def __init__(self, capacity: int = 16, load_factor: float = 0.75) -> None:
        self.capacity = capacity
        self.size = 0
        self.load_factor = load_factor
        self.table = [[] for _ in range(capacity)]

    def _resize(self) -> None:
        old_table = self.table
        self.capacity *= 2
        self.table = [[] for _ in range(self.capacity)]
        self.size = 0
        for bucket in old_table:
            for node in bucket:
                self[node.key] = node.value

    def _hash_index(self, key: object) -> int:
        return hash(key) % self.capacity

    def __setitem__(self, key: object, value: object) -> None:
        if self.size / self.capacity > self.load_factor:
            self._resize()

        index = self._hash_index(key)
        bucket = self.table[index]
        for node in bucket:
            if node.key == key:
                node.value = value
                return
        bucket.append(Node(key, value))
        self.size += 1

    def __getitem__(self, key: object) -> object:
        index = self._hash_index(key)
        bucket = self.table[index]
        for node in bucket:
            if node.key == key:
                return node.value
        raise KeyError(f"Key {key} not found")

    def __len__(self) -> int:
        return self.size
