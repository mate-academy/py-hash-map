from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.load_factor = 2 / 3
        self.current_load = 0
        self.hash_table = [None] * self.capacity

    def __setitem__(self, key: Any, value: Any) -> None:
        node = (key, hash(key), value)
        if self.check_existing_key(node):
            return

        self.current_load += 1

        self.check_for_resizing()

        index = hash(key) % self.capacity
        index = self.find_empty_node(self.hash_table, index)
        self.hash_table[index] = node

    def __getitem__(self, key: Any) -> Any:
        index = hash(key) % self.capacity
        if not self.hash_table[index]:
            raise KeyError
        while self.hash_table[index][0] != key:
            index += 1
            if index >= self.capacity:
                index = 0
        return self.hash_table[index][2]

    def __len__(self) -> int:
        return self.current_load

    def check_existing_key(self, node: tuple) -> bool:
        index = node[1] % self.capacity
        for i in range(index, len(self.hash_table)):
            if self.hash_table[i] and self.hash_table[i][0] == node[0]:
                self.hash_table[i] = node
                return True
        return False

    def check_for_resizing(self) -> None:
        if self.current_load >= self.capacity * self.load_factor:
            self.capacity *= 2
            new_hash_table = [None] * self.capacity
            for exist_node in [node for node in self.hash_table
                               if node is not None]:
                index = exist_node[1] % self.capacity
                index = self.find_empty_node(new_hash_table, index)
                new_hash_table[index] = exist_node
            self.hash_table = new_hash_table

    def find_empty_node(self, hash_table: list, index: int) -> int:
        while hash_table[index] is not None:
            index += 1
            if index >= self.capacity:
                index = 0
        return index
