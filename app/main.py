class IsDeleted:
    def __str__(self):
        return "deleted"


class Dictionary:
    _BASE_CAPACITY = 8
    _LOAD_FACTOR = 2 / 3
    _RESIZE_FACTOR = 2
    _Is_Deleted = IsDeleted()

    def clear(self):
        self._filled_slots = 0
        self._create_hash_table()

    def get(self, key, default_value=None):
        try:
            return self[key]
        except KeyError:
            return default_value

    def pop(self, key, default_value=None):
        try:
            value = self[key]
        except KeyError:
            if default_value is None:
                raise
            value = default_value
        else:
            del self[key]

        return value

    def update(self, iterable=None, **kwargs):
        if iterable is not None:
            try:
                iterable.keys()
            except AttributeError:
                for key in iterable:
                    self[key] = iterable[key]
            else:
                for key, value in iterable.items():
                    self[key] = value
        else:
            for key in kwargs:
                self[key] = kwargs[key]

    def _create_hash_table(self):
        self._hash_table = [None for _ in range(self._capacity)]

    def _resize_hash_table(self):
        self._capacity *= self._RESIZE_FACTOR
        old_table = self._hash_table
        self.clear()
        for item in old_table:
            if item is not None and item != self._Is_Deleted:
                self.__setitem__(item[1], item[2])

    def __delitem__(self, key):
        if self[key]:
            index = hash(key) % self._capacity
            self._hash_table[index] = self._Is_Deleted
            self._filled_slots -= 1
        else:
            raise KeyError("Key not found")

    def __getitem__(self, item):
        index = hash(item) % self._capacity
        while self._hash_table[index] is not None:
            if item == self._Is_Deleted:
                index += 1
                continue
            hash_, key, value = self._hash_table[index]
            if hash_ == hash(item):
                if key == item:
                    return value
            index += 1
            if index >= self._capacity - 1:
                index = 0
        raise KeyError("Key not found")

    def __init__(self):
        self._capacity = self._BASE_CAPACITY
        self._filled_slots = 0
        self._create_hash_table()

    def __iter__(self):
        self._returned_iter_count = 0
        self._iter_index = 0
        return self

    def __len__(self):
        return self._filled_slots

    def __next__(self):
        if self._returned_iter_count < self._filled_slots:
            while True:
                item = self._hash_table[self._iter_index]
                if item is None or item == self._Is_Deleted:
                    self._iter_index += 1
                else:
                    break
            value = self._hash_table[self._iter_index][1]
            self._returned_iter_count += 1
            self._iter_index += 1
            return value
        else:
            raise StopIteration

    def __repr__(self):
        result = []
        for item in self._hash_table:
            result.append(str(item))
        res_str = ", ".join(result)
        return "{" + res_str + "}"

    def __setitem__(self, key, value):
        index = hash(key) % self._capacity

        while self._hash_table[index] is not None:
            if self._hash_table[index] == self._Is_Deleted:
                break
            if self._hash_table[index][0] == hash(key):
                if self._hash_table[index][1] == key:
                    break
            index += 1
            if index >= self._capacity - 1:
                index = 0
        else:
            self._filled_slots += 1

        self._hash_table[index] = (hash(key), key, value)
        if self._filled_slots > self._capacity * self._LOAD_FACTOR:
            self._resize_hash_table()

    def __str__(self):
        result = []
        for item in self._hash_table:
            if item is not None and item != self._Is_Deleted:
                _, key, value = item
                if isinstance(key, str):
                    key = f"'{key}'"
                if isinstance(value, str):
                    value = f"'{value}'"
                line = f"{key}: {value}"
                result.append(line)

        result_str = ", ".join(result)
        return "{" + result_str + "}"
