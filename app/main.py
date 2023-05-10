from typing import Any


class Dictionary:
    def __init__(self, *args) -> None:
        self.nodelist = []
        self.capacity = 8
        self.load_factor = 2 / 3
        self.hash_table = [[i] for i in range(self.capacity)]
        self.reinit(args)

    def reinit(self, args: list) -> None:
        while len(args) > self.capacity * self.load_factor:
            self.capacity *= 2
        self.hash_table = [[i] for i in range(self.capacity)]
        for key_value in args:
            key = key_value[0]
            value = key_value[1]
            current_node = hash(key) % self.capacity
            for i in range(self.capacity):
                correction = 0
                if current_node + i >= self.capacity:
                    correction = self.capacity - 1
                hash_node = self.hash_table[current_node + i - correction]
                if len(hash_node) == 1:
                    hash_node.append(
                        [hash(key), key, value]
                    )
                    break

    def __setitem__(self, key: Any, value: Any) -> Any:
        if self.__len__() + 1 > self.capacity * self.load_factor:
            reinit_args = []
            for i in range(self.capacity):
                check_node = self.hash_table[i]
                if len(check_node) != 1:
                    reinit_args.append((check_node[1][1], check_node[1][2]))
            self.reinit(tuple(reinit_args))

        current_node = hash(key) % self.capacity
        for i in range(self.capacity):
            if current_node + i >= self.capacity:
                hash_node = self.hash_table[
                    current_node + i - self.capacity - 1
                ]
            else:
                hash_node = self.hash_table[current_node + i]
            if len(hash_node) == 1:
                hash_node.append(
                    [hash(key), key, value]
                )
                break
            elif hash_node[1][1] == key:
                hash_node[1][2] = value
                break

    def __getitem__(self, key: Any) -> Any:
        current_node = hash(key) % self.capacity
        for i in range(self.capacity):
            if current_node + i >= self.capacity:
                check_node = self.hash_table[
                    current_node + i - self.capacity - 1
                ]
            else:
                check_node = self.hash_table[current_node + i]
            if len(check_node) != 1:
                try:
                    if (
                            check_node[1][0] == hash(key)
                            and check_node[1][1]
                    ) == key:
                        return check_node[1][2]
                except KeyError as error:
                    raise error
            else:
                raise KeyError

    def __len__(self) -> int:
        result = 0
        for i in range(self.capacity):
            if len(self.hash_table[i]) != 1:
                result += 1
        return result
