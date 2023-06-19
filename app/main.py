class Dictionary:
    """dict clone"""

    def __init__(self, key, value): # mandatory
        self.key = key
        self.value = value
        self.capacity = 8
        self.hash_table: list = [None] * self.capacity

        print(self.hash_table)

    def __setitem__(self, key, value):  # mandatory
        self.key = key
        self.value = value
        pass

    def __getitem__(self, key):  # mandatory
        pass

    def __len__(self):  # mandatory
        pass

    def clear(self):  # extra
        pass

    def __delitem__(self, key):  # extra
        pass

    def get(self):  # extra
        pass

    def pop(self):  # extra
        pass

    def update(self):  # extra
        pass

    def __iter__(self):  # extra
        pass

    def hash(self):  # optional
        pass

    def __repr__(self):  # optional
        return f"{{{self.key} : {self.value}}}"
