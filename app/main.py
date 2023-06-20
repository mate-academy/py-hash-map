from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.capacity = 8
        self.load_factor = 5
        self.hash_table: list = [None] * self.capacity
        self.capacity_cases = [None] * self.capacity
        self.keys = [None] * self.capacity

    def __len__(self) -> int:
        return self.length

    def __setitem__(self, key: Any, value: Any) -> None:
        if self.length > self.load_factor:
            self.resize()

        self.append_item_to_hash_table(key, value, self.hash_table, self.keys)

    def append_item_to_hash_table(
            self,
            key: Any,
            value: Any,
            hash_table: list[list | None],
            keys: list[Any]
    ) -> None:
        if key in keys:
            hash_index = keys.index(key)
            hash_table[hash_index][-1] = value
            return

        hash_index = hash(key) % self.capacity

        if hash_table[hash_index] is not None:
            hash_index = hash_table.index(None)

        hash_table[hash_index] = [key, hash(key), value]
        self.capacity_cases[hash_index] = key
        keys[hash_index] = key
        self.length += 1

    def __getitem__(self, key: Any) -> Any:
        if key not in self.keys:
            raise KeyError

        hash_index = hash(key) % self.capacity

        if self.hash_table[hash_index][0] == key:
            return self.hash_table[hash_index][-1]

        hash_index = self.capacity_cases.index(key)

        return self.hash_table[hash_index][-1]

    def resize(self) -> None:
        self.length = 0
        self.capacity *= 2
        self.load_factor = int(self.capacity * (2 / 3))
        self.capacity_cases = [None] * self.capacity
        keys = [None] * self.capacity
        resized_hash_table = [None] * self.capacity

        for item in self.hash_table:
            if item is not None:
                self.append_item_to_hash_table(
                    item[0], item[-1], resized_hash_table, keys
                )

        self.hash_table = resized_hash_table
        self.keys = keys
