class Dictionary:
    def __init__(self):
        self.length = 0
        self.capacity = 8
        self.buckets = [None] * self.capacity

    def _hashed_value_calculation(self, key):
        hashed_value = hash(key)
        return hashed_value % len(self.buckets)

    def _resize(self):
        self.length = 0
        old_buckets = self.buckets.copy()
        self.buckets = [None] * self.capacity * 2
        self.capacity *= 2
        for i in old_buckets:
            if i is not None:
                self.__setitem__(i[0], i[1])

    def __setitem__(self, key, value):
        index = self._hashed_value_calculation(key)
        while self.buckets[index] is not None:
            if key == self.buckets[index][0]:
                self.length -= 1
                break
            index = (index + 1) % self.capacity
        self.buckets[index] = (key, value)
        self.length += 1
        # check load factor
        if self.__len__() / self.capacity > 2 / 3:
            self._resize()

    def __getitem__(self, input_key):
        index = self._hashed_value_calculation(input_key)
        while self.buckets[index] is not None:
            key, value = self.buckets[index]
            if key == input_key:
                return value
            index = (index + 1) % self.capacity
        raise KeyError

    def __len__(self):
        return self.length

    def clear(self):
        self.length = 0
        self.buckets = [None] * self.capacity

    def __delitem__(self, input_key):
        index = self._hashed_value_calculation(input_key)
        while self.buckets[index] is not None:
            key, value = self.buckets[index]
            if key == input_key:
                self.buckets[index] = None
                self.length -= 1
                return None
            index = (index + 1) % self.capacity
        raise KeyError

    def get(self, input_key, args=None):
        index = self._hashed_value_calculation(input_key)
        while self.buckets[index] is not None:
            key, value = self.buckets[index]
            if key == input_key:
                return value
            index = (index + 1) % self.capacity
        return args

    def pop(self, input_key, args=None):
        index = self._hashed_value_calculation(input_key)
        while self.buckets[index] is not None:
            key, value = self.buckets[index]
            if key == input_key:
                for_returning = self.buckets[index][1]
                self.buckets[index] = None
                self.length -= 1
                return for_returning
            index = (index + 1) % self.capacity
        if args:
            return args
        raise KeyError

    def update(self, inp):
        for key in inp:
            self.__setitem__(key, inp.__getitem__(key))

    def __iter__(self):
        self.new_buckets = self.buckets.copy()
        self.current_element = 0
        self.new_buckets_length = self.capacity
        for _ in range(0, self.capacity - self.length):
            self.new_buckets.remove(None)
            self.new_buckets_length -= 1
        return self

    def __next__(self):
        if self.current_element >= self.new_buckets_length:
            raise StopIteration
        result = self.new_buckets[self.current_element]
        self.current_element += 1
        return result[0]
