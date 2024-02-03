from typing import Any, Hashable


# class Dictionary:
#     def __init__(self) -> None:
#         self.capacity = 8
#         self.hashmap: list = [[] for _ in range(self.capacity)]
#         self.length = 0
#         self.load_factor = 0.75
#
#     def resize(self) -> None:
#         self.capacity *= 2
#         self.length = 0
#         old_hashmap = self.hashmap
#         self.hashmap = [[] for _ in range(self.capacity)]
#
#         for elements in old_hashmap:
#             if len(elements) >= 1:
#                 for element in elements:
#                     self.__setitem__(element[0], element[1])
#
#     def __setitem__(self, key: Hashable, value: Any) -> None:
#         hash_key = hash(key) % self.capacity
#         element_exists = False
#         self.length += 1
#
#         for index, element in enumerate(self.hashmap[hash_key]):
#             if len(element) == 2 and element[0] == key:
#                 self.hashmap[hash_key][index] = (key, value)
#                 element_exists = True
#                 self.length -= 1
#                 break
#
#         if not element_exists:
#             self.hashmap[hash_key].append((key, value))
#
#         if self.length / float(self.capacity) >= self.load_factor:
#             self.resize()
#
#     def __getitem__(self, key: Hashable) -> Any:
#         hash_key = hash(key) % self.capacity
#
#         for index, element in enumerate(self.hashmap[hash_key]):
#             if element[0] == key:
#                 return element[1]
#         else:
#             raise KeyError("Key doesn't exist.")
#
#     def __len__(self) -> int:
#         return self.length

class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.hashmap: list = [[] for _ in range(self.capacity)]
        self.length = 0
        self.load_factor = 0.75

    def resize(self) -> None:
        self.capacity *= 2
        self.length = 0
        old_hashmap = self.hashmap
        self.hashmap = [[] for _ in range(self.capacity)]

        for elements in old_hashmap:
            if len(elements) >= 1:
                for element in elements:
                    self.__setitem__(element[0], element[1])

    def __setitem__(self, key: Hashable, value: Any) -> None:
        hash_key = hash(key)
        element_exists = False
        self.length += 1

        for index, (stored_key, stored_value, stored_hash) \
                in enumerate(self.hashmap[hash_key % self.capacity]):
            if stored_hash == hash_key and stored_key == key:
                self.hashmap[hash_key % self.capacity][index] = \
                    (key, value, hash_key)
                element_exists = True
                self.length -= 1
                break

        if not element_exists:
            (self.hashmap[hash_key % self.capacity].
             append((key, value, hash_key)))

        if self.length / float(self.capacity) >= self.load_factor:
            self.resize()

    def __getitem__(self, key: Hashable) -> Any:
        hash_key = hash(key) % self.capacity

        for index, element in enumerate(self.hashmap[hash_key]):
            if element[0] == key:
                return element[1]
        else:
            raise KeyError("Key doesn't exist.")

    def __len__(self) -> int:
        return self.length
