class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.hash_table: list = [None] * 8

    def __getitem__(self, key):
        hash_key = hash(key)
        index = hash_key % len(self.hash_table)

        if self.hash_table[index] and self.hash_table[index][0] == key:
            return self.hash_table[index][1]
        else:
            for item in self.hash_table:
                if item and item[0] == key:
                    return item[1]

        raise KeyError

    def __setitem__(self, key, value):
        if self.length > len(self.hash_table) * 2 / 3:
            self.extend_hash_table()

        hash_key = hash(key)
        item = (key, value, hash_key)
        index = hash_key % len(self.hash_table)

        if self.hash_table[index] and self.hash_table[index][0] == key:
            self.hash_table[index] = (key, value, hash_key)
        else:
            while self.hash_table[index]:
                index = index + 1 if index != len(self.hash_table) - 1 else 0

            self.hash_table[index] = item
            self.length += 1

    def extend_hash_table(self):
        extending = [None] * len(self.hash_table)
        self.hash_table += extending

        for i in range(len(self.hash_table) // 2):
            if self.hash_table[i]:
                item = self.hash_table[i]
                self.hash_table[i] = None
                key, value, hash_key = item
                new_index = hash_key % len(self.hash_table)

                while self.hash_table[new_index]:
                    new_index = new_index + 1 if new_index != len(self.hash_table) - 1 else 0

                self.hash_table[new_index] = item

    def __len__(self) -> int:
        return self.length


d = Dictionary()
# d[1] = "a"
# d[9] = "b"
# d[124] = "c"
# d[14] = "d"
# d[15] = "e"
# d[0] = "f"
# d[10] = "g"

# d["one"] = 1
# d["two"] = 2
# d["tree"] = 3
# d["four"] = 4
#
# print(d["one"])
# print(d["two"])
# print(d["tree"])
# print(d["four"])

print(d.hash_table)

