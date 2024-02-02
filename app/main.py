from typing import Any, Hashable


class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.contained = [None] * self.capacity
        self.size = 0
        self.load_factor = 2 / 3

    def hash(self, key: Hashable) -> int:
        hash_code = hash(key)
        return hash_code % self.capacity

    def increase(self, new_capacity: int) -> None:
        old_table = self.contained
        self.contained = [None] * new_capacity
        self.capacity = new_capacity
        self.size = 0

        for nodes in old_table:
            if nodes is not None:
                for node in nodes:
                    self[node[0]] = node[2]

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.size / self.capacity > self.load_factor:
            self.increase(self.capacity * 2)

        index = self.hash(key)
        contained_data = [key, index, value]

        if self.contained[index] is None:
            self.contained[index] = []

        for existing_node in self.contained[index]:
            if existing_node[0] == key:
                existing_node[2] = value
                return

        self.contained[index].append(contained_data)
        self.size += 1

    def __getitem__(self, key: Hashable) -> Any | None:
        index = self.hash(key)

        if self.contained[index] is None:
            raise KeyError(f"Key {key} not found")

        for node in self.contained[index]:
            if node[0] == key:
                return node[2]

        raise KeyError(f"Key {key} not found")

    def __len__(self) -> None:
        return self.size
