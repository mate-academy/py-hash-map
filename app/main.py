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
