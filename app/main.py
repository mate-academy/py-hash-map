from typing import Any


class Dictionary:
    def __init__(self,
                 initial_capacity: int = 8,
                 load_factor: float = 0.75
                 ) -> None:
        self.initial_capacity = initial_capacity
        self.load_factor = load_factor
        self.size = 0
        self.capacity = initial_capacity
        self.table = [None] * self.capacity

    def __setitem__(self,
                    key: int | float | str | bool | tuple,
                    value: Any) -> None:
        index = self._get_index(key)
        if self.table[index] is None:
            self.table[index] = []
        nodes = self.table[index]
        for node in nodes:
            if node[0] == key:
                node[2] = value
                return
        nodes.append((key, self._hash(key), value))
        self.size += 1
        self._check_resize()

    def __getitem__(self, key) -> Any:
        index = self._get_index(key)
        nodes = self.table[index]
        if nodes is not None:
            for node in nodes:
                if node[0] == key:
                    return node[2]
        return KeyError(key)

    def __len__(self) -> int:
        return self.size

    def _get_index(self,
                   key: int | float | str | bool | tuple
                   ) -> int:
        hash_value = hash(key)
        return hash_value % self.capacity

    @staticmethod
    def _hash(key: Any) -> int:
        if isinstance(key, list or dict or set):
            raise TypeError(f"`{type(key)}` can not be the key")
        return hash(key)

    def _check_resize(self) -> None:
        load_factor = self.size / self.capacity
        if load_factor >= self.load_factor:
            self._resize()

    def _resize(self) -> None:
        new_capacity = self.capacity * 2
        new_table = [None] * new_capacity
        for nodes in self.table:
            if nodes is not None:
                for node in nodes:
                    index = node[1] % new_capacity
                    if new_table[index] is None:
                        new_table[index] = []
                    new_table[index].append(node)
        self.capacity = new_capacity
        self.table = new_table

    def clear(self) -> None:
        self.table = [None] * self.initial_capacity
        self.size = 0
