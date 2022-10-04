class Dictionary:
    def __init__(self):
        self.capacity = 8
        self.load_factor = 0.66
        self.list = [[] for _ in range(self.capacity)]

    def __setitem__(self, key, value):
        if len(self) + 1 > self.capacity * self.load_factor:
            self.increase_capacity()

        key_hash = hash(key) % self.capacity

        if not self.list[key_hash]:  # check if cell is empty
            self.list[key_hash] = [key, value, hash(key)]
            return

        for i in range(len(self.list)):  # check if we have key in self.list
            try:
                if self.list[i][0] == key:
                    self.list[i][1] = value
                    return
            except IndexError:
                pass

        while True:  # find and fill next empty cell
            if key_hash + 1 == self.capacity:
                key_hash = 0
            else:
                key_hash += 1
            if not self.list[key_hash]:
                self.list[key_hash] = [key, value, hash(key)]
                return

    def __getitem__(self, key):
        for i in range(len(self.list)):
            try:
                if key == self.list[i][0]:
                    return self.list[i][1]
            except IndexError:
                pass
        raise KeyError

    def __len__(self):
        count = 0
        for i in self.list:
            if i:
                count += 1
        return count

    def increase_capacity(self):
        old_list = [char for char in self.list if char]
        self.capacity *= 2
        self.list = [[] for _ in range(self.capacity)]
        for char in old_list:
            print(char, char[1])
            self[char[0]] = char[1]
