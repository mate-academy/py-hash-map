class Dictionary:

    INITIAL_SIZE = 8
    LOAD_FACTOR = 2 / 3
    RESIZE_FACTOR = 2

    def __init__(self, elements=None):
        self.size = self.INITIAL_SIZE
        self.buckets = [[] for _ in range(self.size)]
        if elements:
            for key, value in elements:
                self.__setitem__(key, value)

    def __setitem__(self, key, value):
        hashed_value = hash(key)
        bucket = self.buckets[hashed_value % self.size]

        # rewrite the value of existing key:
        for ind, element in enumerate(bucket):
            if element[0] == key:
                bucket[ind] = (key, hashed_value, value)
                break

        # create new key-value pair and check for the need to resize
        if (key, hashed_value, value) not in bucket:
            fullness = (sum(1 for el in self.buckets if el) + 1) / self.size
            if fullness >= self.LOAD_FACTOR:
                buckets_content = sum(self.buckets, [])
                buckets_content.append((key, hashed_value, value))
                self.clear()
                self.size *= self.RESIZE_FACTOR
                self.buckets = [[] for _ in range(self.size)]
                for key, hashed_value, value in buckets_content:
                    self.__setitem__(key, value)
            else:
                bucket.append((key, hashed_value, value))

    def __getitem__(self, key):
        hashed_value = hash(key)
        bucket = self.buckets[hashed_value % self.size]
        for current_key, hashed_value, value in bucket:
            if current_key == key:
                return value
        raise KeyError

    def __len__(self):
        return len(sum(self.buckets, []))

    def clear(self):
        self.buckets = [[] for _ in range(self.size)]

    def __delitem__(self, key):
        hashed_value = hash(key)
        bucket = self.buckets[hashed_value % self.size]
        for el in bucket:
            if el[0] == key:
                bucket.remove(el)

    def get(self, key, def_value=None):
        hashed_value = hash(key)
        bucket = self.buckets[hashed_value % self.size]
        for current_key, hashed_value, value in bucket:
            if current_key == key:
                return value
        return def_value

    def pop(self, key, def_value=None):
        hashed_value = hash(key)
        bucket = self.buckets[hashed_value % self.size]
        for el in bucket:
            if el[0] == key:
                val_to_return = el[2]
                bucket.remove(el)
                return val_to_return
        return def_value

    def update(self, to_add):
        for key, hashed_value, value in sum(to_add.buckets, []):
            self.__setitem__(key, value)

    def __iter__(self):
        self.curr_ind = 0
        self.curr_inner_ind = 0
        return self

    def __next__(self):
        while self.curr_ind < len(self.buckets):
            while self.curr_inner_ind < len(self.buckets[self.curr_ind]):
                try:
                    result = self.buckets[self.curr_ind][self.curr_inner_ind]
                except IndexError:
                    pass
                else:
                    return result[0]
                finally:
                    self.curr_inner_ind += 1
            self.curr_ind += 1
            self.curr_inner_ind = 0
        raise StopIteration
