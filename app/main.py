class Dictionary:

    def __init__(self) -> None:
        self.length = 0
        self.hash_table = [None] * 8
        self.length_hash_table = 8

    def update(self):
        self.length_hash_table *= 2
        index = 0
        old_hash = self.hash_table
        self.hash_table = [None] * self.length_hash_table

        for data in old_hash:
            print("Data", data)
            try:
                key = data[0]
                value = data[1]
            except Exception:
                print(key)
            index = hash(key) % self.length_hash_table
            while True:
                if self.hash_table[index] is None:
                    break
                if index == self.length_hash_table - 1:
                    index = 0
                    continue
                index += 1



            self.hash_table[index]  = [key, value, hash(key)]


    def __setitem__(self, key, value):
        print(f"Key = {key} \nValue = {value} \nHash table= {self.hash_table} \nHash_key = {hash(key)}\n-------")
        if self.length > self.length_hash_table * 2 / 3:
            self.update()

        index = hash(key) % self.length_hash_table
        print("Index = ", index)
        while True:
            if self.hash_table[index] is None:
                break
            if index == self.length_hash_table - 1:
                index = 0
                continue
            index += 1

        self.hash_table[index] = [key, value, hash(key)]
        self.length += 1
        print(f"out Key = {self.hash_table[index][0]} \nValue = {self.hash_table[index][1]} \nHash table= {self.hash_table[index]} \nHash_key = {hash(key)}\n-------")


    def __getitem__(self, key):
        index = hash(key) % self.length_hash_table
        try:
            while True:
                print(f"Getitem Key = {hash(key)} \n Key in hash table = {self.hash_table[index][2]}")
                if self.hash_table[index][0] == key:
                    break
                if index == self.length_hash_table - 1:
                    index = 0
                    continue
                index += 1

            return self.hash_table[index][1]

        except Exception:
            raise KeyError

    def __len__(self):
        return self.length
