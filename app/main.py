from copy import deepcopy

from typing import Any


class Dictionary:

    def __init__(self,) -> None:

        self.length = 0
        self.hash_table = [[] for _ in range(8)]

    def __setitem__(self, key: Any, value: Any) -> None:
        threshold = (len(self.hash_table) * 2) // 3
        if self.length == threshold:
            self.resize()
        hash_key = hash(key)
        index = self.get_index(hash_key)

        if self.hash_table[index]:

            while self.hash_table[index]:
                if key == self.hash_table[index][0]:
                    self.hash_table[index][1] = value
                    return
                index += 1
                if index == len(self.hash_table):
                    index = 0
            self.hash_table[index] = [key, value, key.__hash__()]
            self.length += 1
        else:
            self.hash_table[index] = [key, value, key.__hash__()]
            self.length += 1

    def __getitem__(self, key: Any) -> Any:
        key_list = []
        for string in self.hash_table:
            if len(string) != 0:
                key_list.append(string[0])
        if len(key_list) == 0 or key not in key_list:
            raise KeyError

        for item in self.hash_table:
            if item != [] and item[0] == key:
                return item[1]

    def __len__(self) -> int:
        return self.length

    def get_index(self, hash_key: int) -> int:
        return hash_key % len(self.hash_table)

    def get_capacity(self) -> int:
        count = 0
        for item in self.hash_table:
            if item:
                count += 1
        return count

    def resize(self) -> None:

        self.length = 0
        new_list = [[] for _ in range((len(self.hash_table) * 2))]
        hash_list_copy = deepcopy(self.hash_table)

        for item in hash_list_copy:
            if item:
                hash_key = hash(item[0])
                index = hash_key % len(new_list)
                if new_list[index]:
                    while new_list[index]:
                        index += 1
                        if index == len(new_list[index]):
                            index = 0
                    new_list[index] = [item[0], item[1], item[2]]
                    self.length += 1
                else:
                    new_list[index] = [item[0], item[1], item[2]]
                    self.length += 1

        self.hash_table = new_list

    def total_len(self) -> None:
        print(len(self.hash_table))
