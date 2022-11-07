import copy
from typing import Union, Any


class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.capacity = 8
        self.hash_table = [[] for i in range(self.capacity)]

    def __setitem__(self,
                    key: Union[int, float, str, tuple, bool],
                    value: Any
                    ) -> None:
        if self.length >= self.capacity * 2 / 3:
            self.length = 0
            self.capacity *= 2
            old_table = copy.deepcopy(self.hash_table)
            self.hash_table = [[] for i in range(self.capacity)]
            for item in old_table:
                if len(item) > 1:
                    self.adding_item(item[0], item[2])

        self.adding_item(key, value)

    def adding_item(self,
                    key: Union[int, float, str, tuple, bool],
                    value: Any
                    ) -> None:
        hash_ = hash(key)
        index_ = hash_ % self.capacity
        while True:
            if len(self.hash_table[index_]) < 1:
                self.hash_table[index_] = ([key, hash_, value])
                self.length += 1
                break
            if self.hash_table[index_][0] == key \
                    and self.hash_table[index_][1] == hash_:
                self.hash_table[index_][2] = value
                break
            index_ = (index_ + 1) % len(self.hash_table)

    def __getitem__(self,
                    key: Union[int, float, str, tuple, bool]
                    ) -> Any:
        hash_ = hash(key)
        index_ = hash_ % self.capacity
        if not self.hash_table[index_]:
            raise KeyError
        for lst in self.hash_table[index_:]:
            if lst[0] == key:
                return lst[2]

    def __len__(self) -> int:
        return self.length
