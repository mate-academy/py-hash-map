import random


class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.len_hash_table = 8
        self.hash_table: list = [None] * self.len_hash_table

    def __len__(self) -> int:
        return self.length

    @staticmethod
    def hash(value: str) -> int:
        random.seed(42)
        return sum(ord(char) + random.randint(0, 100) for char in value)

    def resize(self):

        threshold = int(self.len_hash_table * 0.66)
        if self.length >= threshold:

            self.len_hash_table *= 2
            self.length = 0
            new_hash_table = [None] * self.len_hash_table

            for data in self.hash_table:
                if data is not None:
                    key, value = data
                    index_hash = hash(key) % self.len_hash_table

                    while new_hash_table[index_hash] is not None:
                        index_hash += 1
                        if index_hash >= self.len_hash_table:
                            index_hash = 0

                    new_hash_table[index_hash] = (key, value)
                    self.length += 1
            self.hash_table = new_hash_table

    def __setitem__(self, key, value):

        hash_key = hash(key)
        index_hash = hash_key % self.len_hash_table

        while self.hash_table[index_hash] is not None:
            if self.hash_table[index_hash][0] == key:
                self.hash_table[index_hash] = (key, value)
                return
            index_hash += 1
            if index_hash >= self.len_hash_table:
                index_hash = 0

        self.hash_table[index_hash] = (key, value)
        self.length += 1

        self.resize()

    def __getitem__(self, key):

        hash_key = hash(key)
        index_hash = hash_key % self.len_hash_table

        while self.hash_table[index_hash][0] != key:
            index_hash += 1
            if index_hash >= self.len_hash_table:
                index_hash = 0

        output = self.hash_table[index_hash][1]

        return output
