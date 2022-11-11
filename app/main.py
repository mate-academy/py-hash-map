class Dictionary:

    def __init__(self, key, value):  # hash imitation
        self.key = key
        self.value = value
        self.capacity = 8
        self.hash_table: list = [None] * self.capacity

        print(self.hash_table)

    def __setitem__(self, key, value):
        self.key = key
        self.value = value
        pass

    def __getitem__(self, item):
        pass

    def __len__(self):
        pass

    def __hash__(self):
        pass

    def __repr__(self):
        return f"{{{self.key} : {self.value}}}"


ex = Dictionary(key="qw", value="12")
print(Dictionary)
print(ex)

dicttest = {"qw": 12}
print(dicttest)
