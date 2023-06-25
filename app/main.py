import copy
import time
from datetime import date, datetime
from enum import Enum
from typing import Any, Union


class Dictionary:
    """
    Dict(object) clone
    _ = Dictionary_obj("One", 1) =>
    [["One", 1, hash("One")],[]..to len(capacity)]
    """

    def __init__(self):  # mandatory?
        self.old_hash_table = None
        self.__APPROVED_DATA_TYPES = [int, float, complex, str, bool, tuple,
                                      frozenset, bytes, None, Enum, date, datetime]
        self.hash_table = [[] for i in range(8)]  # [key #value #hash]
        self.capacity = len(self.hash_table)
        self.resize_breakpoint = 2 / 3

    def hash_table_resize(self):
        self.old_hash_table = copy.deepcopy(self.hash_table)
        self.hash_table = [[] for i in range(self.capacity)]
        for i in self.old_hash_table:
            if len(i):
                index_by_new_hash = i[2] % self.capacity
                if not len(self.hash_table[index_by_new_hash]):
                    self.hash_table[index_by_new_hash] = i
                else:
                    self.hash_table[self.hash_table.index([])] = i

    def __setitem__(
            self,
            key: Union[
                int, float, complex, str, bool, tuple, frozenset,
                bytes, None, Enum, date, datetime
            ],
            value: Any
    ) -> None:  # mandatory

        """ Set self[key] to value. """
        try:
            type(key) in self.__APPROVED_DATA_TYPES
        except Exception:
            raise TypeError(f"unhashable type: '{type(key).__name__}'")

        self.key, self.value = key, value
        for node in self.hash_table:  # reassign value
            if hash(self.key) in node:
                node[1] = self.value
                return
        self.new_element = [self.key, self.value, hash(self.key)]
        self.elem_index = self.new_element[2] % self.capacity

        if len(self.hash_table[self.elem_index]) > 0:
            self.hash_table[self.hash_table.index([])] = self.new_element
        else:
            self.hash_table[self.elem_index] = self.new_element
        self.current_load_factor = (self.capacity - self.hash_table.count([])) / self.capacity
        if self.current_load_factor > self.resize_breakpoint:
            self.capacity *= 2
            print("resize call from __set__")
            self.hash_table_resize()

    def __getitem__(self, key) -> Any:  # mandatory
        """ x.__getitem__(y) <==> x[y] """

        for node in self.hash_table:
            if hash(key) in node:
                return node[1]
        raise KeyError

    def __len__(self) -> int:  # mandatory
        """ Return len(self). """
        # print("return len")
        # print(f"hash table len: {len(self.hash_table)}")
        # print(f"empty: {self.hash_table.count([])}")
        # print(self.hash_table)
        self.counter = 0
        return sum(1 for node in self.hash_table if node)

    def clear(self) -> None:  # extra
        """ D.clear() -> None.  Remove all items from D. """
        print("clear testing")  # TODO: DELETE IT

    def __delitem__(self, key) -> None:  # extra
        """ Delete self[key]. """
        print("delitem testing")  # TODO: DELETE IT

    def get(self):  # extra
        """
        Return the value for key if key is in the dictionary,
        else default.
        """
        print("get testing")  # TODO: DELETE IT

    def pop(self):  # extra
        """
        D.pop(k[,d]) -> v, remove specified key
        and return the corresponding value.

        If the key is not found, return the default if given; otherwise,
        raise a KeyError.
        """
        print("pop testing")  # TODO: DELETE IT

    def update(self):  # extra
        """
        D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
        If E is present and has a .keys() method, then does:
            for k in E: D[k] = E[k]
        If E is present and lacks a .keys() method, then does:
            for k, v in E: D[k] = v
        In either case, this is followed by: for k in F:  D[k] = F[k]
        """
        print("update testing")

    def __iter__(self):  # extra
        """ Implement iter(self). """

    def hash(self):  # optional
        """
        For the list, dict, and set, we cannot get the hash value.
        Only hashed values can be hashed.
        """
        # print("hash testing")  # TODO: DELETE IT

    def __repr__(self):  # optional
        # return f"{{{self.key} : {self.value}}}"
        return f"TABLE : {self.hash_table}\n" \
               f"CAPACITY: {self.capacity}\n" \



def timer_decorator(func):  # TODO: DELETE IT
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"{func.__name__} execution took: {end_time - start_time}")

    return wrapper


@timer_decorator
def quick_prints():  # TODO: DELETE IT

    dictionary = Dictionary()
    dictionary[0] = 2
    dictionary[1] = 2
    dictionary[2] = 2
    dictionary[3] = 2
    dictionary[4] = 2
    dictionary[5] = 2
    dictionary[6] = 2
    dictionary[7] = 2


    print(dictionary)




if __name__ == "__main__":  # TODO: DELETE IT
    quick_prints()


