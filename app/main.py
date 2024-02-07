from typing import Any, Hashable

DEFAULT_CAPACITY = 8


class Dictionary:

    def __init__(self) -> None:
        self._capacity = DEFAULT_CAPACITY
        self._hash_table = [None] * self._capacity
        self._length = 0

    def __len__(self) -> int:
        return self._length

    def __setitem__(self, key: Hashable, value: Any) -> None:
        key_hash = hash(key)
        index_insert = self._find_available_cell(key, key_hash)
        threshold = int(self._capacity * 2 / 3)

        if self._hash_table[index_insert] is None:
            self._length += 1
            if self._length >= threshold:
                self._resize()

        self._hash_table[index_insert] = (key, key_hash, value)

    def __getitem__(self, key: Hashable) -> Any:
        key_hash = hash(key)
        index = self._get_index_by_hash(key_hash)

        for _ in range(self._capacity):
            if (self._hash_table[index] is not None
                    and key == self._hash_table[index][0]):
                return self._hash_table[index][2]

            index = self._increment_index(index)

        raise KeyError(f"{key} not exist!")

    def _resize(self) -> None:

        old_hash_table = list(filter(None, self._hash_table))
        self._capacity *= 2
        self._hash_table = [None] * self._capacity
        for key, key_hash, value in old_hash_table:
            index_insert = self._find_available_cell(key, key_hash)
            self._hash_table.__setitem__(index_insert, (key, key_hash, value))

    def _find_available_cell(self, key: Hashable, key_hash: int) -> int:
        available_cell_index = self._get_index_by_hash(key_hash)

        while self._is_cell_irrelevant_to_write_key(available_cell_index, key):
            available_cell_index = self._increment_index(available_cell_index)

        return available_cell_index

    def _get_index_by_hash(self, key_hash: int) -> int:
        return key_hash % self._capacity

    def _increment_index(self, index: int) -> int:
        return (index + 1) % self._capacity

    def _is_cell_irrelevant_to_write_key(self,
                                         index: int,
                                         key: Hashable) -> bool:
        return (
            self._hash_table[index] is not None
            and key != self._hash_table[index][0]
        )
