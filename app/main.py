class Dictionary:
    def set_hash_table_index(self, key_hash):
        self._hash_table_index = key_hash % self.capacity

    def increase_hash_table_index_by_one(self):
        self._hash_table_index += 1
        self._hash_table_index %= self.capacity

    def return_threshold(self):
        return int(self.capacity * 2 / 3)

    def setup_hash_table(self):
        return [[] for _ in range(self.capacity)]

    def clear_hash_table_cell(self):
        self.hash_table[self._hash_table_index] = []

    def hash_table_index_for_key_hash(self, key_hash):
        return key_hash % self.capacity

    def write_to_hash_table(self, hash_table_index, item):
        self.hash_table[hash_table_index] = item

    def is_hash_table_cell_empty(self):
        if self.hash_table[self._hash_table_index]:
            return False
        return True

    def are_keys_equal(self, key):
        if key == self.hash_table[self._hash_table_index][0]:
            return True
        return False

    def update_hash_table_value(self, hash_table_index, item):
        self.hash_table[hash_table_index][2] = item[2]

    def extend_hash_table(self):
        temp_values = self.hash_table.copy()
        self.capacity *= 2
        self.threshold = self.return_threshold()

        print(f"capacity: {self.capacity}, threshold: {self.threshold}")

        self.hash_table = self.setup_hash_table()

        # fill new hash table
        for item in temp_values:
            if item:
                self.set_hash_table_index(item[1])

                while True:
                    if self.is_hash_table_cell_empty():
                        self.write_to_hash_table(self._hash_table_index, item)
                        break

                    self.increase_hash_table_index_by_one()

    def __init__(self):
        self.capacity = 8
        self.threshold = self.return_threshold()
        self._size = 0
        self.hash_table = self.setup_hash_table()
        self._hash_table_index = None

    def __setitem__(self, key, value):
        key_hash = hash(key)
        item = [key, key_hash, value]
        self.set_hash_table_index(key_hash)

        while True:
            if self.is_hash_table_cell_empty():
                self.write_to_hash_table(self._hash_table_index, item)
                self._size += 1
                break

            if self.are_keys_equal(key):
                self.update_hash_table_value(self._hash_table_index, item)
                break

            self.increase_hash_table_index_by_one()

        if self._size == self.threshold:
            self.extend_hash_table()

    def __getitem__(self, key):
        self.set_hash_table_index(hash(key))

        if not self.is_hash_table_cell_empty():
            while True:
                if self.are_keys_equal(key):
                    return self.hash_table[self._hash_table_index][2]
                    break

                self.increase_hash_table_index_by_one()
        else:
            raise KeyError

    def __len__(self):
        return self._size

    def clear(self):
        self.hash_table = self.setup_hash_table()

    def __delitem__(self, key):
        self.set_hash_table_index(hash(key))

        if not self.is_hash_table_cell_empty():
            while True:
                if self.are_keys_equal(key):
                    self.clear_hash_table_cell()
                    self._size -= 1
                    break

                self.increase_hash_table_index_by_one()
        else:
            raise KeyError

    def get(self, key, default=None):
        self.set_hash_table_index(hash(key))

        if not self.is_hash_table_cell_empty():
            while True:
                if self.are_keys_equal(key):
                    return self.hash_table[self._hash_table_index][2]

                self.increase_hash_table_index_by_one()
        else:
            return default

    def pop(self, key, default=None):
        self.set_hash_table_index(hash(key))

        if not self.is_hash_table_cell_empty():
            while True:
                if self.are_keys_equal(key):
                    result = self.hash_table[self._hash_table_index][2]
                    self.clear_hash_table_cell()
                    self._size -= 1
                    return result

                self.increase_hash_table_index_by_one()
        else:
            return default

    def __repr__(self):
        result = "{"
        items = []
        for item in self.hash_table:
            if item:
                items.append(f"{item[0]}: {item[2]}")
        result += ", ".join(items) + "}"
        return result
