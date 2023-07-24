import copy
from typing import Hashable, Any


class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.hash_table: list = [None] * 8
        self.cur_hash_table: list = []

    def set(
            self,
            key: Hashable,
            value: Any,
            reset: bool = False
    ) -> None:
        """ Set new key/value pair to dict"""
        hash_key = hash(key)
        key_index = hash_key % len(self.hash_table)
        if self.hash_table[key_index]:
            if self.hash_table[key_index][1] == key:
                self.hash_table[key_index][2] = value
            else:
                added = False  # check if key was added to dict
                for current_index in range(
                        key_index + 1,
                        len(self.hash_table)
                ):
                    if self.hash_table[current_index]:
                        if self.hash_table[current_index][1] == key:
                            self.hash_table[current_index][2] = value
                            added = True
                            break
                    if not self.hash_table[current_index]:
                        self.hash_table[current_index] = [
                            key_index,
                            key,
                            value
                        ]
                        added = True
                        if not reset:
                            self.length += 1
                        break
                if not added:
                    for current_index in range(0, key_index - 1):
                        if self.hash_table[current_index]:
                            if self.hash_table[current_index][1] == key:
                                self.hash_table[current_index][2] = value
                                break
                        if not self.hash_table[current_index]:
                            self.hash_table[current_index] = [
                                key_index,
                                key,
                                value
                            ]
                            if not reset:
                                self.length += 1
                            break
        else:
            self.hash_table[key_index] = [key_index, key, value]
            if not reset:
                self.length += 1

    def __setitem__(self, key: Hashable, value: Any) -> None:
        """Magik method for Dictionary, add new pair to Dictionary
        and controls count of cells in hash table"""
        self.set(key, value)
        if self.length > 0.66666 * len(self.hash_table):
            self.double_hash_table()

    def double_hash_table(self) -> None:
        """Increases count of cells in hash table and set
        new indexes for each key/value pair"""
        self.cur_hash_table = copy.copy(self.hash_table)
        self.hash_table = [None] * len(self.cur_hash_table) * 2
        for elem in self.cur_hash_table:
            if elem:
                self.set(elem[1], elem[2], True)
        self.cur_hash_table = []

    def find_table_index(self, key: Hashable) -> int:
        """Search key in hash table and returns its index
        in hash table"""
        hash_key = hash(key)
        key_index = hash_key % len(self.hash_table)
        if self.hash_table[key_index]:
            if self.hash_table[key_index][1] == key:
                return key_index
        for cur_index in range(key_index + 1, len(self.hash_table)):
            if self.hash_table[cur_index]:
                if self.hash_table[cur_index][1] == key:
                    return cur_index
        for cur_index in range(0, key_index - 1):
            if self.hash_table[cur_index]:
                if self.hash_table[cur_index][1] == key:
                    return cur_index
        raise KeyError

    def __getitem__(self, key: Hashable) -> Any:
        """ Returns value of given key"""
        index = self.find_table_index(key)
        return self.hash_table[index][2]

    def __len__(self) -> int:
        """ Returns count of records in Dictionary"""
        return self.length

    def __repr__(self) -> str:
        """String representation"""
        return str(f"dict of length{self.length}")

    def __delitem__(self, key: Hashable) -> None:
        """Removes key/value pair from hash table by given key"""
        index = self.find_table_index(key)
        self.hash_table[index] = None
        self.length -= 1

    def clear(self) -> None:
        """Clear all records in Dictionary"""
        self.hash_table = [None] * 8
        self.length = 0

    def get(self, key: Hashable) -> Any:
        """ Returns value of given key"""
        return self.__getitem__(key)

    def pop(self, key: Hashable) -> Any:
        """ Deletes key/value pair
        and returns value of given key"""
        index = self.find_table_index(key)
        elem = self.hash_table[index][2]
        self.hash_table[index] = None
        self.length -= 1
        return elem

    def update(self, key: Hashable, value: Any) -> None:
        """Reassign value of given key"""
        index = self.find_table_index(key)
        self.hash_table[index][2] = value

    def __iter__(self) -> Hashable:
        """Iter through keys in hash table"""
        for key in self.hash_table:
            if key:
                yield key
