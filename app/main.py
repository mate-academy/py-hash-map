from typing import Any, Hashable


class Dictionary(object):
    def __init__(self, capacity: int = 8, load_factor: float = 0.66) -> None:
        self.capacity = capacity
        self.load_factor = load_factor
        self.length = 0
        self.limit = capacity * load_factor
        self.hash_table = [[] for _ in range(capacity)]
        self.collision = []

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.length > self.limit:
            self.resize()

        index = self._get_index(key)

        if self.hash_table[index]:
            self.hash_table[index] = (key, hash(key), value, )
        else:
            self.hash_table[index] = (key, hash(key), value, )
            self.length += 1

    def __getitem__(self, key: Hashable) -> Any:
        index = self._get_index(key, False)

        if not self.hash_table[index]:
            # if len(self.collision) > 0:
            for i in self.collision:
                if i[0] == index:
                    if self.hash_table[i[1]][0] == key:
                        return self.hash_table[i[1]][2]
                    else:
                        continue
            raise KeyError(key)
        elif self.hash_table[index][0] == key:
            return self.hash_table[index][2]

    def __delitem__(self, key: Hashable) -> None:
        index = self._get_index(key, False)
        h_index = hash(key) % self.capacity
        bucket = self.hash_table[index]

        if len(bucket) == 0 or bucket[0] != key:
            raise KeyError(key)
        else:
            self.hash_table[index] = []
            if h_index != index:
                temp = (h_index, index)
                if temp in self.collision:
                    self.collision.remove(temp)
            self.length -= 1

    def __len__(self) -> int:
        return self.length

    def _get_index(self, key: Hashable, available: bool = True) -> int:
        index = hash(key) % self.capacity
        old_index = index
        if not self.hash_table[index] and available:
            return index

        while self.hash_table[index]:
            k, h, v = self.hash_table[index]

            if k == key and h == hash(key):
                return index

            index = (index + 1) % self.capacity
        if old_index != index:
            self.collision.append((old_index, index))
        return index

    def resize(self) -> None:
        old_hash_table = self.hash_table
        self.capacity *= 2
        self.limit = self.capacity * self.load_factor
        self.hash_table = [[] for _ in range(self.capacity)]
        self.length = 0

        for bucket in old_hash_table:
            if bucket:
                self.__setitem__(bucket[0], bucket[2])
