from typing import Any, Hashable


class Node:
    def __init__(self, key: Hashable, value: Any) -> None:
        pass


class Dictionary:
    def __init__(self, capacity: int = 8) -> None:
        pass

    def get_index(self, key: Hashable) -> int:
        pass

    def __setitem__(self, key: Hashable, value: Any) -> None:
        pass

    def __getitem__(self, key: Hashable) -> Any:
        index = self.get_index(key)
        if self.hash_table[index] and self.hash_table[index].key == key:
            return self.hash_table[index].value
        else:
            raise KeyError

    def resize(self) -> None:
        pass

    def __len__(self) -> int:
        pass

    def __iter__(self) -> object:
        pass

    def __next__(self) -> Any:
        pass

    def update(self, dictionary: Dictionary) -> None:
        pass

    def get(self) -> None:
        pass

    def pop(self) -> None:
        pass

    def __delitem__(self) -> None:
        pass

    def clear(self) -> object:
        pass
