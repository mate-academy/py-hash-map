class Dictionary:
    """dict clone"""


    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.capacity = 8
        self.hash_table: list = [None] * self.capacity

        print(self.hash_table)

    def __setitem__(self, key, value):  # mandatory
        self.key = key
        self.value = value
        pass

    def __getitem__(self, key):
        pass

    def __len__(self):
        pass

    def __hash__(self):

        def __repr__(self):
            return f"{{{self.key} : {self.value}}}"

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
