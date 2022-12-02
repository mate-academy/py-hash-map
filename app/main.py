class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.threshold = int(self.capacity * (2 / 3)) + 1
        self.length = 0
        self.hash_table = [[]] * self.capacity

    def __setitem__(self, key: object, value: object) -> None:
        if self.length == self.threshold:
            self.resize()
        index = hash(key) % self.capacity

        while True:
            if not self.hash_table[index]:
                self.hash_table[index] = [key, value]
                self.length += 1
                break
            if key == self.hash_table[index][0]:
                self.hash_table[index][1] = value
                break
            index = (index + 1) % self.capacity

    def __getitem__(self, key: object) -> object:
        index = hash(key) % self.capacity

        while True:
            if self.hash_table[index]:
                if key == self.hash_table[index][0]:
                    return self.hash_table[index][1]
            else:
                raise KeyError(f"No key '{key}' in dictionary.")

            index = (index + 1) % self.capacity

    def resize(self) -> None:

        current_hash_data = self.hash_table
        self.capacity *= 2
        self.threshold = int(2 / 3 * self.capacity) + 1
        self.hash_table = [[]] * self.capacity

        for cell in current_hash_data:
            if cell:
                self.__setitem__(cell[0], cell[1])

    def clear(self) -> object:
        return self.__init__()

    def __len__(self) -> int:
        result = 0
        for i in range(self.capacity):
            if self.hash_table[i]:
                result += 1
        return result
