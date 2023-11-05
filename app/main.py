from typing import Any


class Dictionary:
    count_value_in_dict = 0

    def __init__(self, capacity: int = 8) -> None:
        self.capacity = capacity
        self.key = [[] for _ in range(self.capacity)]
        self.value = [[] for _ in range(self.capacity)]
        self.count_of_jump = []

    def add_value_in_dict(
        self,
        key: Any,
        value: Any,
        ls_key: list,
        ls_value: list,
        ls_buf_count: list
    ) -> None:
        buffer = abs(hash(key) % self.capacity)
        count = 0
        while ls_key[buffer]:
            count += 1
            buffer -= 1
        ls_key[buffer] = key
        ls_value[buffer] = value
        ls_buf_count.append(key)
        ls_buf_count.append(count)

    def __setitem__(self, key: Any, value: Any) -> None:
        if key in self.key:
            if key in self.count_of_jump:
                self.value[
                    hash(key)
                    % self.capacity
                    - self.count_of_jump[
                        self.count_of_jump.index(key) + 1
                    ]
                ] = value
            else:
                self.value[hash(key) % self.capacity] = value
        else:
            self.add_value_in_dict(
                key,
                value,
                self.key,
                self.value,
                self.count_of_jump
            )
            self.count_value_in_dict += 1
            if self.count_value_in_dict >= round(self.capacity * 2 / 3):
                self.revenge()

    def revenge(self) -> None:
        self.capacity *= 2
        new_dict_key = [[] for _ in range(self.capacity)]
        new_dict_value = [[] for _ in range(self.capacity)]
        new_dict_of_jump = []
        for i in range(len(self.key)):
            if self.key[i]:
                self.add_value_in_dict(
                    self.key[i],
                    self.value[i],
                    new_dict_key,
                    new_dict_value,
                    new_dict_of_jump
                )
        self.key = new_dict_key
        self.value = new_dict_value
        self.count_of_jump = new_dict_of_jump

    def __getitem__(self, item: Any) -> Any:
        if item not in self.key:
            raise KeyError
        if item in self.count_of_jump:
            return self.value[
                hash(item) % self.capacity
                - self.count_of_jump[self.count_of_jump.index(item) + 1]
            ]
        return self.value[hash(item) % self.capacity]

    def __len__(self) -> int:
        return self.count_value_in_dict
