class Dictionary:
    def __init__(self):
        self.capacity = 8
        self.hash_table = [None for _ in range(self.capacity)]
        self.size = 0

    def __getitem__(self, item):
        index = hash(item) % self.capacity

        for _ in range(2):
            for i in range(self.capacity):
                if index + i == self.capacity:
                    index = 0
                if self.hash_table[index + i] is not None:
                    if self.hash_table[index + i][0] == item:
                        return self.hash_table[index + i][-1]
        raise KeyError

    def __setitem__(self, key, value):
        self.resize()

        hash_table_index = hash(key) % self.capacity
        while True:
            if hash_table_index == self.capacity:
                hash_table_index = 0

            if self.hash_table[hash_table_index] is not None:
                if self.hash_table[hash_table_index][1] == hash_table_index:
                    if self.hash_table[hash_table_index][0] == key:
                        self.hash_table[hash_table_index] = None
                        self.size -= 1

                    else:
                        hash_table_index += 1
            else:
                break

        self.hash_table[hash_table_index] = (key, hash_table_index, value)
        self.size += 1

    def __len__(self):
        return self.size

    def __repr__(self):
        return str(
            {key[0]: key[-1] for key in self.hash_table if key is not None}
        )

    def resize(self):
        if self.size > self.capacity * 2 / 3:
            self.capacity *= 2
            copy_hash_table = self.hash_table.copy()

            self.hash_table = [None] * self.capacity

            for index, elem in enumerate(copy_hash_table):
                while True:
                    if index == self.capacity:
                        index = 0

                    if self.hash_table[index] is not None:
                        index += 1
                    else:
                        break

                self.hash_table[index] = elem
