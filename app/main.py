from app.point import Point


class Dictionary:
    def __init__(self):
        self.dict_capacity = 8
        self.load_factor = int(self.dict_capacity * (2 / 3))
        self.dict_data = [False for _ in range(8)]
        self.dict_len = 0
        self.free_paces_in_dict_data = [i for i in range(self.dict_capacity)]
        self.need_to_extend = False

    def __setitem__(self, key, value):
        key_hash = hash(key)
        index_to_write = key_hash % self.dict_capacity

        if not self.dict_data[index_to_write]:
            self.dict_data[index_to_write] = (key_hash, key, value)
            self.free_paces_in_dict_data.remove(self.free_paces_in_dict_data[0])
            self.dict_len += 1

        elif self.dict_data[index_to_write]:
            item_hash, item_key, item_value = self.dict_data[index_to_write]

            if item_hash == hash(key) and item_key == key:
                self.dict_data[index_to_write] = (item_hash, item_key, value)
            else:
                temp_index = self.free_paces_in_dict_data[0]
                self.dict_data[temp_index] = (key_hash, key, value)
                self.free_paces_in_dict_data.remove(temp_index)
                self.dict_len += 1
        self.check_load_factor()

    def __getitem__(self, key):
        index = hash(key) % self.dict_capacity
        data_hash, data_key, data_value = self.dict_data[index]
        if key == data_key:
            return data_value
        else:
            for data_item in [item for item in self.dict_data if item]:
                data_item_hash, data_item_key, data_item_value = data_item
                if data_item_key == key:
                    return data_item_value

    def __len__(self):
        return self.dict_len

    def check_load_factor(self):
        if self.dict_len == self.load_factor:
            self.need_to_extend = True
            self.expand_dict_data()

    def expand_dict_data(self):
        self.dict_capacity *= 2
        self.load_factor = int(self.dict_capacity * (2 / 3))
        self.free_paces_in_dict_data = [_ for _ in range(self.dict_capacity)]
        self.dict_len = 0
        only_true_dict_data = [item for item in self.dict_data if item]
        self.dict_data = [False for _ in range(self.dict_capacity)]

        for item in only_true_dict_data:
            item_hash, item_key, item_value = item
            index_to_write = item_hash % self.dict_capacity
            if not self.dict_data[index_to_write]:
                self.dict_data[index_to_write] = (item_hash, item_key, item_value)
            else:
                temp_index = self.free_paces_in_dict_data[0]
                self.dict_data[temp_index] = (item_hash, item_key, item_value)
                self.free_paces_in_dict_data.remove(temp_index)
            self.dict_len += 1
            self.need_to_extend = False


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
        # (Point(1, 1), "A"),
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
    #     (Point(1, 1), "A"),
    # ]

    dictionary = Dictionary()

    for key, value in items:
        dictionary[key] = value
    print(dictionary.dict_data)
    print(len(dictionary), dictionary.dict_capacity, dictionary.load_factor)
    # for key, value in pairs_after_adding:
    #     assert dictionary[key] == value
    # assert len(dictionary) == len(pairs_after_adding)
