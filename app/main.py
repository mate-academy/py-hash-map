from __future__ import annotations


class DictionaryIterator:
    def __init__(self, dictionary_: Dictionary) -> None:
        self.dictionary = dictionary_
        self.current_size = self.dictionary.length
        self.current_index = 0

    def __iter__(self) -> DictionaryIterator:
        return self

    def __next__(self) -> any:
        if self.dictionary.length != self.current_size:
            raise Exception("dictionary changed size during iteration")

        while (
                self.current_index < self.dictionary.capacity
                and not self.dictionary.hash_table[self.current_index]
        ):
            self.current_index += 1

        if (
                self.current_index == self.dictionary.capacity
                or not self.dictionary.hash_table[self.current_index]
        ):
            raise StopIteration

        key = self.dictionary.hash_table[self.current_index]["key"]
        self.current_index += 1

        return key


class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.length = 0
        self.hash_table = [None] * 8
        self.load_factor = 2 / 3

    def __resize(self) -> None:
        self.capacity *= 2
        old_hash_table = self.hash_table
        self.length = 0
        self.hash_table = [None] * self.capacity

        for hash_table_value in old_hash_table:
            if hash_table_value:
                self.__setitem__(
                    hash_table_value["key"],
                    hash_table_value["value"]
                )

    def __setitem__(self, key: any, value: any) -> None:
        key_hash = hash(key)
        index = key_hash % self.capacity

        if self.hash_table[index] and self.hash_table[index]["key"] != key:
            index = (index + 1) % self.capacity
            while (
                    self.hash_table[index]
                    and self.hash_table[index]["key"] != key
            ):
                index = (index + 1) % self.capacity

        if not self.hash_table[index]:
            self.length += 1

        self.hash_table[index] = {
            "key": key,
            "hash": key_hash,
            "value": value,
        }

        if self.length > self.capacity * self.load_factor:
            self.__resize()

    def __getitem__(self, key: any) -> any:
        key_hash = hash(key)
        index = key_hash % self.capacity

        try:
            if self.hash_table[index]["key"] == key:
                return self.hash_table[index]["value"]
            else:
                while self.hash_table[index]["key"] != key:
                    index = (index + 1) % self.capacity

                return self.hash_table[index]["value"]
        except TypeError:
            raise KeyError(key)

    def __len__(self) -> int:
        return self.length

    def clear(self) -> None:
        self.capacity = 8
        self.hash_table = [None] * self.capacity
        self.length = 0

    def __rebuild(self, index: int) -> int:
        prev_index = index
        current_index = (index + 1) % self.capacity

        while current_index != index:
            hash_table_item = self.hash_table[current_index]
            if (
                    hash_table_item
                    and hash_table_item["hash"] % self.capacity == index
            ):
                self.hash_table[prev_index] = self.hash_table[current_index]
                self.hash_table[current_index] = None
                prev_index = self.__rebuild(current_index)

            current_index = (current_index + 1) % self.capacity

        return prev_index

    def __delitem__(self, key: any) -> None:
        key_hash = hash(key)
        hash_index = key_hash % self.capacity
        index = hash_index

        while (
                not self.hash_table[index]
                or self.hash_table[index]["key"] != key
        ):
            index = (index + 1) % self.capacity

            if index == hash_index:
                raise KeyError(key)

        self.hash_table[index] = None

        self.__rebuild(index)

        self.length -= 1

    def get(self, key: any, default_value: None) -> any:
        try:
            return self[key]
        except KeyError:
            return default_value

    def pop(self, key: any, default_value: None) -> any:
        value = default_value

        try:
            value = self[key]
            del self[key]
        except KeyError:
            pass

        return value

    def update(self, *args, **kwargs) -> None:
        if args and len(args) != 1:
            raise TypeError("update expected at most 1 argument, got 2")

        if args:
            if hasattr(args[0], "keys"):
                keys = args[0].keys()
                for key in keys:
                    self[key] = args[0][key]
            else:
                for index, item in enumerate(args[0]):
                    if len(item) != 2:
                        raise ValueError(
                            f"dictionary update sequence element #{index} "
                            f"has length {len(item)} but 2 is required"
                        )
                    self[item[0]] = item[1]

        if kwargs:
            for key, value in kwargs.items():
                self[key] = value

    def __iter__(self) -> DictionaryIterator:
        return DictionaryIterator(self)
