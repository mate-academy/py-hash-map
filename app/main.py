import time
from datetime import date, datetime
from enum import Enum
from typing import Any, Union


def timer_decorator(func):  # TODO: DELETE IT
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"{func.__name__} execution took: {end_time - start_time}")

    return wrapper


class Dictionary:
    """
    Dict(object) clone

    some_dict = {"One": 1}         => {"Key": "value"}
    var = Dictionary_obj("One", 1) => list_1: ["One"] by_index: [1]<-index[0]
    O(n) + O(1)
    """

    def __init__(self):  # mandatory?
        """
        dict() -> new empty dictionary
        dict(mapping) -> new dictionary initialized from a mapping object's
            (key, value) pairs
        dict(iterable) -> new dictionary initialized as if via:
            d = {}
            for k, v in iterable:
                d[k] = v
        dict(**kwargs) -> new dictionary initialized with the name=value pairs
            in the keyword argument list.  For example:  dict(one=1, two=2)
        """
        print("init call")  # TODO: DELETE IT
        self.__APPROVED_DATA_TYPES = [int, float, complex, str, bool, tuple,
                                      frozenset, bytes, None, Enum, date, datetime]
        self.hash_table = [[] for cell in range(8)]
        self.capacity = 8
        self.load_factor = 2 / 3

    def edit_hash_table(self, key, value):
        hash_index = hash(key) % self.capacity
        self.hash_table[hash_index].append([key,value])
        self.hash_space_taken = len(self.hash_table) - self.hash_table.count([])
        if self.hash_space_taken / self.capacity > self.load_factor:
            self.capacity *= 2
            self.hash_table += [[] for cell in range(self.capacity)]
        print(len(self.hash_table))
        print(f"{self.hash_table}")

    def __setitem__(
            self,
            key: Union[
                int, float, complex, str, bool, tuple, frozenset,
                bytes, None, Enum, date, datetime
            ],
            value: Any
    ) -> None:  # mandatory
        print("setitem testing")  # TODO: DELETE IT
        """ Set self[key] to value. """
        if type(key) not in self.__APPROVED_DATA_TYPES:
            raise TypeError(f"unhashable type: '{type(key).__name__}'")
        self.key, self.value = key, value
        self.edit_hash_table(key, value)

    def __getitem__(self, key) -> Any:  # mandatory
        """ x.__getitem__(y) <==> x[y] """
        print("getitem testing")  # TODO: DELETE IT

    def __len__(self) -> int:  # mandatory
        """ Return len(self). """
        print("len testing")  # TODO: DELETE IT

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
        print("hash testing")  # TODO: DELETE IT

    def __repr__(self):  # optional
        return f"{{{self.key} : {self.value}}}"


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __repr__(self):
        return (f"Point example: x = {self.x} ; y = {self.y}\n"
                f"Hash: {self.__hash__()}")


def quick_prints():  # TODO: DELETE IT
    doppelganger = Dictionary()  # Custom
    doppelganger.__setitem__("KEY", "VALUE")
    doppelganger.__setitem__("KEY_2", 77)
    doppelganger.__setitem__("KEY_3", 77)
    doppelganger.__setitem__("KEY_4", 77)
    doppelganger.__setitem__("KEY_5", 77)
    doppelganger.__setitem__("KEY_6", 77)
    doppelganger.__setitem__("KEY_7", 77)
    doppelganger.__setitem__("KEY_8", 77)
    doppelganger.__setitem__("KEY", "VALUE")
    doppelganger.__setitem__("KEY_2", 77)
    doppelganger.__setitem__("KEY_3", 77)
    doppelganger.__setitem__("KEY_4", 77)
    doppelganger.__setitem__("KEY_5", 77)
    doppelganger.__setitem__("KEY_6", 77)
    doppelganger.__setitem__("KEY_7", 77)
    doppelganger.__setitem__("KEY_8", 77)
    print(doppelganger)

    print("____________________________")

    # guido_dict = {1: "one", 2: {"two"}, None: ":)", ":)": None}  # Original
    # guido_dict[":)"] = guido_dict[1]
    # print(f"Py dict example : {guido_dict}")
    # point_for_tests = Point(1, 2)
    # point_for_tests_2 = Point(3, 4)
    # print(point_for_tests)
    # print(point_for_tests_2)


@timer_decorator
def two_diff_lists():  # TODO: DELETE IT
    custom_num = 10_000_000
    custom_index_we_lf = 5_000_000
    big_list = [i for i in range(custom_num)]
    big_list_2 = ["value" for i in range(custom_num)]
    result = [big_list[custom_index_we_lf], big_list_2[custom_index_we_lf]]
    print(result)


@timer_decorator
def one_list_with_lists():  # TODO: DELETE IT
    custom_num = 10_000_000
    custom_index_we_lf = 5_000_000
    big_list = [[i, "value"]
                for i in range(custom_num)]
    result = big_list[custom_index_we_lf]
    print(result)


if __name__ == "__main__":  # TODO: DELETE IT
    quick_prints()

    # two_diff_lists()  # 3.35 <<<---------!!!!!!!!!!!!!!
    # one_list_with_lists()  # 6.40
