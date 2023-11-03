from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.capacity = 8
        self.hash_table: list = [None] * self.capacity

    def resize_table(self) -> None:

        self.capacity *= 2
        new_table = [None] * self.capacity

        for node_list in self.hash_table:
            if node_list:
                for key, value in node_list:

                    index = hash(key) % self.capacity

                    if new_table[index] is None:
                        new_table[index] = [(key, value)]
                    else:
                        new_table[index].append((key, value))

        self.hash_table = new_table

    def __setitem__(self, key: Any, value: Any) -> None:

        if self.length >= self.capacity * 2 / 3:
            self.resize_table()

        index = hash(key) % self.capacity

        if self.hash_table[index] is None:
            self.hash_table[index] = [(key, value)]
            self.length += 1
        else:
            for idx, (exist_key, _) in enumerate(self.hash_table[index]):
                if exist_key == key:
                    self.hash_table[index][idx] = (key, value)
                    break
            else:
                self.hash_table[index].append((key, value))
                self.length += 1

    def __getitem__(self, key: Any) -> Any:
        index = hash(key) % self.capacity
        if self.hash_table[index] is not None:
            for exist_key, value in self.hash_table[index]:
                if exist_key == key:
                    return value
        raise KeyError(key)

    def __len__(self) -> int:
        return self.length
