class Dictionary:
    def __init__(self) -> str:
        self.keys = []
        self.values = []

    def __setitem__(self, key: int, value: str) -> None:
        if key in self.keys:
            index = self.keys.index(key)
            self.values[index] = value
        else:
            self.keys.append(key)
            self.values.append(value)

    def __getitem__(self, key: int) -> int:
        if key in self.keys:
            index = self.keys.index(key)
            return self.values[index]
        else:
            raise KeyError(key)

    def __len__(self) -> int:
        return len(self.keys)

    def dict_(self) -> str:
        capacity_n = len(self.keys) / 8 - len(self.keys) // 8
        if capacity_n >= 0:
            capacity = (8 * (len(self.keys) // 8 + 1))
        else:
            capacity = (8 * (len(self.keys) // 8))
        print(f"capacity = {capacity}")
        load_factor = len(self.keys) / capacity
        print(f"load factor = {load_factor}")
        resize = capacity * 2
        print(f"Resize = {resize}")

    def dict_list_nodes(self) -> list:
        nodes = []
        hashed_value = hash(self.key)
        nodes.append((self.key, hashed_value, self.value))
        print(nodes)
