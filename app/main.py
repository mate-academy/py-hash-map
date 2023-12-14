class Node:
    def __init__(self, key, value):
        self.key = key
        self.hash = hash(key)
        self.value = value
        self.next = None


class Dictionary:
    def __init__(self, initial_capacity=16, load_factor=0.75):
        self.capacity = initial_capacity
        self.load_factor = load_factor
        self.size = 0
        self.table = [None] * self.capacity

    def __setitem__(self, key, value):
        index = self._hash_index(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current.next:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            if current.key == key:
                current.value = value
                return
            current.next = Node(key, value)
        self.size += 1
        self._resize_if_needed()

    def __getitem__(self, key):
        index = self._hash_index(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError(f"Key not found: {key}")

    def __len__(self):
        return self.size

    def _hash_index(self, key):
        return hash(key) % self.capacity

    def _resize_if_needed(self):
        if self.size / self.capacity > self.load_factor:
            self._resize()

    def _resize(self):
        new_capacity = self.capacity * 2
        new_table = [None] * new_capacity

        for i in range(self.capacity):
            current = self.table[i]
            while current:
                new_index = current.hash % new_capacity
                if new_table[new_index] is None:
                    new_table[new_index] = Node(current.key, current.value)
                else:
                    new_current = new_table[new_index]
                    while new_current.next:
                        new_current = new_current.next
                    new_current.next = Node(current.key, current.value)

                current = current.next

        self.table = new_table
        self.capacity = new_capacity

