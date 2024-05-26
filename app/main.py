from typing import Any, Hashable


class Dictionary:
    def __init__(self) -> None:
        self.storage_length = 8
        self.storage = [None] * self.storage_length

    def __setitem__(self, key: Hashable, value: Any) -> None:
        new_item = (key, hash(key), value)
        index = self.get_index(new_item)
        self.storage[index] = new_item
        if len([i for i in self.storage if i]) >= 2 * self.storage_length / 3:
            self.resize()

    def get_index(self, new_item: tuple) -> int:
        index = new_item[1] % self.storage_length
        for item_index, item in enumerate(self.storage):
            if item:
                if item[0] == new_item[0] and item[1] == new_item[1]:
                    return item_index
        while True:
            if not self.storage[index]:
                return index
            index = (index + 1) % self.storage_length

    def resize(self) -> None:
        temp_storage = [i for i in self.storage if i]
        self.storage_length *= 2
        self.storage = [None] * self.storage_length
        for i in temp_storage:
            self.__setitem__(i[0], i[2])
        del temp_storage

    def __getitem__(self, key: Hashable) -> Any:
        key_hash = hash(key)
        for item_ in self.storage:
            if item_:
                if item_[0] == key and item_[1] == key_hash:
                    return item_[2]
        raise KeyError(key)

    def __len__(self) -> int:
        return len([i for i in self.storage if i])

    def __repr__(self) -> str:
        if any(self.storage):
            string = "{"
            for item in self.storage:
                if item:
                    string += str(item[0]) + ": " + str(item[2]) + ", "
            string = string[:-2] + "}"
            return string
        return "{}"

    def __delitem__(self, key: Hashable) -> Any:
        key_hash = hash(key)
        print(key)
        for index_, item_ in enumerate(self.storage):
            if item_:
                if item_[0] == key and item_[1] == key_hash:
                    self.storage[index_] = None
                    return
        raise KeyError(key)

    def __iter__(self) -> tuple:
        for item in self.storage:
            if item:
                yield (item[0], item[2])

    def clear(self) -> None:
        self.__init__()

    def get(self, key: Hashable, default: Any = None) -> Any:
        key_hash = hash(key)
        for item_ in self.storage:
            if item_:
                if item_[0] == key and item_[1] == key_hash:
                    return item_[2]
        return default

    def pop(self, key: Hashable) -> Any:
        key_hash = hash(key)
        print(key)
        for index_, item_ in enumerate(self.storage):
            if item_:
                if item_[0] == key and item_[1] == key_hash:
                    value = item_[2]
                    self.storage[index_] = None
                    return value
        raise KeyError(key)

    def update(self, item: Any) -> None:
        # what foram data must be passed here? As dict? Or as **kwargs?
        # realised as a dict with use dict methods (sorry)
        for key, value in item.items():
            self.__setitem__(key, value)
