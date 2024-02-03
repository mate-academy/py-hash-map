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
        hash_of_key = hash(key)
        index_to_insert = self._find_available_cell(key, hash_of_key)

        if self._hash_table[index_to_insert] is None:
            self._length += 1
            self._resize()

        self._hash_table[index_to_insert] = (key, hash_of_key, value)

    def __getitem__(self, key: Hashable) -> Any:
        hash_of_key = hash(key)
        index = self._get_index_by_hash(hash_of_key)

        for _ in range(self._capacity):
            if (self._hash_table[index] is not None
                    and key == self._hash_table[index][0]):
                return self._hash_table[index][2]

            index = self._increment_index(index)

        raise KeyError(f"{key} not exist!")

    def _resize(self) -> None:
        threshold = int(self._capacity * 2 / 3)
        if self._length >= threshold:
            old_hash_table = [cell
                              for cell in self._hash_table
                              if cell is not None]
            self._capacity *= 2
            self._hash_table = [None] * self._capacity
            for key, hash_of_key, value in old_hash_table:
                index_to_insert = self._find_available_cell(key, hash_of_key)
                self._hash_table[index_to_insert] = (key, hash_of_key, value)

    def _find_available_cell(self, key: Hashable, hash_of_key: int) -> int:
        available_cell_index = self._get_index_by_hash(hash_of_key)

        while self._is_cell_irrelevant_to_write_key(available_cell_index, key):
            available_cell_index = self._increment_index(available_cell_index)

        return available_cell_index

    def _get_index_by_hash(self, hash_of_key: int) -> int:
        return hash_of_key % self._capacity

    def _increment_index(self, index: int) -> int:
        return (index + 1) % self._capacity

    def _is_cell_irrelevant_to_write_key(self,
                                         index: int,
                                         key: Hashable) -> bool:
        return (
            self._hash_table[index] is not None
            and key != self._hash_table[index][0]
        )
