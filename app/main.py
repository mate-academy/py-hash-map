from typing import Any


class Dictionary:
    def __init__(self, threshold: float = 2 / 3, **kwargs) -> None:
        self.threshold = threshold
        self.hash_table = [[] for _ in range(8)]

    def __setitem__(self, key, value) -> None:
        if len(self) == round(len(self.hash_table) * self.threshold):
            self.hash_table = self._double_hash_table()

        key_hash = hash(key)
        index = key_hash % len(self.hash_table)
        if self.hash_table[index]:
            if self.hash_table[index][1] == key:
                self.hash_table[index][2] = value
            else:
                print(f"{index=}")
                while self.hash_table[index]:
                    if index == len(self.hash_table) - 1:
                        index = 0
                    index += 1
                self.hash_table[index].extend([key_hash, key, value])
        else:
            self.hash_table[index].extend([key_hash, key, value])

    def _double_hash_table(self) -> list:
        new_table = [[] for _ in range(len(self.hash_table) * 2)]
        for element in self.hash_table:
            if element:
                key_hash, key, value = element
                index = key_hash % len(new_table)
                if new_table[index]:
                    while new_table[index]:
                        if index == len(new_table) - 1:
                            index = 0
                        index += 1
                new_table[index].extend([key_hash, key, value])
        return new_table

    def __getitem__(self, item) -> Any:
        item_hash = hash(item)
        index = item_hash % len(self.hash_table)
        if self.hash_table[index]:
            while self.hash_table[index][1] != item:
                if index == 0:
                    index = len(self.hash_table) - 1
                index -= 1
            return self.hash_table[index][2]
        raise KeyError

    def __len__(self) -> int:
        size = 0
        for index in self.hash_table:
            if index:
                size += 1
        return size


dictionary = Dictionary()
print(dictionary.hash_table)
print(len(dictionary))
dictionary[1] = 0
dictionary[9] = 1
print(dictionary.hash_table)

