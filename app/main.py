import copy
from collections.abc import Hashable
from typing import Any, Iterator


class Dictionary:
    def __init__(self):

        self.buckets_table = [[] for bucket in range(8)]
        self.capacity = len(self.buckets_table)
        self.resize_breakpoint = 2 / 3
        self.old_buckets_table = None

    def buckets_table_resize(self):
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
        if len(self.buckets_table[index]) > 0:
            self.buckets_table[self.buckets_table.index([])] = new_k_v_pair
        else:
            self.buckets_table[index] = new_k_v_pair
        if ((self.capacity - self.buckets_table.count([])) / self.capacity >
                self.resize_breakpoint):
            self.buckets_table_resize()

    def __getitem__(self, key: Hashable) -> Any:
        for bucket in self.buckets_table:
            if len(bucket) and key == bucket[0]:
                return bucket[1]
        raise KeyError(key)

    def __len__(self) -> int:
        return sum(1 for bucket in self.buckets_table if bucket)

    def clear(self) -> None:  # extra
        """ D.clear() -> None.  Remove all items from D. """
        pass

    def __delitem__(self, key: Hashable) -> None:  # extra
        """ Delete self[key]. """
        pass

    def get(self):  # extra
        """
        Return the value for key if key is in the dictionary,
        else default.
        """
        pass

    def pop(self):  # extra
        """
        D.pop(k[,d]) -> v, remove specified key
        and return the corresponding value.

        If the key is not found, return the default if given; otherwise,
        raise a KeyError.
        """
        pass

    def update(self):  # extra
        """
        D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
        If E is present and has a .keys() method, then does:
            for k in E: D[k] = E[k]
        If E is present and lacks a .keys() method, then does:
            for k, v in E: D[k] = v
        In either case, this is followed by: for k in F:  D[k] = F[k]
        """
        pass

    def __iter__(self) -> Iterator:
        """ Implement iter(self). """
        return iter(bucket[0] for bucket in self.buckets_table if len(bucket))

    def __repr__(self) -> str:

        return f"TABLE : {self.buckets_table}\n" \
               f"CAPACITY: {self.capacity}\n"
