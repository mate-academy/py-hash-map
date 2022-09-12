class Dictionary:
    def __init__(self, size=8):
        self.storage = [[] for _ in range(size)]
        self.size = size
        self.length = 0
        self.load_factor = 2 / 3

    def __setitem__(self, key, value):
        storage_idx = hash(key) % self.size
        for element in self.storage[storage_idx]:
            if key == element[0]:
                element[1] = value
                break
        else:
            self.storage[storage_idx].append([key, value])
            self.length += 1
            if self.length >= self.load_factor * self.size:
                self.size *= 2
                self.resize(self.size, self.storage)

    def resize(self, size, storage):
        self.storage = [[] for _ in range(size)]
        for item in storage:
            try:
                self.__setitem__(item[0][0], item[0][1])
                self.length -= 1
            except IndexError:
                continue

    def __getitem__(self, key):
        storage_idx = hash(key) % self.size
        for ele in self.storage[storage_idx]:
            if ele[0] == key:
                return ele[1]

        raise KeyError('Key {} dont exist'.format(key))

    def __len__(self):
        return self.length

    def clear(self):
        self.storage = [[] for _ in range(self.size)]
        return self.storage

    def __delitem__(self, key):
        remove_idx = hash(key) % self.size
        for element in self.storage[remove_idx]:
            if key == element[0]:
                self.storage[remove_idx].remove(element)
                self.length -= 1

    def update(self, key, value):
        storage_idx = hash(key) % self.size
        for ele in self.storage[storage_idx]:
            if ele[0] == key:
                ele[1] = value

    def pop(self, key=-1):
        try:
            value = self.storage[key][0][1]
            self.storage[key] = []
            return value
        except IndexError:
            print(f"No element by the key - {key}")

    def get(self, key, val=None):
        storage_idx = hash(key) % self.size
        if not self.storage[storage_idx]:
            return val
        for ele in self.storage[storage_idx]:
            if ele[0] == key:
                return ele[1]

    def __iter__(self):
        for item in self.storage:
            if not item:
                continue
            for i in item:
                yield i
