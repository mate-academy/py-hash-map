from typing import Any, Hashable


class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.hashmap: list = [[] for _ in range(self.capacity)]
        self.length = 0
        self.LOAD_FACTOR = 0.75

    def hash_key_index(self, key: Hashable) -> int:
        return hash(key) % self.capacity

    def resize(self) -> None:
        self.capacity *= 2
        self.length = 0
        old_hashmap = self.hashmap
        self.hashmap = [[] for _ in range(self.capacity)]

        for elements in old_hashmap:
            if len(elements) >= 1:
                for element in elements:
                    self[element[0]] = element[1]

    def __setitem__(self, key: Hashable, value: Any) -> None:
        hash_key = hash(key)

        for index, (stored_key, stored_value, stored_hash) \
                in enumerate(self.hashmap[self.hash_key_index(key)]):
            if stored_hash == hash_key and stored_key == key:
                self.hashmap[self.hash_key_index(key)][index] = \
                    (key, value, hash_key)
                self.length -= 1
                break
        else:
            self.hashmap[self.hash_key_index(key)].append(
                (key, value, hash_key)
            )

        self.length += 1

        if self.length / float(self.capacity) >= self.LOAD_FACTOR:
            self.resize()

    def __getitem__(self, key: Hashable) -> Any:
        for index, data_tuple \
                in enumerate(self.hashmap[self.hash_key_index(key)]):
            if data_tuple[0] == key:
                return data_tuple[1]
        raise KeyError("Key doesn't exist.")

    def __len__(self) -> int:
        return self.length
