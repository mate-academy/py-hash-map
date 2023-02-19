from __future__ import annotations


class Node:
    def __init__(self, key, value, hash_val=None):
        self.key = key
        self.value = value
        self.hash = hash(key) if hash_val is None else hash_val


class Dictionary:
    def __init__(self, capacity=8, load_factor=2 / 3):
        self.capacity = capacity
        self.load_factor = load_factor
        self.size = 0
        self.table = [[] for _ in range(self.capacity)]

    def __setitem__(self, key, value):

        hash_val = hash(key)
        store = self.table[hash_val % self.capacity]
        for node in store:
            if node.key == key:
                node.value = value
                return
        store.append(Node(key, value, hash_val))
        self.size += 1
        if self.size >= self.capacity * self.load_factor:
            self.resize()

    def resize(self):
        self.capacity *= 2
        new_table = [[] for _ in range(self.capacity)]

        for store in self.table:

            for node in store:
                new_table[node.hash % self.capacity].append(node)
        self.table = new_table

    def __getitem__(self, key):
        hash_val = hash(key)
        store = self.table[hash_val % self.capacity]
        for node in store:
            if node.key == key:
                return node.value
        raise KeyError(key)

    def __len__(self):
        return self.size

    def __delitem__(self, key):
        hash_val = hash(key)
        store = self.table[hash_val % self.capacity]
        for i, node in enumerate(store):
            if node.key == key:
                del store[i]
                self.size -= 1
                return
        raise KeyError(key)

    def clear(self):
        self.size = 0
        self.table = [[] for _ in range(self.capacity)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def pop(self, key, default=None):
        try:
            value = self[key]
            del self[key]
            return value
        except KeyError:
            return default

    def update(self, other):
        for key, value in other.items():
            self[key] = value

    def __iter__(self):
        for store in self.table:
            for node in store:
                yield node.key
