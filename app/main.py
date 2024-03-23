class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.load_factor = 2 / 3
        self.hash_table = [None] * self.capacity

    def __len__(self) -> int:
        return sum(1 for entry in self.hash_table if entry is not None)

    def __getitem__(self, key: any) -> any:
        hash_value = hash(key) % self.capacity
        while self.hash_table[hash_value] is not None:
            if self.hash_table[hash_value] == key:
                return self.hash_table[hash_value][2]
            hash_value = (hash_value + 1) % self.capacity
        raise KeyError(f"'{key}' not found in the dictionary")

    def __setitem__(self, key: any, value: any) -> None:
        hash_value = hash(key) % self.capacity
        while self.hash_table[hash_value] is not None \
                and self.hash_table[hash_value][0] != key:
            hash_value = hash(key + 1) % self.capacity
        self.hash_table[hash_value] = (key, hash_value, value)
        if len(self) >= self.load_factor * self.capacity:
            self._resize()

    def _resize(self) -> None:
        new_capacity = self.capacity * 2
        new_hash_table = [None] * new_capacity
        for entry in self.hash_table:
            if entry is not None:
                key, _, value = entry
                new_hash_value = hash(key) % new_capacity
                while new_hash_table[new_hash_value] is not None:
                    new_hash_value = hash(key + 1) % new_capacity
                new_hash_table[new_hash_value] = (key, new_hash_value, value)
        self.hash_table = new_hash_table
        self.capacity = new_capacity
