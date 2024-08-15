class Dictionary:

    def __init__(self) -> None:
        self.length = 0
        self.hash_table = [None] * 8
        self.k_hash_table = 1

    def update(self):
        self.k_hash_table += 1
        index = 0
        old_hash = self.hash_table
        self.hash_table = [None] * 8 * self.k_hash_table

        for data in old_hash:
            key, value = data[0], data[1]
            index = hash(key) % (8 * self.k_hash_table)
            while True:
                if not (self.hash_table[index]):
                    break
                index += 1
            self.hash_table[index]  = [key, value, hash(key)]


    def __setitem__(self, key, value):
        print(f"Key = {key} Value = {value} Hash = {self.hash_table}")
        if self.length > len(self.hash_table)* 2 / 3:
            self.update()

        index = hash(key) % (self.k_hash_table * 8)
        while True:
            if not (self.hash_table[index]):
                break
            index += 1

        self.hash_table[index] = [key, value, hash(key)]
        self.length += 1


    def __getitem__(self, key):
        print(f"Key = {key} Value = {value} Hash = {self.hash_table}")
        index = hash(key) % (self.k_hash_table * 8)
        return self.hash_table[index][1]

    def __len__(self):
        return self.length
