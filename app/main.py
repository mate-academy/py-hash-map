class Dictionary:
    def __init__(self):
        self.buckets = [None] * 8

    def _hashed_value_calculation(self, key):
        hashed_value = hash(key)
        return hashed_value % len(self.buckets)

    def _resize(self):
        old_buckets = self.buckets.copy()
        self.buckets = [None] * len(self.buckets) * 2
        for i in old_buckets:
            if i is not None:
                self.__setitem__(i[0], i[1])

    def __setitem__(self, key, value):
        index = self._hashed_value_calculation(key)
        while self.buckets[index] is not None:
            if key == self.buckets[index][0]:
                break
            index = (index + 1) % len(self.buckets)
        self.buckets[index] = (key, value)
        # check load factor
        if self.__len__() / len(self.buckets) > 2 / 3:
            self._resize()

    def __getitem__(self, input_key):
        index = self._hashed_value_calculation(input_key)
        while self.buckets[index] is not None:
            key, value = self.buckets[index]
            if key == input_key:
                return value
            index = (index + 1) % len(self.buckets)
        raise KeyError

    def __len__(self):
        return len(self.buckets) - self.buckets.count(None)

    def clear(self):
        self.__init__()

    def __delitem__(self, input_key):
        index = self._hashed_value_calculation(input_key)
        while self.buckets[index] is not None:
            key, value = self.buckets[index]
            if key == input_key:
                self.buckets[index] = None
                return None
            index = (index + 1) % len(self.buckets)
        raise KeyError

    def get(self, input_key, args=None):
        index = self._hashed_value_calculation(input_key)
        while self.buckets[index] is not None:
            key, value = self.buckets[index]
            if key == input_key:
                return value
            index = (index + 1) % len(self.buckets)
        return args

    def pop(self, input_key, args=None):
        index = self._hashed_value_calculation(input_key)
        while self.buckets[index] is not None:
            key, value = self.buckets[index]
            if key == input_key:
                for_returning = self.buckets[index][1]
                self.buckets[index] = None
                return for_returning
            index = (index + 1) % len(self.buckets)
        if args:
            return args
        else:
            raise KeyError

    def update(self, inp):
        for key in inp:
            self.__setitem__(key, inp.__getitem__(key))

    def __iter__(self):
        self.new_buckets = self.buckets.copy()
        self.current_element = 0
        for _ in range(0, self.buckets.count(None)):
            self.new_buckets.remove(None)
        return self

    def __next__(self):
        if self.current_element >= len(self.new_buckets):
            raise StopIteration
        result = self.new_buckets[self.current_element]
        self.current_element += 1
        return result[0]
