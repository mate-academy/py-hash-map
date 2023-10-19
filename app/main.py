class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class Dictionary:
    def __init__(self, capacity=8, load_factor=0.7):
        self.capacity = capacity
        self.load_factor = load_factor
        self.size = 0
        self.table = [None] * self.capacity

    def hash_function(self, key):
        return hash(key) % self.capacity

    def __setitem__(self, key, value):
        index = self.hash_function(key)
        new_node = Node(key, value)

        if self.table[index] is None:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            new_node.next = self.table[index]
            self.table[index] = new_node

        self.size += 1
        if self.size >= self.load_factor * self.capacity:
            self.resize()

    def __getitem__(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError(f"Key '{key}' not found")

    def __len__(self):
        return self.size

    def __delitem__(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return
            prev = current
            current = current.next
        raise KeyError(f"Key '{key}' not found")

    def clear(self):
        self.capacity = 8
        self.size = 0
        self.table = [None] * self.capacity

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

    def update(self, other_dict):
        for key, value in other_dict.items():
            self[key] = value

    def __iter__(self):
        for index in range(self.capacity):
            current = self.table[index]
            while current:
                yield current.key
                current = current.next

    def resize(self):
        new_capacity = self.capacity * 2
        new_table = [None] * new_capacity

        for i in range(self.capacity):
            current = self.table[i]
            while current:
                new_index = self.hash_function(current.key)
                new_node = Node(current.key, current.value)
                if new_table[new_index] is None:
                    new_table[new_index] = new_node
                else:
                    new_node.next = new_table[new_index]
                    new_table[new_index] = new_node
                current = current.next

        self.capacity = new_capacity
        self.table = new_table
