class Dictionary:
    def __init__(self):
        self.length = 0
        self.capacity = 8
        self.load_factor = 2 / 3
        self.threshold = self.capacity * self.load_factor
        self.hash_table = [[]for _ in range(self.capacity)]

    def __setitem__(self, key, value):
        if self.length > self.threshold:
            self.capacity *= 2
            self.threshold = self.capacity * self.load_factor
            prev_list = [item for item in self.hash_table if item]
            self.hash_table = [[] for _ in range(self.capacity)]
            for item in prev_list:
                index = item[0] % self.capacity
                while True:
                    if len(self.hash_table[index]) > 0:
                        index = (index + 1) % self.capacity
                    else:
                        self.hash_table[index] = item
                        break
        else:
            self.add_new_element(key, value)

    def __getitem__(self, item):
        hashed_value = hash(item)
        index = hashed_value % self.capacity
        while self.hash_table[index]:
            if self.hash_table[index][1] == item \
                    and self.hash_table[index][0] == hashed_value:
                return self.hash_table[index][2]
            index = (index + 1) % self.capacity
        raise KeyError

    def add_new_element(self, key, value):
        hashed_value = hash(key)
        index = hashed_value % self.capacity
        while True:
            if len(self.hash_table[index]) == 0:
                self.hash_table[index] = [hashed_value, key, value]
                self.length += 1
                break
            else:
                if key == self.hash_table[index][1]:
                    self.hash_table[index] = [hashed_value, key, value]
                    break
            index = (index + 1) % self.capacity

    def __len__(self):
        return self.length
