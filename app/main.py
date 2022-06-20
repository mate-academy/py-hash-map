class Dictionary:
    def __init__(self):
        self.dict_len = 8
        self.element = [None] * self.dict_len

    def __setitem__(self, key, value):
        if len(self) == int(self.dict_len * 2 / 3):
            self.resize()

        hash_key = hash(key)
        new_el = (hash_key, key, value)  # store: hash, key, value
        i = hash_key % self.dict_len

        while True:
            if self.element[i] is None:
                self.element[i] = new_el
                break
            elif hash_key == self.element[i][0] and key == self.element[i][1]:
                self.element[i] = new_el
                break
            else:
                i = (i + 1) % self.dict_len

    def __getitem__(self, key):
        hash_key = hash(key)
        i = hash_key % self.dict_len

        if self.element[i] is None:
            raise KeyError

        while True:
            if self.element[i][0] == hash_key:
                return self.element[i][2]
            else:
                i = (i + 1) % self.dict_len

    def __len__(self):
        length = 0

        for i in range(self.dict_len):
            if self.element[i] is not None:
                length += 1

        return length

    def resize(self):
        new_dict_len = self.dict_len * 2
        new_dict = [None] * new_dict_len

        for i in range(self.dict_len):
            if self.element[i] is not None:
                j = self.element[i][0] % new_dict_len

                while True:
                    if new_dict[j] is None:
                        new_dict[j] = self.element[i]
                        break
                    else:
                        j = (j + 1) % new_dict_len

        self.dict_len = new_dict_len
        self.element = new_dict
