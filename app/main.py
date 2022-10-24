class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.hash_size = 8
        self.hash_table = [[] for _ in range(self.hash_size)]
        self.treshold = int(self.hash_size * 2 / 3)

    def resize_hash(self) -> None:
        old_hash_table = self.hash_table
        self.hash_size *= 2
        self.treshold = int(self.hash_size * 2 / 3)
        self.length = 0
        self.hash_table = [[] for _ in range(self.hash_size)]
        for item in old_hash_table:
            if item:
                self.__setitem__(item[0], item[1])

    def __setitem__(self, key: object, value: object) -> None:
        if self.length == self.treshold:
            self.resize_hash()
        index = hash(key) % self.hash_size
        while True:
            if not self.hash_table[index]:
                self.hash_table[index] = [key, value]
                self.length += 1
                return
            if key in self.hash_table[index]:
                self.hash_table[index][1] = value
                return

            index = (index + 1) % self.hash_size

    def __getitem__(self, key: object) -> object:
        index = hash(key) % self.hash_size
        while self.hash_table[index]:
            if key in self.hash_table[index]:
                return self.hash_table[index][1]
            index = (index + 1) % self.hash_size
        raise KeyError(f"Key {key} does not exist")

    def __len__(self) -> int:
        return self.length

    def clear(self) -> None:
        self.hash_size = 8
        self.treshold = int(self.hash_size * 2 / 3)
        self.length = 0
        self.hash_table = [[] for _ in range(self.hash_size)]

    def __delitem__(self, key: object) -> None:
        index = hash(key) % self.hash_size
        while self.hash_table[index]:
            if key in self.hash_table[index]:
                self.hash_table[index] = []
                return
            index = (index + 1) % self.hash_size
