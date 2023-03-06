from typing import Any, Hashable


class Dictionary(object):
    def __init__(self, capacity: int = 8, load_factor: float = 0.66) -> None:
        self.capacity = capacity
        self.load_factor = load_factor
        self.length = 0
        self.limit = capacity * load_factor
        self.hash_table = [[] for _ in range(capacity)]

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.length > self.limit:
            self.resize()
        index = self._get_index(key)
        bucket = self.hash_table[index]
        if len(bucket) == 0:
            bucket.append((key, hash(key), value))
            self.length += 1
        else:
            bucket[0] = (key, hash(key), value)
        return

    def __getitem__(self, key: Hashable) -> Any:
        index = self._get_index(key)
        if not self.hash_table[index]:
            raise KeyError(key)
        elif self.hash_table[index][0][0] == key:
            return self.hash_table[index][0][2]

    def __delitem__(self, key: Hashable) -> None:
        index = self._get_index(key)
        bucket = self.hash_table[index]
        if len(bucket) == 0 or bucket[0][0] != key:
            raise KeyError(key)
        else:
            self.hash_table[index] = []
            self.length -= 1
            return

    def __len__(self) -> int:
        return self.length

    def _get_index(self, key: Hashable) -> int:
        index = hash(key) % self.capacity
        while self.hash_table[index]:
            k, h, v = self.hash_table[index][0]
            if k == key and h == hash(key):
                return index
            index = (index + 1) % self.capacity
        return index

    def resize(self) -> None:
        old_hash_table = self.hash_table
        self.capacity *= 2
        self.limit = self.capacity * self.load_factor
        self.hash_table = [[] for _ in range(self.capacity)]
        self.length = 0
        for bucket in old_hash_table:
            for k, h, v in bucket:
                self.__setitem__(k, v)
