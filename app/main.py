class Dictionary:
    def __init__(self, size=1000):
        self.storage = [[] for _ in range(size)]
        self.size = size
        self.length = 0

    def __setitem__(self, key, value):
        storage_idx = hash(key) % self.size
        for ele in self.storage[storage_idx]:
            if key == ele[0]:
                ele[1] = value
                break
        else:
            self.storage[storage_idx].append([key, value])
            self.length += 1

    def __getitem__(self, key):
        storage_idx = hash(key) % self.size
        for ele in self.storage[storage_idx]:
            if ele[0] == key:
                return ele[1]

        raise KeyError('Key {} dont exist'.format(key))

    def __len__(self):
        return self.length
