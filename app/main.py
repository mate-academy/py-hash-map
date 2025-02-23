class Dictionary:
    def __init__(self, capacity: int = 8, load_factor: float = 0.75):
        self.capacity = capacity
        self.load_factor = load_factor
        self.size = 0
        self.table = [None] * self.capacity  # List to store key-value pairs

    def _hash(self, key: int) -> int:
        return hash(key) % self.capacity

    def _resize(self) -> None:
        new_capacity = self.capacity * 2
        new_table = [None] * new_capacity

        # Rehash all existing items and add them to the new table
        for item in self.table:
            if item:
                key, value = item
                index = hash(key) % new_capacity
                new_table[index] = (key, value)

        self.capacity = new_capacity
        self.table = new_table

    def __setitem__(self, key, value) -> None:
        if self.size / self.capacity > self.load_factor:
            self._resize()  # Resize if the load factor is exceeded

        index = self._hash(key)

        # Handle collisions with linear probing
        while self.table[index] is not None:
            existing_key, existing_value = self.table[index]
            if existing_key == key:
                self.table[index] = (key, value)  # Update the value if the key exists
                return
            index = (index + 1) % self.capacity  # Linear probing
        self.table[index] = (key, value)
        self.size += 1

    def __getitem__(self, key: int) -> None:
        index = self._hash(key)
        while self.table[index] is not None:
            existing_key, existing_value = self.table[index]
            if existing_key == key:
                return existing_value
            index = (index + 1) % self.capacity
        raise KeyError(f"Key {key} not found.")

    def __len__(self) -> int:
        return self.size

