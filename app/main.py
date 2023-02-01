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
            self.buckets_size *= self.resize_factor
            self.resize_rehash()

    def generate_new_list(self):
        self.list = []
        self.list_size = 0
        self.list = [[]] * self.buckets_size

    def get_index(self, key):
        return hash(key) % self.buckets_size

    def resize_rehash(self):
        temp_data = self.list
        self.generate_new_list()
        for bucket_list in temp_data:
            if bucket_list:
                key, index, value = bucket_list
                self.__setitem__(key, value)

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
        while True:
            if not self.list[index]:
                self.list[index] = [key, index, value]
                self.list_size += 1
                self.check_load_factor()
                break
            if self.list[index][0] == key:
                self.list[index][2] = value
                break
            index = (index + 1) % self.buckets_size

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

    def get_all(self):
        raw_list = []
        for bucket_list in self.list:
            raw_list.append(bucket_list)
        return raw_list

    def __len__(self):
        return self.list_size

    def get_num_buckets(self):
        return self.buckets_size


if __name__ == '__main__':
    dictionary = Dictionary()
    for i in range(10):
        dictionary[str(i)] = i

        print(dictionary[str(i)])
        print(dictionary.get_all())
