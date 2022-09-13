class Dictionary:

    def __init__(self):
        self.capacity = 8
        self.length = 0
        self.hash = [None for _ in range(self.capacity)]

    def __len__(self):
        return self.length

    def __setitem__(self, key, value):
        if self.length >= self.capacity * 0.66:
            self.capacity *= 2
            self.length = 0
            old_list = self.hash
            self.hash = [None for _ in range(self.capacity)]
            for item in old_list:
                if item:
                    self.__setitem__(item[0], item[2])
        hashed = hash(key)
        index = hashed % self.capacity
        while True:
            if not self.hash[index]:
                self.hash[index] = [key, hashed, value]
                self.length += 1
                break
            if self.hash[index][0] == key and\
                    self.hash[index][1] == hashed:
                self.hash[index][2] = value
                break
            index = (index + 1) % self.capacity

    def __getitem__(self, key):
        hashed = hash(key)
        index = hashed % self.capacity
        while self.hash[index]:
            if self.hash[index][1] == hashed \
                    and self.hash[index][0] == key:
                return self.hash[index][2]
            index = (index + 1) % self.capacity
        raise KeyError(key)
