class Dictionary:

    def __init__(self):
        self.capacity = 8
        self.length = 0
        self.t_hold = int(self.capacity * (2 / 3))
        self.hash_table = [[] for _ in range(self.capacity)]

    def adding_item(self, key, value):
        hash_index = hash(key) % self.capacity
        if not self.hash_table[hash_index]:
            self.hash_table[hash_index].extend([key, value])
            self.length += 1
        else:
            i = 0
            while i < len(self.hash_table):
                if self.hash_table[i]:
                    if self.hash_table[i][0] == key:
                        self.hash_table[i] = [key, value]
                        break
                    else:
                        i += 1
                else:
                    i += 1
            if i == self.capacity:
                i = 0
                while self.hash_table[i]:
                    i += 1
                self.hash_table[i].extend([key, value])
                self.length += 1

    def __setitem__(self, key, value):
        if self.length < self.t_hold:
            self.adding_item(key, value)
        else:
            temporary_storage = self.hash_table
            print(temporary_storage)
            self.capacity *= 2
            self.length = 0
            self.hash_table = [[] for _ in range(self.capacity)]
            self.t_hold = int(self.capacity * (2 / 3))
            for item in temporary_storage:
                if item:
                    self.adding_item(item[0], item[1])
            self.adding_item(key, value)

    def __getitem__(self, key):
        i = 0
        while i <= len(self.hash_table):
            try:
                if self.hash_table[i][0] == key:
                    return self.hash_table[i][1]
                else:
                    i += 1
            except IndexError:
                i += 1
        raise KeyError

    def __len__(self):
        return self.length
