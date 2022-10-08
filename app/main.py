from copy import deepcopy
from typing import Any, Hashable


class Dictionary:
    def __init__(self) -> None:
        self.size = 8
        self.lenght = 0
        self.dict_ = [None for i in range(self.size)]

    def resize(self) -> None:
        if len(self) > (self.size * (2 / 3)):
            self.lenght = 0
            temp_ = deepcopy(self.dict_)
            self.size *= 2
            self.dict_ = [None for _ in range(self.size)]
            for el in temp_:
                if el is not None:
                    self[el[0]] = el[2]

    def __len__(self) -> int:
        return self.lenght

    def __setitem__(self, key: Hashable, value: Any) -> None:
        hash_ = hash(key)
        index_ = hash_ % self.size
        while self.dict_[index_]:
            if self.dict_[index_] and self.dict_[index_][0] == key:
                self.dict_[index_] = [key, hash_, value]
                return
            index_ = (index_ + 1) % self.size
        self.dict_[index_] = [key, hash_, value]
        self.lenght += 1
        self.resize()

    def __getitem__(self, key: Hashable) -> None:
        index_ = hash(key) % self.size
        for _ in range(self.size):
            if self.dict_[index_] and self.dict_[index_][0] == key:
                return self.dict_[index_][2]
            index_ = (index_ + 1) % self.size
        raise KeyError(f"{key}")
