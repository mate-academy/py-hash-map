from typing import Hashable, Any


class Dictionary:
    def __init__(self) -> None:
        self.hash_list = [None] * 8

    def _set_item(self, key: Hashable, value: Any) -> None:
        """This method is used inside the class for setting item"""

        _hash = hash(key)
        index = _hash % len(self.hash_list)

        for _ in range(len(self.hash_list)):
            if self.hash_list[index] is None \
                    or self.hash_list[index][0] == key:
                self.hash_list[index] = (key, _hash, value)
                break
            if index == len(self.hash_list) - 1:
                index = -1
            index += 1

    def find_item_index(self, item: Hashable) -> int:
        _hash = hash(item)
        index = _hash % len(self.hash_list)
        for _ in range(len(self.hash_list)):
            if self.hash_list[index] is None:
                continue
            if self.hash_list[index][0] == item:
                return index
            if index == len(self.hash_list) - 1:
                index = -1
            index += 1

    def hash_expand(self) -> None:
        """Method expands and restructures hash table if its required"""
        if self.hash_list.count(None) <= \
                len(self.hash_list) - len(self.hash_list) * 2 // 3:
            hash_copy = self.hash_list.copy()
            self.hash_list = [None] * len(hash_copy) * 2
            for item in hash_copy:
                if item:
                    self._set_item(item[0], item[2])

    def __setitem__(self, key: Hashable, value: Any) -> Any:
        self.hash_expand()
        self._set_item(key, value)

        return self

    def __getitem__(self, item: Hashable) -> Any:
        index = self.find_item_index(item)
        if index is not None:
            return self.hash_list[index][2]
        raise KeyError(f"{item} is not in the dict")

    def __len__(self) -> int:
        return len(self.hash_list) - self.hash_list.count(None)

    def clear(self) -> None:
        self.hash_list = [None] * 8

    def __delitem__(self, key: Hashable) -> None:
        index = self.find_item_index(key)
        if index is not None:
            self.hash_list[index] = None
        raise KeyError(f"{key} is not in the dict")

    def get(self, key: Hashable, value: Any = None) -> Any:
        index = self.find_item_index(key)
        if index is not None:
            return self.hash_list[index][2]
        self.__setitem__(key, value)
        return self.__getitem__(key)

    def pop(self, key: Hashable) -> Any:
        index = self.find_item_index(key)
        if index is not None:
            value = self.hash_list[index]
            self.hash_list[index] = None
            return value
        raise KeyError(f"{key} is not in the dict")

    def update(self, keys_values: tuple) -> None:
        key, value = keys_values
        self.__setitem__(key, value)

    def __iter__(self) -> Any:
        self.iter_list = []
        for item in self.hash_list:
            if item is not None:
                self.iter_list.append(item)
        self.index = 0
        return self

    def __next__(self) -> Any:
        if self.index < self.__len__():
            result = self.iter_list[self.index]
            self.index += 1
            return result[0]
        else:
            raise StopIteration

    def __repr__(self) -> str:
        return f"{self.hash_list}"

    def __str__(self) -> str:
        self.str_list = []
        for item in self.hash_list:
            if item is not None:
                self.str_list.append(f"{item[0]}: {item[2]}")
        return f"{self.str_list}"
