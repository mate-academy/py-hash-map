from typing import Any


class Dictionary:
    def __init__(self, capacity: int = 8) -> None:
        self.capacity = capacity
        self.size = 0
        self.table = [[] for _ in range(self.capacity)]

    def get_hash(self, key: Any) -> int:
        return hash(key) % self.capacity

    def __setitem__(self, key: Any, value: Any) -> None:
        if self.size >= self.capacity * 2 / 3:
            self.resize()

        hash_index = self.get_hash(key)
        slot = self.table[hash_index]

        for index, (existing_key, existing_value) in enumerate(slot):
            if existing_key == key:
                slot[index] = (key, value)
                break
        else:
            slot.append((key, value))
            self.size += 1

    def __getitem__(self, key: Any) -> Any:
        hash_index = self.get_hash(key)
        slot = self.table[hash_index]

        for existing_key, existing_value in slot:
            if existing_key == key:
                return existing_value

        raise KeyError(f"Key '{key}' not found")

    def __len__(self) -> int:
        return self.size

    def resize(self) -> None:
        self.capacity *= 2
        new_table = [[] for _ in range(self.capacity)]

        for bucket in self.table:
            for key, value in bucket:
                hash_index = hash(key) % self.capacity
                new_table[hash_index].append((key, value))

        self.table = new_table
