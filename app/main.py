from copy import deepcopy

from typing import Any


class Dictionary:

    def __init__(self,) -> None:
        self.capacity = 8
        self.threshold = (self.capacity * 2) // 3
        self.length = 0
        self.hash_table = [[] for _ in range(self.capacity)]

    def __setitem__(self, key: Any, value: Any) -> None:
        # if self.length == self.threshold:
        #     self.resize()
        if self.length + 1 > self.capacity * (2 / 3):
            self.resize()
        hash_key = hash(key)
        index = self.get_index(hash_key)

        while self.hash_table[index]:
            if key == self.hash_table[index][0]:
                self.hash_table[index][2] = value
                return
            index += 1
            if index == len(self.hash_table):
                index = 0
        self.hash_table[index] = [key, hash_key, value]
        self.length += 1

    def __getitem__(self, key: Any) -> Any:

        hash_key = hash(key)
        index = self.get_index(hash_key)

        while self.hash_table[index]:
            if (self.hash_table[index][0] == key
                    and self.hash_table[index][1] == hash_key):
                return self.hash_table[index][2]
            index += 1

        raise KeyError

    def __len__(self) -> int:
        return self.length

    def get_index(self, hash_key: int) -> int:
        return hash_key % self.capacity

    def get_capacity(self) -> int:
        count = 0
        for item in self.hash_table:
            if item:
                count += 1
        return count

    def resize(self) -> None:

        self.length = 0
        self.capacity *= 2
        new_list = [[] for _ in range((len(self.hash_table) * 2))]
        # hash_list_copy = deepcopy(self.hash_table)
        hash_list_copy = self.hash_table
        self.hash_table = new_list
        for item in hash_list_copy:
            if item:
                self.__setitem__(item[0], item[2])
        #     if item:
        #         hash_key = hash(item[0])
        #         index = hash_key % len(new_list)
        #         if new_list[index]:
        #             while new_list[index]:
        #                 index += 1
        #                 if index == len(new_list[index]):
        #                     index = 0
        #             new_list[index] = [item[0], item[1], item[2]]
        #             self.length += 1
        #         else:
        #             new_list[index] = [item[0], item[1], item[2]]
        #             self.length += 1

        # self.hash_table = new_list

    def total_len(self) -> None:
        print(len(self.hash_table))

    def show(self):
        print(self.hash_table)

f = Dictionary()
f.__setitem__(3, "fds")
f.__setitem__(5, "dddass")
f.__setitem__(6, "s654")
f.__setitem__(7, "nbv")
f.__setitem__(9, "vcx")
f.__setitem__(12, "cxg")



print(f.__getitem__(3))
print(f.__getitem__(5))
print(f.__getitem__(6))
print(f.__getitem__(7))
print(f.__getitem__(9))
print(f.__getitem__(12))
print(f.__len__())
f.total_len()
f.show()
