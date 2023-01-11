import typing


class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.capacity = 8
        self.hash_table = [[] for _ in range(self.capacity)]

    def __len__(self) -> int:
        return self.length

    def __setitem__(self, key: typing.Hashable, value: typing.Any) -> None:
        if self.length > self.capacity * 2 / 3:
            self.resize()
        index = hash(key) % self.capacity
        if self.hash_table[index]:
            for item in self.hash_table[index]:
                if item[0] == key and hash(item[0]) == hash(key):
                    item[1] = value
                    return
        self.hash_table[index].append([key, value])
        self.length += 1

    def resize(self) -> None:
        self.capacity *= 2
        self.hash_table *= 2
        temporary_list = []
        for storage in self.hash_table:
            for item in storage:
                temporary_list.append(item)
        for item in temporary_list:
            self.__setitem__(*item)

    def __getitem__(self, key: str | int) -> list:
        index = hash(key) % self.capacity
        if not self.hash_table[index]:
            raise KeyError
        for item in self.hash_table[index]:
            if item[0] == key:
                return item[1]

    def clear(self) -> None:
        for storage in self.hash_table:
            storage.clear()
