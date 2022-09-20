class Dictionary:
    def __init__(self):
        self.capacity = 8
        self.length = 0
        self.load = int(self.capacity * 2 / 3)
        self.tab = [[] for _ in range(self.capacity)]

    def __setitem__(self, key, value):
        # preparing index of tab
        hashed_key = hash(key)
        index = hashed_key % self.capacity
        while True:
            # if new key length increases
            if not len(self.tab[index]):
                self.tab[index] = [key, value, hashed_key]
                self.length += 1
                break
                # if key in dictionary
            if self.tab[index][0] == key and self.tab[index][2] == hashed_key:
                self.tab[index][1] = value
                break
            index = (index + 1) % self.capacity
        if self.length == self.load:
            self.resize()

    def resize(self):
        # getting new capacity and new length of tab
        self.capacity *= 2
        self.length = 0
        self.load = int(self.capacity * 2 / 3)
        # preparing old tab for iteration
        prep_tab = self.tab
        # creating new tab
        self.tab = [[] for _ in range(self.capacity)]
        # check
        for element in prep_tab:
            if len(element):
                self.__setitem__(element[0], element[1])

    def __len__(self):
        return self.length

    def __getitem__(self, key):
        # getting index of element
        index = hash(key) % self.capacity
        element = self.tab[index]
        while True:
            try:
                if element[0] == key and element[2] == hash(key):
                    return element[1]
            except IndexError:
                raise KeyError
            index = (index + 1) % self.capacity
            element = self.tab[index]

    def clear(self):
        self.capacity = 8
        self.length = 0
        self.load = int(self.capacity * 2 / 3)
        self.tab = [[] for _ in range(self.capacity)]

    def __iter__(self):
        self.it = 0
        self.arr = [element for element in self.tab if len(element)]
        return self
