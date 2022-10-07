from typing import Any, Hashable


class Dictionary:
    def __init__(self) -> None:
        self.size = 8
        self.dict_ = [None for i in range(self.size)]

    def resize(self) -> None:
        temp_ = [el for el in self.dict_ if el is not None]
        if len(temp_) > (self.size * (2 / 3)):
            self.size *= 2
            self.dict_ = [None for _ in range(self.size)]
            for el in temp_:
                self.__setitem__(el[0], el[2])

    def __len__(self) -> int:
        return len([el for el in self.dict_ if el is not None])

    def __setitem__(self, key: Hashable, value: Any) -> None:
        hash_ = hash(key)
        index_ = hash_ % self.size
        while self.dict_[index_]:
            if self.dict_[index_] and self.dict_[index_][0] == key:
                self.dict_[index_] = [key, hash_, value]
                return
                self.resize()
            index_ = (index_ + 1) % self.size
        self.dict_[index_] = [key, hash_, value]
        self.resize()

    def __getitem__(self, key: Hashable) -> None:
        index_ = hash(key) % self.size
        counter = 0
        while counter <= (self.size + 1):
            for i in range(index_, self.size):
                if self.dict_[index_] and self.dict_[index_][0] == key:
                    return self.dict_[index_][2]
                index_ = i % self.size
                counter += 1
        raise KeyError
