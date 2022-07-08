class Dictionary:
    def __init__(self):
        self.hash_table = [[] for _ in range(8)]
        self.capacity = 8

    def __setitem__(self, key, value):
        self._resize()
        hash_ = hash(key)
        index = hash_ % self.capacity
        while self.hash_table[index]:
            if self.hash_table[index][0] == hash_ and \
                    self.hash_table[index][1] == key:

                self.hash_table[index] = [hash_, key, value]
                break

            index = (index + 1) % self.capacity

        self.hash_table[index] = [hash_, key, value]

    def __getitem__(self, key):
        hash_ = hash(key)
        index = hash_ % self.capacity
        while self.hash_table[index]:
            if self.hash_table[index][1] == key and\
                    self.hash_table[index][0] == hash_:
                return self.hash_table[index][2]
            index = (index + 1) % self.capacity
        raise KeyError

    def __len__(self):
        temp_ls = []
        for item in self.hash_table:
            if item:
                temp_ls.append(item)
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
