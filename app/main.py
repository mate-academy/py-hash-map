class Dictionary:
    hash_table = []
    len_hash_table = 8

    def __init__(self, value, key) -> None:
        # self.value = value
        # self.key = key
        # self.hask_key = hash(key)

    def __setitem__(self, key, value):
        if len(self.hash_table) > (self.len_hash_table * 2) / 3:
            self.len_hash_table *= 2

        index = hash(key) % self.len_hash_table
        while True:
            if not (self.hash_table[index]):
                break
            index += 1

        self.hash_table[index] = [key, value, hash(key)]

    def __getitem__(self, key):
        index = hash(key) % self.len_hash_table
        while True:
            if self.hash_table[index]:
                break
            index += 1
        return self.hash_table[index]

    def __len__(self):
        _len = 0
        for data in self.hash_table:
            if data:
                _len += 1
        return _len
