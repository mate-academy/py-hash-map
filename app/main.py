from app.point import Point


class Dictionary:
    def __init__(self):
        self.initial_capacity = 8
        self.load_factor = int(self.initial_capacity * (2 / 3))
        self.dict_data = [False for _ in range(8)]
        self.dict_len = 0

    def __setitem__(self, key, value):
        key_hash = hash(key)
        index = key_hash % self.initial_capacity
        data_to_add = (key, value)

        if not self.dict_data[index]:
            self.dict_data[index] = data_to_add
            self.dict_len += 1
        else:
            for i in range(self.initial_capacity):
                if not self.dict_data[i]:
                    self.dict_data[i] = data_to_add
                    self.dict_len += 1
                    break

    def __getitem__(self, key):
        index = hash(key) % self.initial_capacity
        data_key, data_value = self.dict_data[index]
        if key == data_key:
            return data_value
        else:
            for data_item in [item for item in self.dict_data if item]:
                data_item_key, data_item_value = data_item
                if data_item_key == key:
                    return data_item_value

    def __len__(self):
        return self.dict_len


if __name__ == "__main__":
    items = [
        (8, "8"),
        (16, "16"),
        (32, "32"),
        (64, "64"),
        (128, "128"),
        ("one", 2),
        ("two", 2),
        (Point(1, 1), "a"),
        ("one", 1),
        ("one", 11),
        ("one", 111),
        ("one", 1111),
        (145, 146),
        (145, 145),
        (145, -1),
        ("two", 22),
        ("two", 222),
        ("two", 2222),
        ("two", 22222),
        (Point(1, 1), "A")
    ]
    pairs_after_adding = [
        (8, "8"),
        (16, "16"),
        (32, "32"),
        (64, "64"),
        (128, "128"),
        ("one", 1111),
        ("two", 22222),
        (145, -1),
        (Point(1, 1), "A")
    ]

    dictionary = Dictionary()
    for key, value in items:
        dictionary[key] = value
    print(dictionary.dict_data)
    for key, value in pairs_after_adding:
        assert dictionary[key] == value
    assert len(dictionary) == len(pairs_after_adding)
