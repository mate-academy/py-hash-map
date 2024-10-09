from typing import Any, List, Tuple, Hashable


class Dictionary:
    def __init__(self) -> None:
        self.my_dict = []

    def __setitem__(self, key: Hashable, value: Any) -> None:
        key_hash = self._hash(key)

        for i, (k, v) in enumerate(self.my_dict):
            if k == key_hash and key == v[0]:
                self.my_dict[i] = (key_hash, (key, value))
                return
        self.my_dict.append((key_hash, (key, value)))

    def __getitem__(self, key: Hashable) -> Any:
        key_hash = self._hash(key)

        for k, v in self.my_dict:
            if k == key_hash and key == v[0]:
                return v[1]

        raise KeyError(f"Key '{key}' not found")

    def __len__(self) -> int:
        return len(self.my_dict)

    def __delitem__(self, key: Hashable) -> None:
        key_hash = self._hash(key)
        for i, (h, (k, v)) in enumerate(self.my_dict):
            if h == key_hash and k == key:
                del self.my_dict[i]
                return

        raise KeyError(f"Key '{key}' not found")

    def __contains__(self, key: Hashable) -> bool:
        key_hash = self._hash(key)
        return any(h == key_hash and k == key for h, (k, v) in self.my_dict)

    def items(self) -> List[Tuple[Any, Any]]:
        return [(k, v) for _, (k, v) in self.my_dict]

    def keys(self) -> List[Any]:
        return [k for _, (k, v) in self.my_dict]

    def values(self) -> List[Any]:
        return [v for _, (k, v) in self.my_dict]

    def _hash(self, key: Hashable) -> int:
        if isinstance(key, (list, dict)):
            raise TypeError("Unhashable type: 'list' or 'dict'")
        return hash(key)

    def clear(self) -> None:
        self.my_dict.clear()

    def get(self, key: Hashable, default: Any = None) -> Any:
        key_hash = self._hash(key)
        for k, v in self.my_dict:
            if k == key_hash and key == v[0]:
                return v[1]
        return default

    def pop(self, key: Hashable, default: Any = None) -> Any:
        key_hash = self._hash(key)
        for i, (h, (k, v)) in enumerate(self.my_dict):
            if h == key_hash and k == key:
                del self.my_dict[i]
                return v
        if default is None:
            return default

        raise KeyError(f"Key '{key}' not found")

    def update(self, other: dict) -> None:
        for key, value in other.items():
            self[key] = value

    def __iter__(self) -> iter:
        return iter(self.keys())
