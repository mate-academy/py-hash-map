from typing import Any

class Dictionary:
    def __init__(self, initial_capacity: int = 8,
                 load_factor: float = 0.66,
                 resize_factor: int = 2) -> None:
        self.load_factor = load_factor
        self.resize_factor = resize_factor
        self.list_size = 0
        self.buckets_size = initial_capacity
        self.list = [[]] * self.buckets_size

    def check_load_factor(self):
        current_load = self.list_size / float(self.buckets_size)
        if current_load > self.load_factor:
            buckets = self.buckets_size * self.resize_factor
            self.resize_rehash(buckets)

    def generate_new_list(self, bucket_size: int):
        self.list = []
        self.list_size = 0
        self.list = [[]] * self.buckets_size

    def get_index(self, key):
        return hash(key) % self.buckets_size

    def add_new_keyvalue(self, key, index, value):
        self.list[index] = [key, index, value]
        self.list_size += 1

    def __len__(self):
        return self.list_size

    def resize_rehash(self, buckets):
        if type(buckets) is not int:
            pass
        else:
            temp_data = self.list
            # self.buckets_size = buckets
            self.generate_new_list(buckets)
            for bucket_list in temp_data:
                for key, value in bucket_list:
                    index = self.get_index(key)
                    self.add_new_keyvalue(key, index, value)

    def __getitem__(self, key: Any) -> list:
        index = self.get_index(key)
        while self.list[index]:
            if (
                    self.list[index][1] == index
                    and self.list[index][0] == key
            ):
                return self.list[index][2]
            index = (index + 1) % self.buckets_size
        raise KeyError

    def __setitem__(self, key, value):
        index = self.get_index(key)
        while self.list[index] is not []:
            index = (index + 1) % self.buckets_size
        self.add_new_keyvalue(key, index, value)
        self.check_load_factor()
        else:
        if self.list[index][0] == key:
            self.list[index][2] = value

    def get_all(self):
        raw_list = []
        for bucket_list in self.list:
            # for key_value in bucket_list:
            raw_list.append(bucket_list)
        return raw_list

    def __delitem__(self, key):
        index = self.get_index(key)
        if index is None:
            pass
        if self.list[index][0] != key:
            raise IndexError(f"Key {key} not found in")
        else:
            self.list[index].clear()
            self.list_size -= 1

    def pop(self, key):
        index = self.get_index(key)
        if index is None:
            return None
        if self.list[index][0] != key:
            return None
        else:
            value = self.list[index][2]
            self.list[index].clear()
            return value

    def get_num_buckets(self):
        return self.buckets_size


if __name__ == '__main__':
    dictionary = Dictionary()
    dictionary["1"] = "jfjdhdd"
    dictionary["8"] = "123"
    dictionary["3"] = "45"
    dictionary[0] = "ups"

    print(dictionary["1"])
    print(dictionary["3"])
    print(dictionary.get_all())
    dictionary["1"] = "0987"
    print(dictionary["1"])
    print(dictionary.get_all())