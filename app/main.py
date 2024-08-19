from typing import Hashable, Any

DEFAULT_CAPACITY = 8


class Node:
    def __init__(self, key: Hashable, value: Any) -> None:
        self.key = key
        self.value = value


class Dictionary:
    def __init__(self) -> None:
        self.capacity = DEFAULT_CAPACITY
        self.hash_table = [None] * self.capacity
        self.number_of_elements = 0

    def __len__(self) -> int:
        return self.number_of_elements

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.number_of_elements >= self.capacity * 0.75:
            self.resize()

        hash_key = hash(key)
        index_to_past = self.find_available_case(key, hash_key)

        while (
                self.hash_table[index_to_past] is not None
                and key != self.hash_table[index_to_past].key
        ):
            index_to_past = self.increment_index(index_to_past)

        if self.hash_table[index_to_past] is None:
            self.number_of_elements += 1

        self.hash_table[index_to_past] = Node(key, value)

    def __getitem__(self, key: Hashable) -> Any:
        hash_key = hash(key)
        index_to_search = self.find_available_case(key, hash_key)

        while (
                self.hash_table[index_to_search] is not None
                and key != self.hash_table[index_to_search].key
        ):
            index_to_search = self.increment_index(index_to_search)

        if self.hash_table[index_to_search] is not None:
            return self.hash_table[index_to_search].value
        else:
            raise KeyError(f"Key {key} not found")

    def resize(self) -> None:
        old_cases = self.hash_table
        self.capacity *= 2
        self.hash_table = [None] * self.capacity
        self.number_of_elements = 0

        for node in old_cases:
            if node:
                self[node.key] = node.value

    def find_available_case(self, key: Hashable, hash_key: int) -> int:
        index_available_case = self.get_index_by_hash(hash_key)
        while (
                self.hash_table[index_available_case] is not None
                and key != self.hash_table[index_available_case].key
        ):
            index_available_case = self.increment_index(index_available_case)
        return index_available_case

    def get_index_by_hash(self, hash_key: int) -> int:
        return hash_key % self.capacity

    def increment_index(self, index: int) -> int:
        return (index + 1) % self.capacity
