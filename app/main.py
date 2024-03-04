from __future__ import annotations


class Dictionary:
    def __init__(
            self,
            iterable: iter = None,
            **kwargs: any
    ) -> None:

        self.capacity = 8
        self.hash_table = [[] for _ in range(self.capacity)]
        if iterable:
            for key, value in iterable:
                self[key] = value
        if kwargs:
            for key, value in kwargs.items():
                self[key] = value

    def items(self) -> iter:
        return iter([value[0], value[1]] for value in self.hash_table if value)

    def keys(self) -> iter:
        return iter(value[0] for value in self.hash_table if value)

    def get(self, key: any) -> any:
        try:
            return self[key]
        except KeyError:
            return None

    def pop(self, key: any) -> any:
        value = self.hash_table[self.find_index(key)][1]
        self.hash_table[self.find_index(key)] = []
        return value

    def update(
            self,
            iterable: dict | Dictionary = None,
            **kwargs
    ) -> None:

        if iterable:
            for key, value in iterable.items():
                self[key] = value
        else:
            for key, value in kwargs.items():
                self[key] = value

    def clear(self) -> None:
        self.capacity = 8
        self.hash_table = [[] for _ in range(self.capacity)]

    def find_index(self, key: any) -> int:
        index = hash(key) % self.capacity
        for _ in range(self.capacity):
            if key not in self.hash_table[index % self.capacity]:
                index = (index + 1) % self.capacity

        if hash(key) not in self.hash_table[index]:
            raise KeyError("Key does not exist")
        return index

    def __setitem__(self, key: any, value: any) -> None:
        if len(self) >= self.capacity * 0.625:
            self.capacity *= 2
            tempo = Dictionary(self.items())
            self.hash_table = [[] for _ in range(self.capacity)]
            self.update(tempo)

        index = hash(key) % self.capacity
        if key in self.keys():
            self.hash_table[self.find_index(key)][1] = value
            return
        while self.hash_table[index]:
            index = (index + 1) % self.capacity
        self.hash_table[index] = [key, value, hash(key)]

    def __getitem__(self, item: any) -> any:
        index = self.find_index(item)
        try:
            return self.hash_table[index][1]
        except IndexError:
            raise KeyError("Key does not exist")

    def __delitem__(self, key: any) -> None:
        self.hash_table[self.find_index(key)] = []

    def __iter__(self) -> iter:
        return iter(value[1] for value in self.hash_table if value)

    def __len__(self) -> int:
        return [1 for socket in self.hash_table if socket].__len__()

    def __str__(self) -> str:
        return "".join("{}: {}\n".format(
            socket[0], socket[1]) for socket in self.hash_table if socket
        )
