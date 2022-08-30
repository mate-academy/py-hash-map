class Dictionary:
    def __init__(self):
        self.__size = 0
        self.hash_table = [None] * 8

    def get_need_index(self, ind, key, hash_key):
        if self.hash_table[ind] is None:
            return ind
        if self.hash_table[ind][1] == hash_key \
                and self.hash_table[ind][0] == key:
            return ind
        need_item = [
            tup for tup in self.hash_table
            if tup is not None and tup[1] == hash_key and tup[0] == key]

        if len(need_item) > 0:
            return self.hash_table.index(need_item[0])

        for new_ind in range(ind + 1, len(self.hash_table)):
            if self.hash_table[new_ind] is None:
                return new_ind
        for new_ind in range(0, ind):
            if self.hash_table[new_ind] is None:
                return new_ind
        raise KeyError("Logical error")

    def resize(self):
        if len(self) >= len(self.hash_table) * 2 / 3:
            cash_hash_table = self.hash_table.copy()
            self.hash_table = [None] * len(cash_hash_table) * 2
            for item in cash_hash_table:
                if item is not None:
                    (key, hash_key, value) = item
                    ind = hash_key % len(self.hash_table)
                    if self.hash_table[ind] is None:
                        self.hash_table[ind] = (key, hash_key, value)
                        continue
                    new_index = self.get_need_index(ind, key, hash_key)
                    self.hash_table[new_index] = (key, hash_key, value)

    def __setitem__(self, key, value):
        hash_key = hash(key)
        try:
            ind = hash_key % len(self.hash_table)
        except TypeError:
            return
        new_index = self.get_need_index(ind, key, hash_key)
        self.hash_table[new_index] = (key, hash_key, value)
        self.__size = len([item for item in self.hash_table
                           if item is not None])
        self.resize()

    def __getitem__(self, item):
        hash_key = hash(item)
        ind = hash_key % len(self.hash_table)
        if self.hash_table[ind] is None:
            raise KeyError
        need_item = [
            tup for tup in self.hash_table
            if tup is not None and tup[1] == hash_key and tup[0] == item]
        if len(need_item) > 0:
            return need_item[0][2]
        raise KeyError("Invalid key")

    def __len__(self):
        return self.__size

    def clear(self):
        self.hash_table = [None] * 8

    def __delitem__(self, item):
        hash_key = hash(item)
        need_item = [
            tup for tup in self.hash_table
            if tup is not None and tup[1] == hash_key and tup[0] == item]
        if len(need_item) > 0:
            self.hash_table[self.hash_table.index(need_item[0])] = None
        else:
            raise KeyError

    def get(self, item):
        return self.__getitem__(item)

    def update(self):
        self.resize()
