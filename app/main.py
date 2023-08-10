import dataclasses

from typing import Any, Hashable, Optional, List


@dataclasses.dataclass
class Dictionary:
    capacity: int = 8
    load_factor: float = 0.75
    hash_table_:  Optional[list[list[str]]] = None

    size: int = 0

    def hash_table(self) -> None:
        self.hash_table_ = [None] * self.capacity

    def hash(self, key: Hashable) -> int:
        return hash(key) % self.capacity

    def __len__(self) -> int:
        return self.size

    def __getitem__(self, key: Hashable) -> None:
        if self.hash_table_ is None:
            self.hash_table()
        index = self.hash(key)
        initial_index = index
        while self.hash_table_[index] is not None:
            if self.hash_table_[index][0] == key:
                return self.hash_table_[index][2]
            index = (index + 1) % self.capacity
            if index == initial_index:
                raise KeyError(key)
        raise KeyError(key)

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.hash_table_ is None:
            self.hash_table()
        index = self.hash(key)
        initial_index = index
        while self.hash_table_[index] is not None:
            if self.hash_table_[index][0] == key:
                self.hash_table_[index] = (key, hash(key), value)
                return
            index = (index + 1) % self.capacity
            if index == initial_index:
                raise KeyError(key)
        self.hash_table_[index] = (key, hash(key), value)
        self.size += 1

        if self.size >= self.capacity * self.load_factor:
            self.resize()

    def resize(self) -> None:
        old_hash_table = self.hash_table_
        self.capacity *= 2
        self.hash_table()
        for node in old_hash_table:
            if node:
                self.reinsert(node)

    def reinsert(self, node: tuple) -> None:
        key, _, value = node
        index = self.hash(key)
        while self.hash_table_[index] is not None:
            index = (index + 1) % self.capacity
        self.hash_table_[index] = (key, hash(key), value)

    def clear(self) -> None:
        self.hash_table()
        self.size = 0


movies = Dictionary()

movies[1] = "Oppenheimer"
movies[2] = "Inception"
movies[3] = "Interstellar"
movies[4] = "Tenet"
movies[5] = "The Prestige"
print(f"Size: {movies.size}, Capacity: {movies.capacity}")
movies[6] = "The Dark Knight"
print(f"Size: {movies.size}, Capacity: {movies.capacity}")
print(movies.hash_table_)
movies[7] = "Gladiator"
print(movies.hash_table_)
movies[8] = "Shutter Island"
print(movies.hash_table_)
movies[9] = "Blade Runner 2049"
movies[10] = "Matrix"
print(f"Size: {movies.size}, Capacity: {movies.capacity}")

movies.clear()
print(len(movies))

movies.__setitem__(2, "Memento")
print(len(movies))

print(movies.__getitem__(2))
movies.__setitem__(3, "Tenet")
print(movies.__getitem__(3))
print(len(movies))
