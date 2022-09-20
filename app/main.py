class Dictionary:
    def __init__(self):
        self.capacity = 8
        self.length = 0
        self.load = int(self.capacity * 2 / 3)
        self.table = [[] for _ in range(self.capacity)]

    def __setitem__(self, key, value):
        # preparing index of tab
        hashed_key = hash(key)
        index = hashed_key % self.capacity
        while True:
            # if new key length increases
            if self.table[index] == []:
                self.table[index] = [key, value, hashed_key]
                self.length += 1
                break
                # if key in dictionary
            if self.table[index][2] == hashed_key\
                    and self.table[index][0] == key:
                self.table[index][1] = value
                break
            index = (index + 1) % self.capacity
        if self.length == self.load:
            self.resize()

    def resize(self):
        # getting new capacity and new length of table
        self.capacity *= 2
        self.length = 0
        self.load = int(self.capacity * 2 / 3)
        # preparing old tab for iteration
        prep_table = self.table
        # creating new table
        self.table = [[] for _ in range(self.capacity)]
        # check
        for element in prep_table:
            if len(element):
                self.__setitem__(element[0], element[1])

    def __len__(self):
        return self.length

    def __getitem__(self, key):
        # getting index of element
        index = hash(key) % self.capacity
        element = self.table[index]
        while True:
            try:
                if element[2] == hash(key) and element[0] == key:
                    return element[1]
            except IndexError:
                raise KeyError
            index = (index + 1) % self.capacity
            element = self.table[index]

    def clear(self):
        self.capacity = 8
        self.length = 0
        self.load = int(self.capacity * 2 / 3)
        self.table = [[] for _ in range(self.capacity)]

    def __iter__(self):
        self.it = 0
        self.arr = [element for element in self.table if len(element)]
        return self
