import math
from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.hash_table = [[key, None] for key in range(8)]
        self.data = []
        self.capacity = 0

    def __setitem__(self, key: Any, value: Any) -> None:
        self.data.append([key, value])
        self.create_hash_table(key, value)
        self.capacity += 1
        if self.capacity >= math.floor(len(self.hash_table) * (2 / 3)):
            self._resize()

    def __getitem__(self, item: Any) -> Any:
        for key, value in self.data:
            if key == item:
                return value
        raise KeyError(f"Key '{item}' not found in the dictionary")

    def __len__(self) -> int:
        return len(self.data)

    def create_hash_table(self, key: Any, value: Any) -> None:
        cell_index = hash(key) % len(self.hash_table)
        while True:
            if self.hash_table[cell_index][1]:
                if self.hash_table[cell_index][1][0] == key:
                    for data in self.data:
                        if data[0] == key:
                            self.data.remove(data)
                            break
                    self.hash_table[cell_index][1] = [key, hash(key), value]
                    self.capacity -= 1
                    break
                cell_index = (cell_index + 1) % len(self.hash_table)
            if self.hash_table[cell_index][1] is None:
                self.hash_table[cell_index][1] = [key, hash(key), value]
                break

    def _resize(self) -> None:
        copy_hash_table = self.hash_table.copy()
        two_times_len = len(self.hash_table) * 2
        self.hash_table = [[key, None] for key in range(two_times_len)]
        for stored_node in copy_hash_table:
            if stored_node[1] is not None:
                key = stored_node[1][0]
                value = stored_node[1][2]
                self.create_hash_table(key, value)
