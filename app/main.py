class Dictionary:

    def __init__(self):
        self.key = None
        self.value = None
        self.capacity = 8
        self.threshold = 5
        self.non_empty = 0
        self.dict = [None for _ in range(self.capacity)]

    def __setitem__(self, key, value):
        self.key = key
        self.value = value
        self.hash = self.__hash__()
        self.add_to_dict()

    def __getitem__(self, key):
        for item in self.dict:
            if type(item) is list and item[0] == key:
                return item[1]
        raise KeyError

    def __repr__(self):
        return f"{{{self.key}: {self.value}}}"

    def choose_index(self):
        index = self.hash % self.capacity
        if not any(self.dict):
            self.dict[index] = [self.key, self.value, self.hash]
            self.non_empty += 1
            return
        for index in range(len(self.dict)):
            if type(self.dict[index]) is list:
                if self.dict[index][0] == self.key:
                    self.dict[index][1] = self.value
                    return
        if self.dict[index]:
            for index_after in range(index + 1, self.capacity):
                if not self.dict[index_after]:
                    index = index_after
                    self.dict[index] = [self.key, self.value, self.hash]
                    self.non_empty += 1
                    return
            for index_before in range(index):
                if not self.dict[index_before]:
                    index = index_before
                    self.dict[index] = [self.key, self.value, self.hash]
                    self.non_empty += 1
                    return
        self.dict[index] = [self.key, self.value, self.hash]

    def add_to_dict(self):
        self.choose_index()
        if self.non_empty == self.threshold:
            self.capacity *= 2
            self.threshold = int(self.capacity * (2 / 3))
            all_items = [item for item in self.dict if item]
            self.dict = [None for _ in range(self.capacity)]
            for item in all_items:
                self.key = item[0]
                self.value = item[1]
                self.add_to_dict()

    def __hash__(self):
        return hash((self.key, self.value))

    def __len__(self):
        return sum(1 for item in self.dict if type(item) is list)
