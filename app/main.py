from typing import Any


class Dictionary:
    def __init__(self, size: int = 8, load_factor: float = 0.66) -> None:
        self.size = size
        self.hash_table = [None] * size
        self.length = 0
        self.load_factor = load_factor

    def __setitem__(self, key: Any, value: Any) -> None:
        if self.length / self.size >= self.load_factor:
            self._resize()

        index = hash(key) % self.size
        end_index = index - 1
        while end_index != index:
            if ((is_in_table := (self.hash_table[index]
                                 and self.hash_table[index][1] == key))
                    or self.hash_table[index] is None):
                if not is_in_table:
                    self.length += 1
                self.hash_table[index] = (hash(key), key, value)
                return
            index = 0 if index + 1 > len(self.hash_table) - 1 else index + 1

    def __getitem__(self, key: Any) -> Any:
        index = hash(key) % self.size
        end_index = index - 1
        while end_index != index:
            if (self.hash_table[index]
                    and self.hash_table[index][0] == hash(key)
                    and self.hash_table[index][1] == key):
                return self.hash_table[index][2]
            index = 0 if index + 1 > len(self.hash_table) - 1 else index + 1
        raise KeyError(f"There is not key: {key}")

    def __len__(self) -> int:
        return self.length

    def _resize(self) -> None:
        self.size *= 2
        new_hash_table = [None] * self.size

        for item in self.hash_table:
            if item is None:
                continue
            index = item[0] % self.size
            end_index = index - 1
            while end_index != index:
                if ((new_hash_table[index]
                     and new_hash_table[index][1] == item[1])
                        or not new_hash_table[index]):
                    new_hash_table[index] = item
                    break
                index = (0 if index + 1 > len(self.hash_table) - 1
                         else index + 1)
        self.hash_table = new_hash_table

    def clear(self) -> None:
        self.hash_table = [None] * self.size
        self.length = 0

    def get(self, key: Any) -> Any:
        try:
            return self[key]
        except KeyError:
            return None
