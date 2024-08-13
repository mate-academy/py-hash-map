class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.load_factor = 2 / 3
        self.size = 0
        self.hash_table = [[] for _ in range(self.capacity)]

    def _resize(self) -> None:
        old_hash_table = self.hash_table
        self.capacity *= 2
        self.hash_table = [[] for _ in range(self.capacity)]
        self.size = 0

        for slot in old_hash_table:
            if slot:
                self[slot[0]] = slot[1]

    def _probe(self, key: any, setting: bool = True) -> int:
        index = hash(key) % self.capacity

        while True:
            if not self.hash_table[index]:
                return index if setting else -1
            if self.hash_table[index][0] == key:
                return index
            index = (index + 1) % self.capacity

    def __setitem__(self, key: any, value: any) -> None:
        if self.size > self.capacity * self.load_factor:
            self._resize()

        index = self._probe(key)
        if not self.hash_table[index]:
            self.size += 1
        self.hash_table[index] = [key, value]

    def __getitem__(self, key: any) -> any:
        index = self._probe(key, False)
        if index == -1:
            raise KeyError(f"Key {key} not found")
        return self.hash_table[index][1]

    def __len__(self) -> int:
        return self.size
