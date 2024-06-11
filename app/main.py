class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8   # default value
        self.hash_table = self.create_hash_table()
        self.load_factor = self.calculate_load_factor()
        self.size = 0

    def create_hash_table(self) -> list:
        return [None] * self.capacity

    def calculate_load_factor(self) -> int:
        return int(self.capacity * (2 / 3))

    def __setitem__(self, key: int, value: int) -> int:
        hash_key = hash(key)
        index = hash_key % self.capacity

        while True:
            if self.hash_table[index] is None:
                self.hash_table[index] = (key, value, hash_key)
                self.size += 1
                if self.size == self.load_factor:
                    self.resise_table()
                break
            elif self.hash_table[index][0] == key:
                self.hash_table[index] = (key, value, hash_key)
                break
            index += 1
            index %= self.capacity

    def __getitem__(self, key: int) -> None:
        hash_key = hash(key)
        index = hash_key % self.capacity

        while True:
            if self.hash_table[index] is None:
                raise KeyError
            if self.hash_table[index][0] == key:
                return self.hash_table[index][1]
                break
            index += 1
            index %= self.capacity

    def resise_table(self) -> None:
        self.capacity *= 2
        self.load_factor = self.calculate_load_factor()
        old_hash_table = self.hash_table.copy()
        self.hash_table = self.create_hash_table()
        self.size = 0
        for node in old_hash_table:
            if node:
                key, value, hash_key = node
                self.__setitem__(key, value)

    def __len__(self) -> int:
        return self.size
