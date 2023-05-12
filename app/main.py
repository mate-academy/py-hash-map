from typing import Any


class Dictionary:
    def __init__(self, *args) -> None:
        self.hash_table = None
        self.capacity = 8
        self.load_factor = 2 / 3
        self.reinit(args)

    def reinit(self, args: list) -> None:
        while len(args) > self.capacity * self.load_factor:
            self.capacity *= 2
        self.hash_table = [[] for i in range(self.capacity)]
        for key_value in args:
            key, value = key_value
            current_node = hash(key) % self.capacity
            node_step = 0
            hash_node = self.hash_table[current_node]
            while len(hash_node) != 0:
                node_step += 1
                if current_node + node_step >= self.capacity:
                    node_step -= self.capacity
                hash_node = self.hash_table[current_node + node_step]
            hash_node.append(
                [hash(key), key, value]
            )

    def __setitem__(self, key: Any, value: Any) -> None:
        if self.__len__() + 1 > self.capacity * self.load_factor:
            reinit_args = []
            for i in range(self.capacity):
                check_node = self.hash_table[i]
                if len(check_node) != 0:
                    reinit_args.append((check_node[0][1], check_node[0][2]))
            self.reinit(list(reinit_args))

        current_node = hash(key) % self.capacity
        node_step = 0
        hash_node = self.hash_table[current_node]
        while len(hash_node) != 0:
            if hash_node[0][1] == key:
                hash_node[0][2] = value
                break
            node_step += 1
            if current_node + node_step >= self.capacity:
                node_step -= self.capacity
            hash_node = self.hash_table[current_node + node_step]
        hash_node.append(
            [hash(key), key, value]
        )

    def __getitem__(self, key: Any) -> Any:
        current_node = hash(key) % self.capacity
        node_step = 0
        hash_node = self.hash_table[current_node]
        while len(hash_node) != 0:
            try:
                if hash_node[0][0] == hash(key) and hash_node[0][1] == key:
                    return hash_node[0][2]
            except KeyError as error:
                raise error
            node_step += 1
            if current_node + node_step >= self.capacity:
                node_step -= self.capacity
            hash_node = self.hash_table[current_node + node_step]
        raise KeyError

    def __len__(self) -> int:
        result = 0
        for i in range(self.capacity):
            if len(self.hash_table[i]) != 0:
                result += 1
        return result
