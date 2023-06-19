from datetime import date, datetime
from enum import Enum
from typing import Any, Union


class Dictionary:
    """
    Dict(object) clone

    some_dict = {"One": 1}          => {"Key": "value"}
    var = Dictionary_obj("One", 1)  => [("One", 1)]
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
        approved_data_types = [int, float, complex, str, bool, tuple,
                               frozenset, bytes, None, Enum, date, datetime]
        if type(key) not in approved_data_types:
            raise TypeError(f"unhashable type: '{type(key).__name__}'")
        self.key = key
        self.value = value

    def __setitem__(self, key, value) -> None:  # mandatory
        """ Set self[key] to value. """
        self.key = key
        self.value = value
        pass

    def __getitem__(self, key) -> Any:  # mandatory
        """ x.__getitem__(y) <==> x[y] """

    def __len__(self) -> int:  # mandatory
        """ Return len(self). """

    def clear(self) -> None:  # extra
        """ D.clear() -> None.  Remove all items from D. """
        print("NO")

    def __delitem__(self, key) -> None:  # extra
        """ Delete self[key]. """

    def get(self):  # extra #
        """
        Return the value for key if key is in the dictionary,
        else default.
        """

    def pop(self):  # extra
        """
        D.pop(k[,d]) -> v, remove specified key
        and return the corresponding value.

        If the key is not found, return the default if given; otherwise,
        raise a KeyError.
        """

    def update(self):  # extra
        """
        D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
        If E is present and has a .keys() method, then does:
            for k in E: D[k] = E[k]
        If E is present and lacks a .keys() method, then does:
            for k, v in E: D[k] = v
        In either case, this is followed by: for k in F:  D[k] = F[k]
        """

    def __iter__(self):  # extra
        """ Implement iter(self). """

    def hash(self):  # optional
        """
        For the list, dict, and set, we cannot get the hash value.
        Only hashed values can be hashed.
        """
        hash_capacity: int = 8
        hash_table: list = [None] * self.capacity

    def __repr__(self):  # optional
        return f"{{{self.key} : {self.value}}}"


def quick_prints():  # TODO: DELETE IT
    doppelganger = Dictionary("One", 1)  # Custom
    print(f"REPR EXAMPLE: {doppelganger}")
    print(doppelganger.__dict__)
    print(f"KEY: {doppelganger.key}")
    print(f"VALUE: {doppelganger.value}")
    print("____________________________")

    guido_dict = {1: "one", 2: {"two"}, None: ":)", ":)": None}  # Original
    guido_dict[":)"] = guido_dict[1]
    print(guido_dict)


if __name__ == "__main__":
    quick_prints()
