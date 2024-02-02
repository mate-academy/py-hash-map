from typing import Any, Hashable


class Dictionary:
    def __init__(self, capacity: int = 8) -> None:
        self.capacity = capacity
        self.dict_size = 0
        self._hash_table = [None] * self.capacity

    def __hash_index__(self, key_hash: int) -> None:
        return key_hash % self.capacity

    def __resize__(self) -> None:
        old_table = self._hash_table
        self.capacity *= 2
        self._hash_table = [None] * self.capacity
        self.dict_size = 0

        for item in old_table:
            if item:
                for key, key_hash, value in item:
                    self.__setitem__(key, value)

    def __setitem__(self, key: Hashable, value: Any) -> None:
        key_hash = hash(key)
        index = self.__hash_index__(key_hash)

        if not self._hash_table[index]:
            self._hash_table[index] = []

        found = False
        for item in self._hash_table[index]:
            if item[0] == key:
                self._hash_table[index][
                    self._hash_table[index].index(item)
                ] = (key, key_hash, value)
                found = True
                break
        if not found:
            self._hash_table[index].append((key, key_hash, value))
            self.dict_size += 1

        if self.dict_size / self.capacity > 0.75:
            self.__resize__()

    def __getitem__(self, key: Hashable) -> None:
        key_hash = hash(key)
        index = self.__hash_index__(key_hash)
        if self._hash_table[index] is None:
            raise KeyError(key)

        for k, kh, v in self._hash_table[index]:
            if k == key:
                return v

        raise KeyError(key)

    def __len__(self) -> None:
        return self.dict_size

    def clear(self) -> None:
        self._hash_table = [None] * self.capacity
        self.dict_size = 0

    def __delitem__(self, key: Hashable) -> None:
        key_hash = hash(key)
        index = self.__hash_index__(key_hash)

        if self.table[index] is None:
            raise KeyError(key)

        for i, (k, kh, v) in enumerate(self._hash_table[index]):
            if k == key:
                del self._hash_table[index][i]
                self.dict_size -= 1
                return

        raise KeyError(key)

    def get(self, key: Hashable, default: Any = None) -> None:
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    def pop(self, key: Hashable, default: Any = None) -> None:
        key_hash = hash(key)
        index = self.__hash_index__(key_hash)

        if self._hash_table[index] is None:
            if default is not None:
                return default
            else:
                raise KeyError(key)

        for i, (k, kh, v) in enumerate(self._hash_table[index]):
            if k == key:
                self.dict_size -= 1
                return self._hash_table[index].pop(i)[2]

        if default is not None:
            return default
        else:
            raise KeyError(key)

    def update(self, *args, **kwargs) -> None:
        for key, value in dict(*args, **kwargs).items():
            self.__setitem__(key, value)

    def __iter__(self) -> None:
        for bucket in self._hash_table:
            if bucket:
                for key, _, _ in bucket:
                    yield key
