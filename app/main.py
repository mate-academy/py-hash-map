from typing import Any


class Dictionary:
    def __init__(self, capacity: int = 8) -> None:
        self.capacity = capacity
        self.size = 0
        self.hash_table = [[] for _ in range(self.capacity)]

    def calculate_hash(self, key: Any) -> int:
        return hash(key) % self.capacity

    def __setitem__(self, key: Any, value: Any) -> None:
        index = self.calculate_hash(key)
        container = self.hash_table[index]

        for index, (key_in_container, _) in enumerate(container):
            if key_in_container == key:
                container[index] = (key, value)
                return

        container.append((key, value))
        self.size += 1

    def __getitem__(self, key: Any) -> None:
        index = self.calculate_hash(key)
        container = self.hash_table[index]

        for key_in_container, value_in_container in container:
            if key_in_container == key:
                return value_in_container

        raise KeyError(f"Key{key} not found.")

    def __len__(self) -> int:
        return self.size

    def clear(self) -> None:
        for container in self.hash_table:
            container.clear()
        self.size = 0

    def __delitem__(self, key: Any) -> None:
        index = self.calculate_hash(key)
        container = self.hash_table[index]

        for index, (key_in_container, _) in enumerate(container):
            if key_in_container == key:
                del container[index]
                self.size -= 1
                return
        raise KeyError(f"Key: {key} not found.")
