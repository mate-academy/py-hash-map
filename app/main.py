class Dictionary:
    def __init__(self):
        self.length = 0   # len() value
        self.capacity = 8  # current capacity hash table
        self.buckets = [None] * self.capacity  # creating an empty hash table

    def _hashed_value_calculation(self, key):  # Calculating hash value
        hashed_value = hash(key)
        index = hashed_value % len(self.buckets)
        return index, hashed_value

    def _resize(self):  # hash table resizing
        self.length = 0
        old_buckets = self.buckets.copy()
        self.buckets = [None] * self.capacity * 2
        self.capacity *= 2
        for key_value in old_buckets:
            if key_value is not None:
                self.__setitem__(key_value[0], key_value[1])

    def __setitem__(self, key, value):
        index, hashed_value = self._hashed_value_calculation(key)
        # print("index = ", index, "hashed_value = ", hashed_value)
        while self.buckets[index] is not None:
            if key == self.buckets[index][0] and\
                    hashed_value == self.buckets[index][2]:
                self.length -= 1
                break
            index = (index + 1) % self.capacity
        self.buckets[index] = (key, value, hashed_value)
        self.length += 1
        # check load factor
        if self.__len__() / self.capacity > 2 / 3:
            self._resize()

    def __getitem__(self, input_key):
        index, input_hashed_value = self._hashed_value_calculation(input_key)
        while self.buckets[index] is not None:
            key, value, hashed_value = self.buckets[index]
            if key == input_key and hashed_value == input_hashed_value:
                return value
            index = (index + 1) % self.capacity
        raise KeyError

    def __len__(self):
        return self.length

    def clear(self):
        self.length = 0
        self.buckets = [None] * self.capacity

    def __delitem__(self, input_key):
        index, input_hashed_value = self._hashed_value_calculation(input_key)
        while self.buckets[index] is not None:
            key, value, hashed_value = self.buckets[index]
            if key == input_key and hashed_value == input_hashed_value:
                for_returning = self.buckets[index][1]
                self.buckets[index] = None
                self.length -= 1
                return for_returning
            index = (index + 1) % self.capacity
        raise KeyError

    def get(self, input_key, args=None):
        try:
            return self.__getitem__(input_key)
        except KeyError:
            return args

    def pop(self, input_key, args=None):
        try:
            return self.__delitem__(input_key)
        except KeyError:
            if args:
                return args
            raise KeyError

    def update(self, inp=None, **kwargs):
        if inp:
            for key in inp:
                self.__setitem__(key, inp.__getitem__(key))
        if kwargs:
            for k in kwargs:
                self[k] = kwargs[k]

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

    def __repr__(self):
        pairs = []
        for pair in self.buckets:
            if pair is not None:
                pairs.append(f"{pair[0]}: {pair[1]}")
        return "{" + ', '.join(pairs) + "}"
