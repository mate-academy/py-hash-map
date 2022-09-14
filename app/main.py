class Dictionary:
    def __init__(self, size=8):
        self.storage = [[] for _ in range(size)]
        self.size = size
        self.length = 0
        self.load_factor = 2 / 3

    def __setitem__(self, key, value):
        storage_idx = hash(key) % self.size

        self.length += 1
        if self.length >= self.load_factor * self.size:
            self.size *= 2
            self.resize(self.size, self.storage, key, value)

        while True:
            if not self.storage[storage_idx]:
                self.storage[storage_idx] = [key, value, hash(key)]
                break
            elif self.storage[storage_idx][0] == key:
                self.storage[storage_idx][1] = value
                self.length -= 1
                break
            storage_idx = (storage_idx + 1) % self.size

    def resize(self, size, storage, key, value):
        self.storage = [[] for _ in range(size)]
        for item in storage:
            if item:
                self.__setitem__(item[0], item[1])
                self.length -= 1

    def __getitem__(self, key):
        storage_idx = hash(key) % self.size
        while True:
            if not self.storage[storage_idx]:
                raise KeyError
            elif self.storage[storage_idx][0] == key:
                return self.storage[storage_idx][1]
            storage_idx = (storage_idx + 1) % self.size

    def __len__(self):
        return self.length

    def clear(self):
        self.storage = [[] for _ in range(self.size)]
        self.length = 0

    def __delitem__(self, key):
        remove_idx = hash(key) % self.size
        if key == self.storage[remove_idx][0]:
            self.storage[remove_idx] = []
            self.length -= 1

    def update(self, key, value):
        storage_idx = hash(key) % self.size
        if self.storage[storage_idx][0] == key:
            self.storage[storage_idx][1] = value

    def pop(self, key=-1):
        if self.storage[key]:
            value = self.storage[key][1]
            self.storage[key] = []
            return value

    def get(self, key, val=None):
        storage_idx = hash(key) % self.size
        if not self.storage[storage_idx]:
            return val
        elif self.storage[storage_idx]:
            return self.storage[storage_idx][1]

    def __iter__(self):
        for item in self.storage:
            if not item:
                continue
            for i in item:
                yield i
