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

        self.capacity *= 2
        print("resize action ________________________________")
        old_hash_table = copy.deepcopy(self.hash_table)
        print(old_hash_table)
        self.hash_table = [[] for i in range(self.capacity)]
        print(self.hash_table, print(len(self.hash_table)))
        for i in old_hash_table:
            if len(i):
                print(i[0], i[1], i[2])
                if self.hash_table[i[2] % len(self.hash_table)] == []:
                    self.hash_table[i[2] % len(self.hash_table)] = i

    def __setitem__(
            self,
            key: Union[
                int, float, complex, str, bool, tuple, frozenset,
                bytes, None, Enum, date, datetime
            ],
            value: Any
    ) -> None:  # mandatory

        """ Set self[key] to value. """
        if type(key) not in self.__APPROVED_DATA_TYPES:
            raise TypeError(f"unhashable type: '{type(key).__name__}'")

        self.current_load_factor = (self.capacity - self.hash_table.count([])) / self.capacity
        if self.current_load_factor > self.resize_breakpoint:
            self.hash_table_resize()

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
               f"LOAD FACTOR: {self.current_load_factor}\n"


class Point:
    def __init__(self, x: float, y: float) -> None:
        self._x = x
        self._y = y

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        # Change the implementation of the hash to debug your code.
        # For example, you can return self.x + self.y as a hash
        # which is NOT a best practice, but you will be able to predict
        # a hash value by coordinates of the point and its index
        # in the hashtable as well
        return hash((self.x, self.y))

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    def __repr__(self):
        return (f"Point example: x = {self.x} ; y = {self.y}\n"
                f"Hash: {self.__hash__()}")


def timer_decorator(func):  # TODO: DELETE IT
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"{func.__name__} execution took: {end_time - start_time}")

    return wrapper


def quick_prints():  # TODO: DELETE IT
    items = [(f"Element {i}", i) for i in range(7)]
    dictionary = Dictionary()
    for key, value in items:
        dictionary[key] = value
    print(len(dictionary))
    print(len(items))


if __name__ == "__main__":  # TODO: DELETE IT
    quick_prints()

    # def hash_table_resize(self):
    #     print("resize action ________________________________")
    #     self.hash_table += [[] for i in range(self.capacity)]
    #     self.capacity *= 2
    #     self.old_hash_table = copy.deepcopy(self.hash_table)
    #     self.hash_table.clear()
    #     self.hash_table = [[] for i in range(self.capacity)]
    #
    #     for node in self.old_hash_table:
    #         if len(node):
    #             self.hash_table[
    #                 node[2] % self.capacity
    #                 ] = node
    #
    #     del self.old_hash_table
