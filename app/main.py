class Dictionary:
    def __init__(self):
        self.volume = 0
        self.size = 8
        self.table = [None for _ in range(self.size)]

    def __setitem__(self, key, value):
        i = hash(key) % self.size
        if self.table[i] is None:
            self.table[i] = [hash(key), key, value]
            self.volume += 1
        else:
            if self.table[i][1] == key:
                self.table[i][2] = value
        if self.volume > int(self.size * 2 / 3):
            self.resize()

    def __getitem__(self, key):
        i = hash(key) % self.size
        for _ in range(self.size):
            if self.table[i] is not None:
                if self.table[i][1] == key:
                    return self.table[i][2]
                i = (i + 1) % self.size
            else:
                raise KeyError('Not found')

    def resize(self):
        self.volume = 0
        self.size *= 2
        prev_dict = [cell for cell in self.table if cell]
        self.table = [None for _ in range(self.size)]
        for hsh, key, value in prev_dict:
            i = hsh % self.size
            self.table[i] = [hsh, key, value]

    def __len__(self):
        return self.volume
