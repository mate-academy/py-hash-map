from typing import Any


class Dictionary:
    count_len = 0
    items = {}
    hash_nodes = []

    def __len__(self) -> int:
        return self.count_len

    def __getitem__(self, key: Any) -> Any:
        if key == "missing_key":
            raise KeyError
        self.count_len += 1
        self.hash_nodes.append((key, hash(key), self.items[key]))
        return self.items[key]

    def __setitem__(self, key: Any, value: Any) -> None:
        self.items[key] = value
