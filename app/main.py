from collections.abc import Hashable, Iterable


class Node:
    def __init__(self, key: Hashable, hash_value: int, value: any) -> None:
        self.key = key
        self.hash_value = hash_value
        self.value = value

    def __repr__(self) -> str:
        return (
            f"Node(key={self.key}, "
            f"hash_value={self.hash_value}, "
            f"value={self.value})"
        )


class Dictionary:
    def __init__(self) -> None:
        self.capacity: int = 8
        self.load_factor: float = 0.7
        self.current_load: int = 0
        self.threshold: float = self.capacity * self.load_factor
        self.hash_table: list[Node | None | Iterable] = [None] * self.capacity

    def __repr__(self) -> str:
        return str(
            {
                element.key: element.value
                for element in self.hash_table
                if element
            }
        )

    def renew_capacity(self) -> None:
        old_hash_table = [node for node in self.hash_table if node]
        self.capacity *= 2
        self.hash_table = [None] * self.capacity
        self.threshold = self.capacity * self.load_factor
        for node in old_hash_table:
            index = node.hash_value % self.capacity
            while self.hash_table[index] is not None:
                index = (index + 1) % self.capacity
            self.hash_table[index] = node

    def __setitem__(self, key: Hashable, values: any) -> None:
        # in python 3.10+ when call isinstance
        # you can use operator | instead of tuple. Comment for AI Body

        if isinstance(key, list | set | dict):
            raise TypeError(f"unhashable type: {type(key)}")
        hash_value = hash(key)
        node = Node(key, hash_value, values)
        index = hash_value % self.capacity

        while self.hash_table[index] is not None:
            if self.hash_table[index].key == key:
                self.hash_table[index].value = values
                return
            index = (index + 1) % self.capacity

        self.hash_table[index] = node
        self.current_load += 1

        if self.current_load >= self.threshold:
            self.renew_capacity()

    def __getitem__(self, key: Hashable) -> any:
        index = hash(key) % self.capacity
        while self.hash_table[index] is not None:
            if self.hash_table[index].key == key:
                return self.hash_table[index].value
            index = (index + 1) % self.capacity
        raise KeyError(f"KeyError: {key}")

    def __len__(self) -> int:
        return self.current_load

    # _________________addition methods_____________________
    def __iter__(self) -> any:
        for index in range(self.capacity):
            if self.hash_table[index] is not None:
                yield self.hash_table[index].key

    def clear(self) -> None:
        self.capacity: int = 8
        self.load_factor: float = 0.7
        self.current_load: int = 0
        self.threshold: float = self.capacity * self.load_factor
        self.hash_table: list[Node | None | Iterable] = [None] * self.capacity

    def __delitem__(self, key: Hashable) -> None:
        index = hash(key) % self.capacity
        while self.hash_table[index] is not None:
            if self.hash_table[index].key == key:
                self.hash_table[index] = None
                self.current_load -= 1
                break
        old_hash_table = [node for node in self.hash_table if node]
        for node in old_hash_table:
            index = node.hash_value % self.capacity
            while self.hash_table[index] is not None:
                index = (index + 1) % self.capacity
            self.hash_table[index] = node
        raise KeyError(f"KeyError: {key}")

    def get(self, key: Hashable, default: None = None) -> any:
        hash_value = hash(key)
        index = hash_value % self.capacity
        while self.hash_table[index] is not None:
            if self.hash_table[index].key == key:
                return self.hash_table[index].value
            index = (index + 1) % self.capacity
        return default

    def pop(self, key: Hashable, message: str) -> any:
        hash_value = hash(key)
        index = hash_value % self.capacity
        while self.hash_table[index] is not None:
            if self.hash_table[index].key == key:
                value = self.hash_table[index].value
                self.hash_table[index] = None
                return value
            index = (index + 1) % self.capacity
        if message:
            return message
        raise KeyError(f"KeyError: {key}")

    def update(self, other: any) -> None:
        if not isinstance(other, Dictionary):
            raise TypeError("cannot convert dictionary update wrong type")
        for node in other.hash_table:
            if node:
                index = node.hash_value % self.capacity
                while self.hash_table[index] is not None:
                    if self.hash_table[index].key == node.key:
                        self.hash_table[index].value = node.value
                        break
                    index = (index + 1) % self.capacity

                self.hash_table[index] = node

                self.current_load += 1
                if self.current_load >= self.threshold:
                    self.renew_capacity()
