from dataclasses import dataclass
from typing import Hashable, Any


CAPACITY = 8
TREASHOLD = 2 / 3


@dataclass
class Pair:
    key: Hashable
    value: Any


class Dictionary:
    def __init__(self, capacity: int = CAPACITY) -> None:
        self.capacity = capacity
        self.size = 0
        self.hash_table: list[Pair | None] = [None] * self.capacity

    def obtain_index(self, key: Hashable) -> None:
        index = hash(key) % self.capacity

        while (
                self.hash_table[index] is not None
                and self.hash_table[index].key != key
        ):
            index = (index + 1) % self.capacity

        return index

    @property
    def current_max_size(self) -> int:
        return self.capacity * TREASHOLD

    def resize(self) -> None:
        new_capacity = self.capacity * 2
        hash_table = self.hash_table

        self.__init__(new_capacity)

        for node in hash_table:
            if node is not None:
                self.__setitem__(node.key, node.value)

    def __setitem__(self, key: Hashable, value: Any) -> None:
        index = self.obtain_index(key)

        if self.hash_table[index] is None:
            if self.size + 1 >= self.current_max_size:
                self.resize()
                return self.__setitem__(key, value)

            self.size += 1

        self.hash_table[index] = Pair(key, value)

    def __getitem__(self, key: Hashable) -> None:
        index = self.obtain_index(key)

        if self.hash_table[index] is None:
            raise KeyError(f"Cannot find value for key: {key}")

        return self.hash_table[index].value

    def __len__(self) -> int:
        return self.size


if __name__ == "__main__":
    my_dict = Dictionary(CAPACITY)
    my_dict["one"] = 1

    print(my_dict)
