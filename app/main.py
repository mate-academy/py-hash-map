from typing import Any, Hashable


class Dictionary:
    def __init__(self) -> None:
        self._length: int = 0
        self._hash_table: list = [None] * 8
        self._hash_size: int = 8
        self._resize_factor: float | int = 2 / 3
        self._resize_multiplier: int = 2

    def __setitem__(self, key: Hashable, value: Any) -> None:
        self._hash_size_check_increase()
        key_hash_position = self._find_key_position(key)

        while self._hash_table[key_hash_position]:
            if self._hash_table[key_hash_position][0] == key:
                self._hash_table[key_hash_position][1] = value
                return print(f"value with key '{key}' were rewritten")
            key_hash_position = (key_hash_position + 1) % self._hash_size

        self._hash_table[key_hash_position] = [key, value]
        self._length += 1
        print(f"'key:value = {key}:{value}' "
              f"is set to {key_hash_position} index in the Dictionary")

    def __getitem__(self, item: Hashable) -> Any | None:
        key_hash_position = self._find_key_position(item)

        # find item by key_hash_position and if it has the right key to it
        while self._hash_table[key_hash_position]:
            if self._hash_table[key_hash_position][0] == item:
                return self._hash_table[key_hash_position][1]
            key_hash_position = (key_hash_position + 1) % self._hash_size

        raise KeyError("Key is not found in the Dictionary")

    def __len__(self) -> int:
        return self._length

    def __repr__(self) -> str:
        result = [f"{item[0]}:{item[1]}"
                  for item in self._hash_table
                  if item is not None]
        return "{" + ", \n".join(result) + "}"

    def __delitem__(self, key: Hashable) -> None:
        key_hash_position = self._find_key_position(key)

        while self._hash_table[key_hash_position]:
            if self._hash_table[key_hash_position][0] == key:
                self._hash_table[key_hash_position] = None
                print(f"removed: {key} from position {key_hash_position}")
                return
            key_hash_position = (key_hash_position + 1) % self._hash_size

        raise KeyError("Key is not found in the Dictionary")

    def pop(self, key: Hashable) -> Any:
        result = self.__getitem__(key)
        self.__delitem__(key)
        return result

    def get(self, key: Hashable) -> Any | None:
        """
        Works same as __getitem__ but
        doesn't return KeyError if key doesn't exist
        """
        try:
            self.__getitem__(key)
        except KeyError:
            return None
        else:
            return self.__getitem__(key)

    def clear(self) -> None:
        self._hash_table = [None] * 8
        self._hash_size = 8
        self._length = 0

    def _find_key_position(self, key: Hashable) -> int:
        try:
            key_hash_position = hash(key) % self._hash_size
        except TypeError as e:
            raise TypeError(e)
        else:
            return key_hash_position

    def _hash_size_check_increase(self) -> None:
        """Supporting func to check and increase hash_table size when needed"""

        if self.__len__() == int(self._hash_size * self._resize_factor):
            self._hash_size *= self._resize_multiplier
            temp_hash_table = [None] * self._hash_size
        else:
            return

        for item in self._hash_table:
            if item:
                item_key_hash_position = hash(item[0]) % self._hash_size
                # check so they don't overwrite each-other
                while temp_hash_table[item_key_hash_position]:
                    item_key_hash_position = ((item_key_hash_position + 1)
                                              % self._hash_size)
                temp_hash_table[item_key_hash_position] = item
        self._hash_table = temp_hash_table
        print(f"Dictionary size were increased "
              f"from {self._hash_size // self._resize_multiplier} "
              f"to {self._hash_size}")
