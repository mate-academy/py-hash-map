from typing import Any


class Dictionary:
    def __init__(self, elements: list[tuple[Any, Any]] = None) -> None:
        self.indices = [-1 for _ in range(8)]
        self.length = 0
        self.entries = []
        if elements is not None:
            self._assign_entries(elements)

    def _assign_entries(self, elements: list[tuple]) -> None:
        for key, value in elements:
            self.__setitem__(key, value)

    @staticmethod
    def _get_next_index(index: int, iterable: list[int]) -> int:
        return (index + 1) % len(iterable)

    @staticmethod
    def _get_index(key: Any, iterable: list[int]) -> int:
        return hash(key) % len(iterable)

    @staticmethod
    def _object_equal(
            input_key: Any,
            input_hash: int,
            entries_key: Any,
            entries_hash_: int
    ) -> bool:
        return input_key == entries_key and entries_hash_ == input_hash

    def _resize_indices(self) -> None:
        new_indices = [-1 for _ in range(len(self.indices) * 2)]
        index_in_entries = 0

        for entry in self.entries:
            index = self._get_index(entry[1], new_indices)

            while new_indices[index] != -1:
                index = self._get_next_index(index, new_indices)

            new_indices[index] = index_in_entries
            index_in_entries += 1
        self.indices = new_indices

    def __setitem__(self, input_key: Any, input_value: Any) -> None:
        if self.length / len(self.indices) > 0.7:
            self._resize_indices()

        input_hash = hash(input_key)
        index = self._get_index(input_key, self.indices)

        while self.indices[index] != -1:

            entries_hash, entries_key, entries_value = \
                self.entries[self.indices[index]]

            if self._object_equal(
                    input_key,
                    input_hash,
                    entries_key,
                    entries_hash
            ):
                self.entries[self.indices[index]][2] = input_value
                return
            else:
                index = (index + 1) % len(self.indices)

        self.indices[index] = self.length
        self.entries.append([input_hash, input_key, input_value])
        self.length += 1

    def __getitem__(self, input_key: Any) -> Any:

        input_hash = hash(input_key)
        index = self._get_index(input_key, self.indices)

        while self.indices[index] != -1:
            entries_hash, entries_key, entries_value = \
                self.entries[self.indices[index]]

            if self._object_equal(
                    input_key,
                    input_hash,
                    entries_key,
                    entries_hash
            ):
                return entries_value
            index = self._get_next_index(index, self.indices)
        raise KeyError

    def __len__(self) -> int:
        return self.length
