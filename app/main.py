from app.point import Point


class Dictionary:
    def __init__(self):
        self.dict_capacity = 8
        self.load_factor = int(self.dict_capacity * (2 / 3))
        self.dict_data = [False for _ in range(8)]
        self.dict_len = 0
        self.free_paces_in_dict_data = [i for i in range(self.dict_capacity)]

    def __setitem__(self, key, value):
        key_hash = hash(key)
        index_to_write = key_hash % self.dict_capacity
        tepm_index = self.free_paces_in_dict_data[0]

        if not self.dict_data[index_to_write]:
            self.dict_data[index_to_write] = (key_hash, key, value)

        else:
            item_hash, item_key, item_value = self.dict_data[index_to_write]

            if item_hash == hash(key) or item_key == key:
                self.dict_data[index_to_write] = value
            else:
                self.dict_data[tepm_index] = (key_hash, key, value)
        self.free_paces_in_dict_data.remove(tepm_index)
        self.dict_len += 1

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
            self.expand_dict_data()

    def expand_dict_data(self):
        expanded_capacity = self.dict_capacity * 2
        expanded_dict_data = [False for _ in range(expanded_capacity)]
        self.dict_len = 0
        free_paces_in_dict_data = [i for i in range(expanded_capacity)]
        for i, data_item in enumerate(self.dict_data):
            if data_item:
                key, value = data_item
                key_hash = hash(key)
                data_to_add = (key, value)
                index = key_hash % expanded_capacity
                if not expanded_dict_data[index]:
                    expanded_dict_data[index] = data_to_add
                    free_paces_in_dict_data.remove(index)
                else:
                    second_type_index = free_paces_in_dict_data[0]
                    expanded_dict_data[second_type_index] = data_to_add
                    free_paces_in_dict_data.remove(second_type_index)
                self.dict_len += 1
        self.dict_capacity = expanded_capacity
        self.dict_data = expanded_dict_data
        self.load_factor = int(self.dict_capacity * (2 / 3))


if __name__ == "__main__":
    items = [
        (1, "one"), (2, "two"), (3, "tree"), (4, "four")
    ]
    pairs_after_adding = [
        (1, "one"), (2, "two"), (3, "tree"), (4, "four")
    ]

    dictionary = Dictionary()

    for key, value in items:
        dictionary[key] = value
    print(dictionary.dict_data)
    for key, value in pairs_after_adding:
        assert dictionary[key] == value
    assert len(dictionary) == len(pairs_after_adding)
