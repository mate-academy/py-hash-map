from app.point import Point


class Dictionary:
    _BASE_CAPACITY = 8
    _LOAD_FACTOR = 2 / 3
    _RESIZE_FACTOR = 2

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
                for k in iterable:
                    self[k] = iterable[k]
            else:
                for k, v in iterable.items():
                    self[k] = v
        else:
            for k in kwargs:
                self[k] = kwargs[k]

    def _create_hash_table(self):
        self._hash_table = [
            [None, None]
            for i in range(self._capacity)
        ]

    def _resize_hash_table(self):
        self._capacity *= self._RESIZE_FACTOR
        old_table = self._hash_table
        self.clear()
        for key, value in old_table:
            if key is not None:
                self.__setitem__(key, value)

    def __delitem__(self, key):
        if self[key]:
            hash_index = hash(key) % self._capacity
            self._hash_table[hash_index] = [None, None]
            self._filled_slots -= 1
        else:
            raise KeyError("Key not found")

    def __getitem__(self, item):
        index = hash(item) % self._capacity
        while self._hash_table[index][1] is not None:
            key, value = self._hash_table[index]
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
        self._current_iter_index = 0

        return self

    def __len__(self):
        return self._filled_slots

    def __next__(self):
        if self._returned_iter_count < self._filled_slots:
            while self._hash_table[self._current_iter_index][0] is None:
                self._current_iter_index += 1
            value = self._hash_table[self._current_iter_index][0]
            self._returned_iter_count += 1
            self._current_iter_index += 1
            return value
        else:
            raise StopIteration

    def __repr__(self):
        result = []
        num = 0
        for item in self._hash_table:
            line = f"({num} {item[0]} {item[1]})"
            result.append(line)
            num += 1
        res_str = ", ".join(result)
        return "{" + res_str + "}"

    def __setitem__(self, key, value):
        index = hash(key) % self._capacity

        # find index of next free slot
        while self._hash_table[index][0] is not None:
            if self._hash_table[index][0] == key:
                self._filled_slots += 1
                break
            index += 1
            if index >= self._capacity - 1:
                index = 0

        self._hash_table[index][0] = key
        self._hash_table[index][1] = value
        self._filled_slots += 1
        if self._filled_slots > self._capacity * self._LOAD_FACTOR:
            self._resize_hash_table()

    def __str__(self):
        result = []

        for key, value in self._hash_table:
            if key is not None:
                if isinstance(key, str):
                    key = f"'{key}'"
                if isinstance(value, str):
                    value = f"'{value}'"
                line = f"{key}: {value}"
                result.append(line)

        result_str = ", ".join(result)
        return "{" + result_str + "}"


items = [("one", 1), ("two", 22), (145, -1), (Point(1, 1), "A")]
dictionary = Dictionary()
for key, value in items:
    dictionary[key] = value
print(repr(dictionary))
for key, value in items:
    print(dictionary[key], value)
