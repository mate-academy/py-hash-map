from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.hash_table: list = [None] * 8

    def __len__(self) -> int:
        return self.length

    def table_resize(self) -> None:
        cache_table = self.hash_table
        self.length = 0
        self.hash_table = list([None] * len(self.hash_table) * 2)
        for element in cache_table:
            if element is not None:
                self.__setitem__(element[0], element[1])

    def __setitem__(self, key: Any, value: Any) -> None:
        index_hash_table = hash(key) % len(self.hash_table)
        if self.hash_table[index_hash_table] is None:
            self.hash_table[index_hash_table] = (key, value, hash(key))
            self.length += 1
        elif self.hash_table[index_hash_table][0] == key:
            self.hash_table[index_hash_table] = (key, value, hash(key))
        else:
            i = 0
            while True:
                i += 1
                if self.hash_table[
                    (index_hash_table + i)
                    % len(self.hash_table)
                ] is None:
                    self.hash_table[
                        (index_hash_table + i)
                        % len(self.hash_table)
                    ] = (key, value, hash(key))
                    self.length += 1
                    break
                elif self.hash_table[
                    (index_hash_table + i)
                    % len(self.hash_table)
                ][0] == key:
                    self.hash_table[
                        (index_hash_table + i)
                        % len(self.hash_table)
                    ] = (key, value, hash(key))
                    break
        if self.length > (len(self.hash_table) / 3 * 2):
            self.table_resize()

    def __getitem__(self, key: Any) -> Any:
        index_hash_table = hash(key) % len(self.hash_table)
        if self.hash_table[index_hash_table] is None:
            raise KeyError
        elif self.hash_table[index_hash_table][0] == key:
            return self.hash_table[index_hash_table][1]
        else:
            for i in range(1, len(self.hash_table)):
                if self.hash_table[
                    (index_hash_table + i)
                    % len(self.hash_table)
                ][0] == key:
                    return self.hash_table[
                        (index_hash_table + i)
                        % len(self.hash_table)
                    ][1]
