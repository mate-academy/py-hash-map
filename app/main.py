class Dictionary:
    def __init__(self):
        self.length = 0
        self.hash_table = [[] for _ in range(8)]
        self.capacity = len(self.hash_table)

    def __setitem__(self, key, value):
        self._resize()
        index = hash(key) % self.capacity
        for _ in self.hash_table:
            if self.hash_table[index]:

                if hash(key) == self.hash_table[index][0] and key == self.hash_table[index][1]:
                    self.hash_table[index] = [hash(key), key, value]
                    break

                index += 1
                if index == len(self.hash_table):
                    index = 0

            else:
                self.hash_table[index] = [hash(key), key, value]
                self.length += 1
                break

    def __getitem__(self, key):
        index = hash(key) % self.capacity
        for _ in self.hash_table:
            if self.hash_table[index]:
                if self.hash_table[index][1] == key and self.hash_table[index][0] == hash(key):
                    return self.hash_table[index][2]
                index += 1
                if index == len(self.hash_table):
                    index = 0

        else:
            raise KeyError

    def __len__(self):
        temp_ls = []
        for i in self.hash_table:
            if i:
                temp_ls.append(i)
        return len(temp_ls)

    def _resize(self):
        size_to_resize = (self.capacity / 3) * 2
        if len(self) >= size_to_resize:
            temp_list = []
            for item in self.hash_table:
                if item:
                    temp_list.append(item)
            self.capacity *= 2
            self.hash_table = [[] for _ in range(self.capacity)]
            for el in temp_list:
                self[el[1]] = el[2]
