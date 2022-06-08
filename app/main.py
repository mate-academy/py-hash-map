class Dictionary:
    def __init__(self):
        self.volume = 0
        self.size = 8
        self.table = [None for _ in range(self.size)]

    def __setitem__(self, key, value, hsh=None):
        if hsh is None:
            hsh = hash(key)
        i = hsh % self.size
        while True:
            if not self.table[i]:
                self.table[i] = [hsh, key, value]
                self.volume += 1
                break
            if self.table[i][1] == key:
                self.table[i][2] = value
                break
            i = (i + 1) % self.size
        if self.volume > int(self.size * 2 / 3):
            self.resize()

    def __getitem__(self, key):
        i = hash(key) % self.size
        for _ in range(self.size):
            if self.table[i][1] == key:
                return self.table[i][2]
            i = (i + 1) % self.size
        raise KeyError

    def resize(self):
        self.volume = 0
        self.size *= 2
        prev_dict = [cell for cell in self.table if cell]
        self.table = [None for _ in range(self.size)]
        for hsh, key, value in prev_dict:
            self.__setitem__(key, value, hsh)

    def __len__(self):
        return self.volume
