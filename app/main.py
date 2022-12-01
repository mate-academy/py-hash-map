from typing import Any


class Dictionary:

    def __init__(self) -> None:
        self.my_dict = []

    def __setitem__(self, key: Any, item: Any) -> None:
        for i, v in enumerate(self.my_dict):
            if key == v[0]:
                del self.my_dict[i]
                break
        self.my_dict.append((key, hash(key), item))

    def __getitem__(self, key: Any) -> dict:
        for obj in self.my_dict:
            if obj[0] == key:
                return obj[2]
        raise KeyError

    def __len__(self) -> int:
        return len(self.my_dict)
