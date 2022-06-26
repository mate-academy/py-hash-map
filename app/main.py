class Dictionary:

    def __init__(self):
        self.dic = [[] for _ in range(8)]
        self.initial_capacity = len(self.dic)
        self.load_factor = 0

    def __setitem__(self, key, value):
        new_key = True
        hash_ = hash(key)
        for element in self.dic:
            if element:
                if element[0][0] == key:
                    element.clear()
                    element.append((key, hash_, value))
                    new_key = False
        if new_key:
            if self.load_factor >= 2 / 3 * self.initial_capacity:
                self.resize()
            index = hash_ % self.initial_capacity
            while self.dic[index]:
                index = (index + 1) % self.initial_capacity
            self.dic[index].append((key, hash_, value))
            self.load_factor += 1

    def __len__(self):
        return self.load_factor

    def resize(self):
        new_list = [[] for _ in range(self.initial_capacity * 2)]
        self.initial_capacity = len(new_list)
        for element in self.dic:
            if element:
                new_index = element[0][1] % self.initial_capacity
                while new_list[new_index]:
                    new_index = (new_index + 1) % self.initial_capacity
                new_list[new_index].append(element[0])
        self.dic = new_list

    def __getitem__(self, key):
        for element in self.dic:
            if element:
                if element[0][0] == key:
                    return element[0][2]
        raise KeyError
