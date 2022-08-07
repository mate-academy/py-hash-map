import random


class Dictionary:

    def __init__(self):
        self.capacity = 8
        self.length = 0
        self.hash_table = [[] for _ in range(self.capacity)]
        self.free_indexes = [_ for _ in range(self.capacity)]
        self.t_hold = int(self.capacity * (2 / 3))

    def adding_item(self, key, value):
        hash_index = hash(key) % self.capacity
        if not self.hash_table[hash_index]:
            self.hash_table[hash_index].extend([key, value])
            self.length += 1
            self.free_indexes.remove(hash_index)
        else:
            if key in [item[0] for item in self.hash_table if item]:
                elt = [itm for itm in self.hash_table if itm and itm[0] == key]
                self.hash_table[self.hash_table.index(elt[0])] = [key, value]
            else:
                hash_index = random.choice(self.free_indexes)
                self.hash_table[hash_index].extend([key, value])
                self.length += 1
                self.free_indexes.remove(hash_index)

    def __setitem__(self, key, value):
        if self.length < self.t_hold:
            self.adding_item(key, value)
        else:
            temporary_storage = self.hash_table
            self.capacity *= 2
            self.length = 0
            self.hash_table = [[] for _ in range(self.capacity)]
            self.free_indexes = [_ for _ in range(self.capacity)]
            self.t_hold = int(self.capacity * (2 / 3))
            for item in temporary_storage:
                if item:
                    self.adding_item(item[0], item[1])
            self.adding_item(key, value)

    def __getitem__(self, key):
        hash_table_out_empty = [item for item in self.hash_table if item]
        value = [item[1] for item in hash_table_out_empty if item[0] == key]
        if value:
            return value[0]
        raise KeyError

    def __len__(self):
        return self.length
