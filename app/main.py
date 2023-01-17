from typing import Any, Hashable


class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.capacity = 8
        self.hash_table = [None] * self.capacity

    def __len__(self) -> int:
        return self.length

    def resize(self) -> None:
        old_hash_table = self.hash_table
        self.capacity *= 2
        self.hash_table = [None] * self.capacity
        for key_value in old_hash_table:
            if key_value:
                self.__setitem__(key_value)

    def __setitem__(self, key: Any, value: Any) -> None:
        if self.length > int(self.capacity * 2 / 3):
            self.resize()
        current_hash = hash(key)
        index = current_hash % self.capacity
        while True:
            if not self.hash_table[index]:
                self.hash_table[index] = current_hash, key, value
                self.length += 1
                break
            if current_hash == self.hash_table[index][0] and key == self.hash_table[index][1]:
                self.hash_table[index] = current_hash, key, value
                break

            else:
                while self.hash_table[index]:
                    index += 1
                self.hash_table[index % self.capacity] = current_hash, key, value
                break

    def __getitem__(self, key: Any) -> Any:
        current_hash = hash(key)
        index = current_hash % self.capacity
        if self.hash_table[index]:
            if self.hash_table[index][1] == key:
                return self.hash_table[index][2]
            else:
                for i in range(self.capacity):
                    if key == self.hash_table[i][1]:
                        return self.hash_table[index][2]
                    else:
                        raise KeyError
