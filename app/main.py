class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.hash_table = [None] * self.capacity
        self.load_factor = 2 / 3
        self.length = 0

    def __setitem__(self, key: any, value: any) -> None:
        if self.length == round(self.capacity * self.load_factor):
            self.resize_table()
        index = hash(key) % self.capacity
        for i in range(self.capacity):
            if index > self.capacity - 1:
                index -= self.capacity
            if self.hash_table[index] and self.hash_table[index][0] == key:
                self.hash_table[index] = (key, value)
                break
            elif not self.hash_table[index]:
                self.hash_table[index] = (key, value)
                self.length += 1
                break
            else:
                index += 1

    def __getitem__(self, key: any) -> None:
        index = hash(key) % self.capacity
        for i in range(self.capacity):
            if index > self.capacity - 1:
                index -= self.capacity

            if self.hash_table[index] and self.hash_table[index][0] == key:
                return self.hash_table[index][1]
            else:
                index += 1
        raise KeyError

    def __len__(self) -> int:
        return self.length

    def resize_table(self) -> None:
        old_hash_table = self.hash_table.copy()
        self.capacity *= 2
        self.hash_table = [None] * self.capacity
        self.length = 0
        for el in old_hash_table:
            if el:
                self.__setitem__(*el)

    def clear(self) -> None:
        self.__init__()

    def get(self, key: any, value: any = None) -> any:
        try:
            self.__getitem__(key)
        except KeyError:
            return value

    def update(self, iterable_value: dict) -> None:
        for key, value in iterable_value.items():
            self.__setitem__(key, value)
