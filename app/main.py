class Dictionary:
    def __init__(self, initial_capacity=8, load_factor=0.75):
        self.capacity = initial_capacity
        self.load_factor = load_factor
        self.size = 0
        self.buckets = [None] * self.capacity

    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.hash = hash(key)
            self.next = None

    def __setitem__(self, key, value):
        if self.size / self.capacity >= self.load_factor:
            self._resize()

        index = hash(key) % self.capacity
        if not self.buckets[index]:
            self.buckets[index] = self.Node(key, value)
        else:
            node = self.buckets[index]
            while True:
                if node.key == key:
                    node.value = value  # Update value
                    return
                if not node.next:
                    break
                node = node.next
            node.next = self.Node(key, value)

        self.size += 1

    def __getitem__(self, key):
        index = hash(key) % self.capacity
        node = self.buckets[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        raise KeyError(f"Key {key} not found")

    def __len__(self):
        return self.size

    def _resize(self):
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [None] * self.capacity
        self.size = 0
        for node in old_buckets:
            while node:
                self[key] = node.value
                node = node.next
