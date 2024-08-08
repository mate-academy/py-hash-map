from typing import Hashable, Any, Iterator


class Dictionary:
    def __init__(self) -> None:
        self.__iter = 0
        self.__capacity = 8
        self.__threshold = 2 / 3
        self.__table = [None] * self.__capacity
        self.__length = 0

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if not isinstance(key, Hashable):
            raise TypeError(f"unhashable type: {type(key)}")

        index = hash(key) % self.__capacity
        node = (hash(key), key, value)

        if self.__table[index]:
            for _ in range(self.__capacity):

                if key == self.__table[index][1]:
                    self.__table[index] = node
                    return

                index += 1

                if index == self.__capacity:
                    index = 0

                if not self.__table[index]:
                    break

        self.__table[index] = node
        self.__length += 1

        if self.__length > round(self.__capacity * self.__threshold):
            self.__double_capacity()

    def __getitem__(self, key: Hashable) -> Any:
        return self.__find_entry(key, False)

    def __delitem__(self, key: Hashable) -> None:
        self.__find_entry(key, True)

    def __len__(self) -> int:
        return self.__length

    def __str__(self) -> str:
        return str([
            f"Key: {entry[1]}, Val: {entry[2]}"
            for entry in self.__table
            if entry
        ])

    def __iter__(self) -> Iterator:
        self.__iter = 0
        return self

    def __next__(self) -> Any:
        while self.__iter < self.__capacity and not self.__table[self.__iter]:
            self.__iter += 1

        if self.__iter >= self.__capacity:
            raise StopIteration

        result = self.__table[self.__iter][2]
        self.__iter += 1
        return result

    def __find_entry(self, key: Hashable, erase: bool) -> Any:
        if not isinstance(key, Hashable):
            raise TypeError(f"unhashable type: {type(key)}")

        index = hash(key) % self.__capacity

        if not self.__table[index]:
            raise KeyError(f"no such key: {key}")

        while True:
            if key == self.__table[index][1]:
                temp = self.__table[index]
                if erase:
                    self.__iter = 0
                    self.__table[index] = None
                return temp[2]
            index += 1
            if index == self.__capacity:
                index = 0

    def pop(self, key: Hashable) -> Any:
        return self.__find_entry(key, True)

    def __double_capacity(self) -> None:
        self.__iter = 0
        self.__capacity *= 2
        self.__length = 0
        old_table = self.__table
        self.__table = [None] * self.__capacity

        for node in old_table:
            if node is not None:
                self.__setitem__(node[1], node[2])

    def update(self, source: dict) -> None:
        """
        Here we could use the "Iterable" type annotation to
        make the method more flexible in terms of the arguments it
        processes. Naturally, with a more complex implementation,
        but I already want to move on to the next task :)
        """
        for key, value in source.items():
            self.__setitem__(key, value)

    def clear(self) -> None:
        self.__init__()
