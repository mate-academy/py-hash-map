class Dictionary:

    def __init__(self):
        self.capacity = 8
        self.load_factor = 2 / 3
        self.buckets = self.create_table()

    def __setitem__(self, key, value):
        hash_code = hash(key)
        index = int(hash_code % self.capacity)
        fill_cell = self.calc_fill_cell()
        if self.capacity / fill_cell > self.load_factor:
            self.resize()
        while self.buckets[index] is not None:
            index = (index + 1) % self.capacity
        self.buckets[index] = [hash_code, key, value]

    def __getitem__(self, input_key):
        hash_code = hash(input_key)
        index = hash_code % self.capacity
        while self.buckets[index] is not None:
            hash_x, key, value = self.buckets[index]
            if hash_x == hash_code and input_key == key:
                return self.buckets[index][2]
            index = (index + 1) % self.capacity

    def __len__(self):
        return self.calc_fill_cell()

    def resize(self):
        self.capacity *= 2
        copy_elements = self.buckets.copy()
        self.buckets = self.create_table()
        for cell in copy_elements:
            self.__setitem__(cell[1], cell[2])
        del copy_elements

    def create_table(self):
        buckets = [[None] for _ in range(self.capacity)]
        return buckets

    def calc_fill_cell(self):
        res = 0
        for elem in self.buckets:
            if elem is not None:
                res += 1
        return res
