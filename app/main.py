import copy
import pprint
from collections.abc import Hashable
from typing import Union, Any, Iterator


class Dictionary:
    def __init__(self) -> None:

        self.buckets_table = [[] for _ in range(8)]
        self.capacity = len(self.buckets_table)
        self.resize_breakpoint = 2 / 3
        self.old_buckets_table = None

    def buckets_table_resize(self) -> None:
        self.capacity *= 2
        self.old_buckets_table = copy.deepcopy(self.buckets_table)
        self.buckets_table = [[] for bucket in range(self.capacity)]
        for bucket in self.old_buckets_table:
            if len(bucket):
                index_by_new_hash = bucket[2] % self.capacity
                if not len(self.buckets_table[index_by_new_hash]):
                    self.buckets_table[index_by_new_hash] = bucket
                else:
                    self.buckets_table[self.buckets_table.index([])] = bucket

    def __setitem__(self, key: Hashable, value: Any) -> None:
        try:
            hash(key)
        except TypeError:
            raise TypeError(f"unhashable type: '{type(key).__name__}'")
        for bucket in self.buckets_table:
            if bucket and bucket[0] == key:
                bucket[1] = value
                return
        new_k_v_pair = [key, value, hash(key)]
        index = hash(key) % self.capacity
        empty_bucket_index = next((i for i, x in enumerate(self.buckets_table)
                                   if not x), None)
        if empty_bucket_index is not None:
            self.buckets_table[empty_bucket_index] = new_k_v_pair
        else:
            self.buckets_table[index] = new_k_v_pair
        if ((self.capacity - self.buckets_table.count([]))
                / self.capacity > self.resize_breakpoint):
            self.buckets_table_resize()

    def __getitem__(self, key: Hashable) -> Any:
        for bucket in self.buckets_table:
            if len(bucket) and key == bucket[0]:
                return bucket[1]
        raise KeyError(key)

    def __len__(self) -> int:
        return sum(1 for bucket in self.buckets_table if len(bucket))

    def clear(self) -> None:
        self.buckets_table = [[] for bucket in range(self.capacity)]

    def __delitem__(self, key: Hashable) -> None:
        for bucket in self.buckets_table:
            if len(bucket) and bucket[0] == key:
                bucket.clear()

    def get(self, key: Hashable, default: Any = None) -> Any:
        for bucket in self.buckets_table:
            if len(bucket) and key == bucket[0]:
                return bucket[1]
        return default

    def update(self, other_dict: "Dictionary") -> None:
        for bucket in other_dict.buckets_table:
            if len(bucket):
                self.__setitem__(bucket[0], bucket[1])

    def pop(self, key: Hashable, default: Any = None) -> Union[None, Any]:
        value = None
        for bucket in self.buckets_table:
            if len(bucket) and bucket[0] == key:
                value = bucket[1]
                bucket.clear()
        if default is not None:
            return default
        if value is not None:
            return value
        raise KeyError

    def __iter__(self) -> Iterator:

        return iter(bucket[0] for bucket in self.buckets_table if len(bucket))

    def __repr__(self) -> str:
        return ("CUSTOM_HASH_TABLE: [KEY, VALUE, HASH(KEY)]\n"
                + ("*" * 42) + "\n" + pprint.pformat(
                    object=self.buckets_table,
                    indent=0)[1:-1]
                + "\n" + "CAPACITY: " + str(self.capacity) + "\n"
                + "LEN: " + str(self.__len__())) + "\n" + ("*" * 42)

    def __str__(self) -> str:
        return "{" + ", ".join([bucket[0] + " : " + str(bucket[1])
                                for bucket in self.buckets_table
                                if len(bucket)]) + "}"
