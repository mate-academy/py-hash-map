class Dictionary:
    def __init__(self):
        self.size = 2048
        self.table = [None] * self.size

    def __setitem__(self, key, value):
        self.table[hash(key) % self.size] = [hash(key), key, value]

    def __getitem__(self, key):
        if self.table[hash(key) % self.size] is not None:
            return self.table[hash(key) % self.size][2]
        else:
            raise KeyError

    def __len__(self):
        return self.table
