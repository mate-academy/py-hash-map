from typing import Hashable, Any


class Dictionary:
<<<<<<< HEAD
    def __init__(self,
                 capacity: int = 8,
                 size: int = 0,
                 load_factor: float = 2 / 3
                 ) -> None:
        self.capacity = capacity
        self.size = size
        self.load_factor = load_factor
        self.storage = [(None, None, None)] * self.capacity

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.size > self.capacity * self.load_factor:
            self.resize()
        key_hash = hash(key)
        key_index = self.get_index(key)

        if key != self.storage[key_index][0]:
            self.size += 1
        self.storage[key_index] = (key, key_hash, value)

    def get_index(self, key: Hashable) -> int:
        key_hash = hash(key)
        index = key_hash % self.capacity

        while True:
            if self.storage[index][0] is None:
                break
            elif self.storage[index][0] == key:
                break
            else:
                index = (index + 1) % self.capacity

        return index

    def resize(self) -> None:
        self.capacity *= 2
        temp_list = self.storage
        self.storage = [(None, None, None)] * self.capacity
        for element in temp_list:
            key_index = self.get_index(element[0])
            self.storage[key_index] = element

    def __getitem__(self, key: Hashable) -> Any:
        index = self.get_index(key)
        if not any(self.storage[index]):
            raise KeyError
        return self.storage[index][2]

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        return (f"capacity: {self.capacity} "
                f"size: {self.size} "
                f"storage: {self.storage}"
                )
=======
    def __init__(self, capacity: int = 8) -> None:
        self.capacity = capacity
        self.storage = [[] for _ in range(self.capacity)]
        self.size = 0

    def __setitem__(self, key: Hashable, value: Any) -> None:
        self.resize()
        hash_key = hash(key) % self.capacity
        while True:
            if self.storage[hash_key] != []:
                hash_key += 1
                if hash_key > self.capacity - 1:
                    hash_key = 0
            else:
                self.storage[hash_key] = [key, value, hash(key)]
                self.size += 1
                break

    def resize(self) -> None:
        if self.size > 2 / 3 * self.capacity:
            self.capacity *= 2
            old_elements = self.storage
            self.storage = [[] for _ in range(self.capacity)]
            self.size = 0
            for element in old_elements:
                if element != []:
                    self.__setitem__(element[2], element[1])

    def __getitem__(self, key: Hashable) -> Any:
        hash_key = hash(key) % self.capacity
        if not self.storage[hash_key]:
            raise KeyError
        else:
            return self.storage[hash_key][1]

    def __len__(self) -> int:
        return self.size
