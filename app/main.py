import math
from collections.abc import Hashable
from typing import Any, Dict, Iterable, List, Tuple


class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.load_factor = 2 / 3
        self.threshold = math.floor(self.capacity * self.load_factor)
        self.hash_table = [None] * self.capacity
        self.length = 0

    def __len__(self) -> int:
        return self.length

    def _resize(self) -> None:
        self.capacity *= 2
        self.threshold = math.floor(self.capacity * self.load_factor)
        old_table = self.hash_table
        self.hash_table = [None] * self.capacity
        self.length = 0

        for bucket in old_table:
            if bucket is not None and bucket != "del":
                key, key_hash, value = bucket
                index = key_hash % self.capacity

                for _ in range(self.capacity):
                    target = self.hash_table[index]
                    if target is None:
                        self.hash_table[index] = bucket
                        self.length += 1
                        break
                    index = (index + 1) % self.capacity

    def __setitem__(self, key: Hashable, value: Any) -> None:
        key_hash = hash(key)
        index = key_hash % self.capacity

        if self.length >= self.threshold:
            target = self.hash_table[index]
            if target is None or target == "del":
                self._resize()
                index = key_hash % self.capacity
            elif target[0] != key:
                self._resize()
                index = key_hash % self.capacity

        while True:
            target = self.hash_table[index]
            if target is None or target == "del":
                self.hash_table[index] = [key, key_hash, value]
                self.length += 1
                break
            elif target[1] == key_hash and target[0] == key:
                self.hash_table[index][2] = value
                break
            index = (index + 1) % self.capacity

    def __getitem__(self, key: Any) -> Any:
        key_hash = hash(key)
        index = key_hash % self.capacity
        start_index = index

        while True:
            target = self.hash_table[index]
            if target is None:
                raise KeyError(f"Key {key} does not exist")
            if target != "del" and target[1] == key_hash and target[0] == key:
                return target[2]
            index = (index + 1) % self.capacity
            if start_index == index:
                raise KeyError(f"Key {key} does not exist")

    def clear(self) -> None:
        self.hash_table = [None] * self.capacity
        self.length = 0

    def __delitem__(self, key: Any) -> None:
        key_hash = hash(key)
        index = key_hash % self.capacity
        start_index = index

        while True:
            target = self.hash_table[index]
            if target is None:
                raise KeyError(f"Key {key} does not exist")
            if target != "del" and target[1] == key_hash and target[0] == key:
                self.hash_table[index] = "del"
                self.length -= 1
                break
            index = (index + 1) % self.capacity
            if start_index == index:
                raise KeyError(f"Key {key} does not exist")

    def get(self, key: Any, default: Any = None) -> Any:
        key_hash = hash(key)
        index = key_hash % self.capacity
        start_index = index

        while True:
            target = self.hash_table[index]
            if target is None:
                return default
            if target != "del" and target[1] == key_hash and target[0] == key:
                return target[2]
            index = (index + 1) % self.capacity
            if start_index == index:
                return default

    def pop(self, key: Any, default: Any = "raise") -> None:
        key_hash = hash(key)
        index = key_hash % self.capacity
        start_index = index

        while True:
            target = self.hash_table[index]
            if target is None:
                if default == "raise":
                    raise KeyError(f"Key {key} does not exist")
                return default
            if target != "del" and target[1] == key_hash and target[0] == key:
                value = target[2]
                self.hash_table[index] = "del"
                self.length -= 1
                return value
            index = (index + 1) % self.capacity
            if start_index == index:
                if default == "raise":
                    raise KeyError(f"Key {key} does not exist")
                return default

    def update(self, new_pairs: Iterable[Tuple] | Dict) -> None:
        if isinstance(new_pairs, dict):
            new_pairs = list(new_pairs.items())
        for pair in new_pairs:
            key, value = pair
            self.__setitem__(key, value)

    def __iter__(self) -> List:
        keys_list = []
        for bucket in self.hash_table:
            if bucket is not None and bucket != "del":
                keys_list.append(bucket[0])
        return keys_list
