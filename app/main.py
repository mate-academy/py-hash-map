from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.length = 8
        self.load_factor = 2 / 3
        self.dictionary = [-1 for _ in range(8)]
        self.insert_elem = 0

    def __setitem__(self, key: Any, value: Any) -> None:
        hash_code = hash(key)
        index = hash_code % self.length
        if self.dictionary[index] == -1:
            self.dictionary[index] = (key, hash_code, value)
            self.insert_elem += 1
        elif (hash_code == self.dictionary[index][1]) and (
            key == self.dictionary[index][0]
        ):
            self.dictionary[index] = (key, hash_code, value)
        else:
            need_location = True
            while need_location:
                index = (index + 1) % self.length
                if self.dictionary[index] == -1:
                    self.dictionary[index] = (key, hash_code, value)
                    need_location = False
                    self.insert_elem += 1
                elif (hash_code == self.dictionary[index][1]) and (
                    key == self.dictionary[index][0]
                ):
                    self.dictionary[index] = (key, hash_code, value)
                    need_location = False
        if self.insert_elem / self.length > self.load_factor:
            self.dictionary += [-1 for _ in range(self.length)]
            self.length *= 2

    def __len__(self) -> int:
        return self.insert_elem

    def __getitem__(self, key: Any) -> Any:
        hash_code = hash(key)
        index = hash_code % self.length
        for i in range(self.length):
            index = (hash_code + i) % self.length
            if self.dictionary[index] != -1:
                if self.dictionary[index][0] == key:
                    return self.dictionary[index][2]
        raise KeyError("There is no such key.")
