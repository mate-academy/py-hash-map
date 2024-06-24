from app.point import Point


class Dictionary:
    def __init__(self):
        self.dict_capacity = 8
        self.load_factor = int(self.dict_capacity * (2 / 3))
        self.dict_data = [False for _ in range(8)]
        self.dict_len = 0

    def __setitem__(self, key, value):
        key_hash = hash(key)
        index = key_hash % self.dict_capacity
        data_to_add = (key, value)

        if not self.dict_data[index]:
            self.dict_data[index] = data_to_add
            self.dict_len += 1
            self.check_load_factor()
        else:
            for i in range(self.dict_capacity):
                if not self.dict_data[i]:
                    self.dict_data[i] = data_to_add
                    self.dict_len += 1
                    self.check_load_factor()
                    break

    def __getitem__(self, key):
        index = hash(key) % self.dict_capacity
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

    def check_load_factor(self):
        if self.dict_len >= self.load_factor:
            print("Load factor is: ", self.load_factor, "Lenth is: ", self.dict_len)
            self.expand_dict_data()

    def expand_dict_data(self):
        current_capacity = self.dict_capacity
        expanded_capacity = current_capacity * 2
        expanded_dict_data = [False for _ in range(expanded_capacity)]
        expanded_dict_len = 0
        print(self.dict_data)
        for i, data_item in enumerate(self.dict_data):
            if data_item:
                key, value = data_item
                key_hash = hash(key)
                index = key_hash % expanded_capacity
                data_to_add = (key, value)
                expanded_dict_data[index] = data_to_add
                expanded_dict_len += 1
        self.dict_capacity = expanded_capacity
        self.dict_data = expanded_dict_data
        self.dict_len = expanded_dict_len
        print(self.dict_data)


if __name__ == "__main__":
    items = [
        (8, "8"),
        (16, "16"),
        (32, "32"),
        (64, "64"),
        (128, "128"),
        # ("one", 2),
        # ("two", 2),
        # (Point(1, 1), "a"),
        # ("one", 1),
        # ("one", 11),
        # ("one", 111),
        # ("one", 1111),
        # (145, 146),
        # (145, 145),
        # (145, -1),
        # ("two", 22),
        # ("two", 222),
        # ("two", 2222),
        # ("two", 22222),
        # (Point(1, 1), "A")
    ]
    # pairs_after_adding = [
    #     (8, "8"),
    #     (16, "16"),
    #     (32, "32"),
    #     (64, "64"),
    #     (128, "128"),
    #     ("one", 1111),
    #     ("two", 22222),
    #     (145, -1),
    #     (Point(1, 1), "A")
    # ]

    dictionary = Dictionary()

    for key, value in items:
        dictionary[key] = value

    # for key, value in pairs_after_adding:
    #     assert dictionary[key] == value
    # assert len(dictionary) == len(pairs_after_adding)
