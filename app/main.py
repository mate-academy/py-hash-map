class Dictionary:
    def __init__(self) -> None:
        self.dicts = []
        self.capacity = 8
        self.resize = None
        self.lens = 0

    def __setitem__(self, key: int, value: int) -> None:
        hash_key = hash(key)
        self.dicts.append([key, hash(key), value])
        for i, (k, h, v) in enumerate(self.dicts):
            if hash(key) == h and key == k and v != value:
                self.dicts[i] = [key, hash_key, value]
                return

        self.lens += 1

    def __getitem__(self, key: int) -> None:
        hash_key = hash(key)
        for k, h, v in self.dicts:
            if hash_key == h and key == k:
                return v
        raise KeyError(f"{key} , not found")

    def __len__(self) -> int:
        return self.lens

    def resize_(self) -> None:
        self.capacity = self.capacity * 2
        old_table = self.dicts
        self.dicts = [None] * self.capacity
        for item in old_table:
            if item:
                self.__setitem__(item[0], item[2])
