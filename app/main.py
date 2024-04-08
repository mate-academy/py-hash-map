from typing import Any, Hashable


class Dictionary:
    def __init__(self,
                 hash_size: int = 8,
                 resize_factor: float = 2 / 3,
                 resize_multiplier: int = 2) -> None:
        self.length = 0
        self.hash_table: list = [None] * 8
        self.hash_size = hash_size
        self.resize_factor = resize_factor
        self.resize_multiplier = resize_multiplier

    def __setitem__(self, key: Hashable, value: Any) -> None:
        self._hash_size_check_increase()

        key_hash_position = hash(key) % self.hash_size

        while self.hash_table[key_hash_position]:
            if self.hash_table[key_hash_position][0] == key:
                self.hash_table[key_hash_position][1] = value
                return print(f"value with key '{key}' were rewritten")
            key_hash_position = (key_hash_position + 1) % self.hash_size

        print(f"'key:value = {key}:{value}' "
              f"is set to {key_hash_position} index in the Dictionary")
        self.hash_table[key_hash_position] = [key, value]
        self.length += 1

    def __getitem__(self, item: Hashable) -> Any | None:
        key_hash_position = hash(item) % self.hash_size

        if not self.hash_table[key_hash_position]:
            raise KeyError("No such item in the Dictionary")

        # find item by key_hash_position and if it has the right key to it
        while self.hash_table[key_hash_position]:
            if self.hash_table[key_hash_position][0] == item:
                return self.hash_table[key_hash_position][1]
            key_hash_position = (key_hash_position + 1) % self.hash_size

        raise KeyError("Key not found in the Dictionary")

    def __len__(self) -> int:
        return self.length

    # am I allowed to use over O(1) while creating a __repr__?
    def __repr__(self) -> str:
        result = [f"{item[0]}:{item[1]}"
                  for item in self.hash_table
                  if item is not None]
        return "{" + ", \n".join(result) + "}"

    def _hash_size_check_increase(self) -> None:
        if self.__len__() == int(self.hash_size * self.resize_factor):
            self.hash_size *= self.resize_multiplier
            temp_hash_table = [None] * self.hash_size
        else:
            return

        for item in self.hash_table:
            if item:
                item_key_hash_position = hash(item[0]) % self.hash_size
                # check so they don't overwrite each-other
                while temp_hash_table[item_key_hash_position]:
                    item_key_hash_position = (
                            (item_key_hash_position + 1) % self.hash_size
                    )
                temp_hash_table[item_key_hash_position] = item
        self.hash_table = temp_hash_table
        print(f"Dictionary size were increased "
              f"from {self.hash_size // self.resize_multiplier} "
              f"to {self.hash_size}")
