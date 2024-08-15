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
            try:
                key = data[0]
                value = data[1]
            except Exception:
                print(key)
            index = hash(key) % (8 * self.k_hash_table)
            while True:
                if not (self.hash_table[index]):
                    break
                index += 1
            self.hash_table[index]  = [key, value, hash(key)]


    def __setitem__(self, key, value):
        print(f"Key = {key} Value = {value} Hash = {self.hash_table} Hash_key = {hash(key)}")
        if self.length > len(self.hash_table)* 2 / 3:
            self.update()

        index = hash(key) % (self.k_hash_table * 8)
        print("Index = ", index)
        while True:
            if not (self.hash_table[index]):
                break
            index += 1

        self.hash_table[index] = [key, value, hash(key)]
        self.length += 1


    def __getitem__(self, key):
        # print(f"Key = {key} Hash = {self.hash_table}")
        index = hash(key) % (self.k_hash_table * 8)
        try:
            return self.hash_table[index][1]
        except Exception:
            raise KeyError

    def __len__(self):
        return self.length
