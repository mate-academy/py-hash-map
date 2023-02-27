class Dictionary:
    def __init__(self, capacity=10, load_factor=0.7):
        self.capacity = capacity
        self.load_factor = load_factor
        self.size = 0
        self.hash_table = [[] for _ in range(capacity)]

    def __setitem__(self, key, value):
        index = self._hash_function(key)
        for node in self.hash_table[index]:
            if node[0] == key:
                node[2] = value
                return
        self.hash_table[index].append([key, self._hash_function(key), value])
        self.size += 1
        if self.size / self.capacity >= self.load_factor:
            self._resize()

    def __getitem__(self, key):
        index = self._hash_function(key)
        for node in self.hash_table[index]:
            if node[0] == key:
                return node[2]
        raise KeyError(key)

    def __len__(self):
        return self.size

    def _hash_function(self, key):
        return hash(key) % self.capacity

    def _resize(self):
        self.capacity *= 2
        new_hash_table = [[] for _ in range(self.capacity)]
        for nodes in self.hash_table:
            for node in nodes:
                index = self._hash_function(node[0])
                new_hash_table[index].append(node)
        self.hash_table = new_hash_table
