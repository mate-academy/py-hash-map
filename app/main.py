class Dictionary:
    """dict clone"""

    def __init__(self, key, value):  # mandatory
        self.key = key
        self.value = value

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

    def custom_hash(self):  # optional
        hash_capacity: int = 8
        hash_table: list = [None] * self.capacity

    def __repr__(self):  # optional
        return f"{{{self.key} : {self.value}}}"


def quick_prints():  # TODO: DELETE IT
    doppelganger = Dictionary(32, "asd")
    print(f"REPR EXAMPLE: {doppelganger}")
    print(doppelganger.__dict__)
    print(f"KEY: {doppelganger.key}")
    print(f"VALUE: {doppelganger.value}")
    print("____________________________")


if __name__ == '__main__':
    quick_prints()
