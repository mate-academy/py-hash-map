class Dictionary:

    def __init__(self, **kwargs):
        self.bucket_len = 0
        self.bucket_size = 8
        self.buckets = [None for _ in range(self.bucket_size)]
        for key, value in kwargs.items():
            self.__setitem__(key, value)

    def __getitem__(self, input_key):
        hashed_value = hash(input_key)
        index = hashed_value % self.bucket_size
        while self.buckets[index] is not None:
            key, value = self.buckets[index]
            if key == input_key:
                return value
            index = (index + 1) % self.bucket_size
        raise KeyError(f"{input_key} is missing")

    def __setitem__(self, input_key, input_value):
        self.resize()
        hashed_value = hash(input_key)
        index = hashed_value % self.bucket_size
        while True:
            if self.buckets[index] is None:
                self.buckets[index] = (input_key, input_value)
                self.bucket_len += 1
                break
            elif self.buckets[index][0] == input_key:
                self.buckets[index] = (input_key, input_value)
                break
            else:
                index = (index + 1) % self.bucket_size

    def resize(self):
        if self.bucket_len >= self.bucket_size * 2 / 3:
            self.bucket_len = 0
            self.bucket_size *= 2
            old = self.buckets.copy()
            self.buckets = [None for _ in range(self.bucket_size)]
            for item in old:
                if item is not None:
                    self.__setitem__(item[0], item[1])

    def __len__(self):
        return self.bucket_len
