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

    some_dict = {"One": 1}          => {"Key": "value"}
    var = Dictionary_obj("One", 1)  => list_1: ["One"] by_index: [1]<-index[0]
    """

    def __init__(
            self,
            key: Union[
                int, float, complex, str, bool, tuple, frozenset,
                bytes, None, Enum, date, datetime
            ],
            value: Any
    ) -> None:  # mandatory
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
        approved_data_types = [int, float, complex, str, bool, tuple,
                               frozenset, bytes, None, Enum, date, datetime]
        if type(key) not in approved_data_types:
            raise TypeError(f"unhashable type: '{type(key).__name__}'")
        self.key = key
        self.value = value
        self.custom_dict_example = []

    def __setitem__(self, key, value) -> None:  # mandatory
        """ Set self[key] to value. """
        self.key = key
        self.value = value
        print("setitem testing")  # TODO: DELETE IT

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
        hash_capacity: int = 8
        hash_table: list = [None] * self.capacity
        print("hash testing")  # TODO: DELETE IT

    def __repr__(self):  # optional
        return f"{{{self.key} : {self.value}}}"


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return self.__hash__()

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __repr__(self):
        return f"Point example: x ={self.x} ; y= {self.y}"


def quick_prints():  # TODO: DELETE IT
    doppelganger = Dictionary("One", 1)  # Custom
    print(f"REPR EXAMPLE: {doppelganger}")
    print(doppelganger.__dict__)

    print("____________________________")

    guido_dict = {1: "one", 2: {"two"}, None: ":)", ":)": None}  # Original
    guido_dict[":)"] = guido_dict[1]
    print(f"Py dict example : {guido_dict}")
    point_for_tests = Point(1, 2)
    print(point_for_tests)


@timer_decorator
def two_diff_lists():  # TODO: DELETE IT
    custom_num = 1_000_000
    custom_index_we_lf = 500_000
    big_list = [i for i in range(custom_num)]
    big_list_2 = [i ** 2 for i in range(custom_num)]
    result = [big_list[custom_index_we_lf], big_list_2[custom_index_we_lf]]
    print(result)


@timer_decorator
def one_list_with_lists():  # TODO: DELETE IT
    custom_num = 1_000_000
    custom_index_we_lf = 500_000
    big_list = [[i, i ** 2]
                for i in range(custom_num)]
    result = big_list[custom_index_we_lf]
    print(result)


if __name__ == "__main__":  # TODO: DELETE IT
    quick_prints()

    two_diff_lists()  # 0.33 <<<---------!!!!!!!!!!!!!!
    one_list_with_lists()  # 0.62
