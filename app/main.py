class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.table_size = 8
        self.hash_table: list = [None] * self.table_size

    def __setitem__(self, key, value):
        hashed_value = hash(key)
        index = hashed_value % self.table_size
        while self.hash_table[index] is not None:
            print(f"The key {key} collided with {self.hash_table[index]}")
            index = (index + 1) % len(self.hash_table)

        self.hash_table[index] = (key, hashed_value, value)
        self.length += 1
        self.resize()

    def resize(self):
        if self.length > 2 / 3 * self.table_size:
            old_hash_table = []
            for container in self.hash_table:
                if container is not None:
                    old_hash_table.append(container)
            self.table_size *= 2
            self.hash_table = [None] * self.table_size
            self.length = 0
            for key, hashed_value, value in old_hash_table:
                self.__setitem__(key, value)

    def __getitem__(self, key):
        hashed_value = hash(key)
        index = hashed_value % len(self.hash_table)
        while self.hash_table[index] is not None:
            saved_key, saved_hashed_value, saved_value = self.hash_table[index]
            if key == saved_key and hashed_value == saved_hashed_value:
                return saved_value
            index = (index + 1) % len(self.hash_table)

    def __len__(self):
        return self.length


new_dict = Dictionary()
print(new_dict.__setitem__(2, "Hello"))
print(new_dict.__getitem__(2))
print(new_dict.hash_table)
print(new_dict.__getitem__(3))