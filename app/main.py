import pprint
from typing import List


class Dictionary:
    def __init__(self, elements: List[tuple] = None):
        if elements is None:
            elements = []
        self._bucket_size = 8
        self._bucket_resize = self._bucket_size * 2 / 3
        while len(elements) > self._bucket_resize:
            self._bucket_size *= 2
            self._bucket_resize = self._bucket_size * 2 / 3
        self._buckets = [[] for i in range(self._bucket_size)]
        self._len_bucket = 0
        if len(elements):
            self._assign_buckets(elements)

    def _assign_buckets(self, elements):
        if not self._len_bucket:
            self._buckets = [None] * self._bucket_size

        for key, value in elements:
            if isinstance(key, list | dict | set):
                raise KeyError
            hashed_value = hash(key)
            index = hashed_value % self._bucket_size

            while self._buckets[index] is not None:
                index = (index + 1) % self._bucket_size

            self._buckets[index] = (key, value,)

    def _get_buckets_full(self):
        return [full_bucket for full_bucket in self._buckets if full_bucket is not None and len(full_bucket)]

    def _resize(self, new_key_value):
        current_buckets = self._get_buckets_full()
        current_buckets += new_key_value

        while self._len_bucket > self._bucket_resize:
            self._bucket_size *= 2
            self._bucket_resize = self._bucket_size * 2 / 3

        self._buckets = [[] for i in range(self._bucket_size)]
        self._len_bucket = 0
        self._assign_buckets(current_buckets)

    def __setitem__(self, key, value):
        self._len_bucket = len(self) + 1

        if self._len_bucket > self._bucket_resize:
            self._resize([(key, value)])

        else:
            self._assign_buckets([(key, value)])

    def __getitem__(self, input_key):
        hashed_value = hash(input_key)
        index = hashed_value % self._bucket_size
        if input_key not in self.keys():
            raise KeyError
        while self._buckets[index] is not None:
            key, value = self._buckets[index]
            if key == input_key:
                return value
            index = (index + 1) % self._bucket_size

    def __str__(self):
        dict_repr = "  {\n"
        for key, value in self._get_buckets_full():
            dict_repr += f"    {key}: {value},\n"
        dict_repr += "}"
        return dict_repr

    def __repr__(self):
        dict_repr = "  {\n"
        for key, value in self._get_buckets_full():
            dict_repr += f"    {key}: {value},\n"
        dict_repr += "}"
        return dict_repr

    def __len__(self):
        return len(self._get_buckets_full())

    def keys(self):
        keys_list = []
        for key, value in self._get_buckets_full():
            keys_list.append(key)
        return keys_list

    def values(self):
        values_list = []
        for key, value in self._get_buckets_full():
            values_list.append(value)
        return values_list

#
# some_dict = Dictionary()
#
# # some_dict[5] = "good idea"
# #
# # some_dict[6] = "cool idea"
# #
# # some_dict[7] = "bad idea"
#
# print(len(some_dict))
#
# # print(some_dict[123])
# # some_dict[8] = "great idea"
# # print(f"""
# #
# #     {some_dict}
# #
# #     {some_dict}
# # """)
