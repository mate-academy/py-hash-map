class Dictionary:
    def __init__(self):
        self.hash_table = [[] for _ in range(8)]
        self.capacity = 8

    def __setitem__(self, key, value):
        self._resize()
        index = hash(key) % self.capacity
        while self.hash_table[index]:
            if self.hash_table[index][0] == hash(key) or \
                    self.hash_table[index][0] == key:
                self.hash_table[index] = [hash(key), key, value]
                break
            else:
                index = (index + 1) % self.capacity
        else:
            self.hash_table[index] = [hash(key), key, value]

    def __getitem__(self, key):
        index = hash(key) % self.capacity
        while self.hash_table[index]:
            if self.hash_table[index][1] == key and\
                    self.hash_table[index][0] == hash(key):
                return self.hash_table[index][2]
            else:
                index = (index + 1) % self.capacity
        else:
            raise KeyError

    def __len__(self):
        temp_ls = []
        for i in self.hash_table:
            if i:
                temp_ls.append(i)
        return len(temp_ls)

    def _resize(self):
        size_to_resize = round((self.capacity / 3) * 2)
        if len(self) >= size_to_resize:
            temp_list = []
            for item in self.hash_table:
                if item:
                    temp_list.append(item)
            self.capacity *= 2
            self.hash_table = [[] for _ in range(self.capacity)]
            for el in temp_list:
                self[el[1]] = el[2]


if __name__ == '__main__':
    dct = Dictionary()
    dct[1] = 11
    dct[2] = 12
    dct[3] = 13
    dct[4] = 14
    dct[5] = 15
    dct[5] = 555
    # dct[6] = 16
    # dct[7] = 17
    # dct[8] = 18
    # dct[9] = 19
    print(dct.hash_table)


