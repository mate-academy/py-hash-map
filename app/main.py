from typing import Any


class Dictionary:
    def __init__(self, capacity: int = 64) -> None:
        self.capacity = capacity
        self.container = [[] for i in range(capacity)]

    def __setitem__(self, key: Any, value: Any) -> None:
        key_hash = hash(key) % self.capacity
        room = self.container[key_hash]
        for pair in room:
            if pair[0] == key:
                pair[1] = value
                return
        room.append([key, value])

    def __getitem__(self, key: Any) -> Any:
        key_hash = hash(key) % self.capacity
        room = self.container[key_hash]
        for pair in room:
            if pair[0] == key:
                return pair[1]
        raise KeyError(key)

    def __len__(self) -> int:
        return sum(len(room) for room in self.container)

    def clear(self) -> None:
        for room in self.container:
            room.clear()

    def __delitem__(self, key: Any) -> None:
        key_hash = hash(key) % self.capacity
        room = self.container[key_hash]
        for pair_number, pair in enumerate(room):
            if pair[0] == key:
                del room[pair_number]
                return
        raise KeyError(key)

    def get(self, key: Any, default: Any = None) -> Any:
        key_hash = hash(key) % self.capacity
        room = self.container[key_hash]
        for pair in room:
            if pair[0] == key:
                return pair[1]
        return default

    def pop(self, key: Any) -> Any:
        key_hash = hash(key) % self.capacity
        room = self.container[key_hash]
        for pair_number, pair in enumerate(room):
            if pair[0] == key:
                value = pair[1]
                del room[pair_number]
                return value
        raise KeyError(key)

    def update(self, other: dict) -> None:
        for key in other:
            self[key] = other[key]

    def __iter__(self) -> None:
        keys = []
        for room in self.container:
            for pair in room:
                keys.append(pair[0])
        return iter(keys)
