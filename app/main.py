class Dictionary:
    def __init__(self) -> None:
        self.hash_table = [[] for _ in range(8)]
        self.length = 0

    def __setitem__(self, key: object, value: object) -> None:
        index = hash(key) % 8
        for data in self.hash_table[index]:
            if data[0] == key:
                data[1] = value
                return
        self.hash_table[index].append([key, value])
        self.length += 1

    def __getitem__(self, key: object) -> None:
        index = hash(key) % 8
        for data in self.hash_table[index]:
            if data[0] == key:
                return data[1]
        raise KeyError(f"Key {key} does not exist")

    def __len__(self) -> int:
        return self.length
