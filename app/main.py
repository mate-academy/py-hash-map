from typing import Hashable, Any


class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.table = [[] for _ in range(self.capacity)]
        self.size = 0
        self.load_factor = 0.67

    def __len__(self) -> int:
        return self.size

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.size >= len(self.table) * self.load_factor:
            self.resize()
        index = hash(key) % len(self.table)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                break
        else:
            bucket.append((key, value))
            self.size += 1

    def __getitem__(self, key: Hashable) -> Any:
        index = hash(key) % len(self.table)
        bucket = self.table[index]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(key)

    def resize(self) -> None:
        new_capacity = self.capacity * 2
        new_table = [[] for _ in range(new_capacity)]
        for bucket in self.table:
            for k, v in bucket:
                index = hash(k) % new_capacity
                new_table[index].append((k, v))
        self.table = new_table
        self.capacity = new_capacity

    def clear(self) -> None:
        self.table = [[] for _ in range(self.capacity)]
        self.size = 0

    def __delitem__(self, key: Hashable) -> None:
        index = hash(key) % len(self.table)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
            else:
                raise KeyError(key)

    def pop(self, key: Hashable, default: Any = None) -> Any:
        index = hash(key) % len(self.table)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return v
        if default:
            return default
        raise KeyError(key)

    def update(self, other: dict) -> None:
        if not isinstance(other, dict):
            print("Data for update must be dictionary!")
        for k, v in other.items():
            self[k] = v

    def __iter__(self) -> iter:
        for bucket in self.table:
            for k, v in bucket:
                yield k
