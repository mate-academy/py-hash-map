class Dictionary:
    def __init__(self):
        self.capacity = 8
        self.size = 0
        self.load_factor = self.capacity * 2 / 3
        self.hash_table = [None] * 8

    def resize_hash_table(self):
        self.capacity += 8
        self.size = 0
        self.load_factor = self.capacity * 2 / 3

        old_hash_table = self.hash_table

        new_resized_hash_table = [None] * self.capacity

        for entry in old_hash_table:
            if entry is not None:
                index = hash(entry[0]) % self.capacity

                if isinstance(new_resized_hash_table[index], list):
                    for _ in range(len(new_resized_hash_table)):
                        index = (index + 1) % len(new_resized_hash_table)
                        if new_resized_hash_table[index] is None:
                            new_resized_hash_table[index] = entry
                            self.size += 1
                            break
                new_resized_hash_table[index] = entry
                self.size += 1

        self.hash_table = new_resized_hash_table



    def __setitem__(self, key, value):
        index = hash(key) % self.capacity
        hash_table = self.hash_table

        if self.size > self.load_factor:
            self.resize_hash_table()
            hash_table = self.hash_table

        if self.size < self.load_factor and hash_table[index] is None:

            hash_table[index] = [key, value]
            self.size += 1

        elif hash_table[index] == "key":
            del hash_table[index]
            hash_table[index] = [key, value]

        elif isinstance(hash_table[index], list):
            for _ in range(len(hash_table)):
                index = (index + 1) % len(hash_table)
                if hash_table[index] is None:
                    hash_table[index] = [key, value]
                    self.size += 1
                    break

    def __getitem__(self, key):
        return key

    def __len__(self):
        return self.size
