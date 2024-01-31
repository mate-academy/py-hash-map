from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.hashmap: list = [[] for _ in range(self.capacity)]
        self.length = 0

    def __setitem__(self, key: Any, value: Any) -> None:
        hash_key = hash(key) % self.capacity
        element_exists = False

        for index, element in enumerate(self.hashmap[hash_key]):
            if len(element) == 2 and element[0] == key:
                self.hashmap[hash_key][index] = (key, value)
                element_exists = True
                self.length -= 1
                break

        if not element_exists:
            self.hashmap[hash_key].append((key, value))
        self.length += 1

    def __getitem__(self, key: Any) -> Any:
        hash_key = hash(key) % self.capacity

        for index, element in enumerate(self.hashmap[hash_key]):
            if element[0] == key:
                return element[1]
        else:
            raise KeyError("Key doesn't exist.")

    def __len__(self) -> int:
        return self.length
