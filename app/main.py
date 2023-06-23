from typing import Hashable, Any


class Dictionary:
    initial_capacity: int = 8
    load_factor: float = 2 / 3

    def __init__(self, capacity: int = initial_capacity) -> None:
        self.initial_capacity = capacity
        self.load_factor = Dictionary.load_factor
        self.size = 0
        self.capacity = self.initial_capacity
        self.table = [None] * self.capacity

    def __setitem__(self,
                    key: Hashable,
                    value: Any) -> None:
        self._check_resize()
        index = self._get_index(key)
        if self.table[index] is None:
            self.table[index] = []
        nodes = self.table[index]
        for node in nodes:
            if node[0] == key:
                node[2] = value
                return
        nodes.append([key, hash(key), value])
        self.size += 1

    def __getitem__(self,
                    key: Hashable
                    ) -> Any:
        index = self._get_index(key)
        nodes = self.table[index]
        if not nodes:
            raise KeyError(f"{key} not found")
        for node in nodes:
            if node[0] == key:
                return node[2]

    def __len__(self) -> int:
        return self.size

    def _get_index(self,
                   key: Hashable
                   ) -> int:
        hash_value = hash(key)
        return hash_value % self.capacity

    def _check_resize(self) -> None:
        load_factor = self.size / self.capacity
        if load_factor >= self.load_factor:
            self._resize()

    def _resize(self) -> None:
        old_hash_table = self.table

        self.__init__(self.capacity * 2)

        for node in old_hash_table:
            if node is not None:
                self.__setitem__(node[0][0], node[0][2])

    def clear(self) -> None:
        self.table = [None] * self.initial_capacity
        self.size = 0
