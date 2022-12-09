class Dictionary:
    def __init__(self):
        self.length = 0
        self.size = 8
        self.hash_table: list = [[] for _ in range(self.size)]

    def __setitem__(self, key, value):
        index = hash(key) % self.size
        if self.hash_table[index]:
            for item in self.hash_table[index]:
                if item[0] == key and hash(item[0]) == hash(key):
                    item[1] = value
                    return
        self.hash_table[index].append([key, value])
        self.length += 1

    def resize(self):
        self.size += 2
        temp_list = []
        for container in self.hash_table:
            for item in container:
                temp_list.append(item)
        for item in temp_list:
            self.__setitem__(*item)

    def __getitem__(self, key):
        index = hash(key) % self.size
        if not self.hash_table[index]:
            raise KeyError
        for item in self.hash_table[index]:
            if item[0] == key:
                return item[1]

    def __len__(self):
        return self.length
