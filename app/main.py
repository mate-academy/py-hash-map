from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.size = 0
        self.threshold = 5
        self.nodes = [(0, 0, 0)] * self.capacity

    def __str__(self) -> str:
        return ("{"
                + ", ".join(
                    [
                        f"{node[0]}: {node[2]}"
                        for node in self.nodes if any(node)
                    ]
                )
                + "}")

    def __setitem__(
            self,
            key: Any,
            value: Any
    ) -> None:

        if self.size >= self.threshold:
            self.resize()

        key_hash = hash(key)
        key_index = self.get_index(key)
        if key != self.nodes[key_index][0]:
            self.size += 1
        self.nodes[key_index] = (key, key_hash, value)

    def __getitem__(
            self,
            key: Any
    ) -> Any:
        key_index = self.get_index(key)
        if not any(self.nodes[key_index]):
            raise KeyError
        return self.nodes[key_index][2]

    def __len__(self) -> int:
        return self.size

    def resize(self) -> None:
        self.capacity *= 2
        self.threshold = self.capacity * 2 / 3

        old_nodes = self.nodes.copy()

        self.nodes = [(0, 0, 0)] * self.capacity
        for node in old_nodes:
            key_index = self.get_index(node[0])
            self.nodes[key_index] = node

    def get_index(
            self,
            key: Any
    ) -> int:
        # return unoccupied index for node
        key_hash = hash(key)
        key_index = key_hash % self.capacity

        while any(self.nodes[key_index]):

            if key == self.nodes[key_index][0]:
                return key_index

            key_index = (key_index + 1) % self.capacity

        return key_index

    def clear(self) -> None:
        self.capacity = 8
        self.size = 0
        self.threshold = 5
        self.nodes = [(0, 0, 0)] * self.capacity

    def __delitem__(
            self,
            key: Any
    ) -> None:
        key_index = self.get_index(key)
        if not any(self.nodes[key_index]):
            raise KeyError
        self.nodes[key_index] = (0, 0, 0)
        self.size -= 1

    def get(
            self,
            key: Any,
            value: Any = None

    ) -> Any:
        try:
            return self.__getitem__(key)
        except KeyError:
            return value

    def pop(
            self,
            key: Any,
            value: None
    ) -> Any:
        try:
            value = self.__getitem__(key)
            self.__delitem__(key)
            return value
        except KeyError:
            return value

    def __iter__(self) -> object:
        self.index = -1
        self.iter_nodes = [node for node in self.nodes if any(node)]
        return self

    def __next__(self) -> Any:
        if self.index >= self.size:
            raise StopIteration
        self.index += 1
        return self.iter_nodes[self.index][0]

    def update(
            self,
            iterable: Any
    ) -> None:
        for key in iterable:
            self.__setitem__(key, iterable[key])
