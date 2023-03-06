from typing import Any, Hashable


class Dictionary:
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
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i] = (key, hash(key), value)
                return
        bucket.append((key, hash(key), value))
        self.length += 1

    def __getitem__(self, key: Hashable) -> Any:
        index = self._get_index(key)
        for k, h, v in self.hash_table[index]:
            if k == key:
                return v
        raise KeyError(key)

    def __delitem__(self, key: Hashable) -> None:
        index = self._get_index(key)
        bucket = self.hash_table[index]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                del bucket[i]
                self.length -= 1
                return
        raise KeyError(key)

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
