from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.threshold = int(self.capacity * 2 / 3)
        self.resize = 2
        self.length = 0
        self.hash = [[] for _ in range(self.capacity)]

    def __len__(self) -> int:
        return self.length

    def get_index_and_hash(self, key: Any) -> Any:
        index = hash(key) % self.capacity
        hash_of_item = hash(key)
        return hash_of_item, index

    def __setitem__(self, key: Any, value: Any) -> None:
        if self.length > self.threshold:
            self.resize_table()
        hash_of_item, index = self.get_index_and_hash(key)
        node = [key, hash_of_item, value]
        while True:
            if not self.hash[index]:
                self.hash[index] = node
                self.length += 1
                break
            if (self.hash[index][0] == key
                    and self.hash[index][1] == hash_of_item):
                self.hash[index][2] = value
                break
            index = (index + 1) % self.capacity

    def resize_table(self) -> None:
        self.capacity *= self.resize
        self.threshold = int(self.capacity * 2 / 3)
        hash_list = self.hash
        self.length = 0
        self.hash = [[] for _ in range(self.capacity)]
        for item in hash_list:
            if item:
                self.__setitem__(item[0], item[2])

    def __getitem__(self, key: Any) -> Any:
        hash_of_item, index = self.get_index_and_hash(key)
        while self.hash[index]:
            if (self.hash[index][0] == key
                    and self.hash[index][1] == hash_of_item):
                return self.hash[index][2]
            index = (index + 1) % self.capacity
        raise KeyError
