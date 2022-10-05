class Dictionary:
    def __init__(self, capacity: int = 8) -> None:
        self.capacity = capacity
        self.load_factor = 0.67
        self.buckets = [[] for _ in range(self.capacity)]

    def __is_full(self):
        fullness = sum(1 for bucket in self.buckets if bucket)
        return fullness >= (self.capacity * self.load_factor)

    def __resizer(self):
        self.capacity *= 2

        instance = Dictionary(capacity=self.capacity)
        for i in range(len(self.buckets)):
            if not self.buckets[i]:
                continue

            for entry in self.buckets[i]:
                instance.__setitem__(entry[0], entry[1])

        self.buckets = instance.buckets

    def __setitem__(self, key, value):
        if self.__is_full():
            self.__resizer()
        index = hash(key) % self.capacity

        for bucket in self.buckets[index]:
            if bucket[0] == key:
                bucket[1] = value
                break
        else:
            self.buckets[index].append([key, value])

    def __getitem__(self, key):
        index = hash(key) % self.capacity
        if self.buckets[index] == []:
            raise KeyError()
        else:
            for stored_pair in self.buckets[index]:
                if stored_pair[0] == key:
                    return stored_pair[1]
            raise KeyError()

    def __len__(self):
        counter = 0
        for stored_pair in self.buckets:
            if stored_pair:
                counter += len(stored_pair)
        return counter
