from dataclasses import dataclass, field
from typing import Any
from app.point import Point


@dataclass
class Node:
    key: Any
    hash_val: int
    value: Any


@dataclass
class Dictionary:
    initial_capacity = 8
    load_factor = 2 / 3
    size = 0
    hash_table: list[list[Node]] = field(init=False)

    def __post_init__(self) -> None:
        self.hash_table = [None] * self.initial_capacity

    def line_stop(self) -> int:
        return int(self.initial_capacity * self.load_factor)

    def __len__(self) -> int:
        return self.size

    def __setitem__(self, key: Any, value: Any) -> None:
        hash_val = hash(key)
        index = hash_val % self.initial_capacity
        if self.hash_table[index] is None:
            self.hash_table[index] = [Node(key, hash_val, value)]

        else:
            for node in self.hash_table[index]:
                if node.hash_val == hash_val and node.key == key:
                    node.value = value
                    return
        self.hash_table[index].append(Node(key, hash_val, value))
        self.size += 1

        if self.size >= self.line_stop():
            self.resize()

    def __getitem__(self, key: Any) -> Any:
        hash_val = hash(key)
        index = hash_val % self.initial_capacity
        if self.hash_table[index] is not None:
            for node in self.hash_table[index]:
                if node.hash_val == hash_val and node.key == key:
                    return node.value
        raise KeyError(f"Key not found: {key}")

    def resize(self) -> None:
        new_capacity = self.initial_capacity * 2  # new_capacity = 16
        new_hash_table = [None] * new_capacity

        for i in range(self.initial_capacity):
            if self.hash_table[i]:
                for node in self.hash_table[i]:
                    if node is not None:
                        new_index = node.hash_val % new_capacity
                        if new_hash_table[new_index] is None:
                            new_hash_table[new_index] = [node]
                        else:
                            new_hash_table[new_index].append(node)

        self.hash_table = new_hash_table
        self.initial_capacity = new_capacity


if __name__ == "__main__":
    my_dict = Dictionary()
    point1 = Point(1.0, 2.0)
    point2 = Point(3.0, 4.0)

    my_dict[point1] = "value1"
    my_dict[point2] = "value2"

    print(my_dict[point1])
    print(my_dict[point2])
