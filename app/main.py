from typing import Any

INC_SIZE_TWICE = 2


class Dictionary:
    size = 8

    def __init__(self) -> None:
        self.capacity = 0
        self.hash_table = [None] * Dictionary.size

    def __setitem__(self, key: Any, value: Any) -> None:
        if isinstance(key, (list, dict, set)):
            raise KeyError("key must be hashable")
        hash_key = hash(key)

        # rewrite value, if we have the same key
        for item in self.hash_table:
            if item and item.hash == hash_key and item.key == key:
                item.value = value
                return

        # recount dict size, if too load
        if self.capacity >= Dictionary.size * 2 // 3:
            self.resize_dict()

        # check collision
        index = hash_key % Dictionary.size
        index = self.check_collision(index)
        self.hash_table[index] = Node(hash_key, key, value)
        self.capacity += 1

    def __getitem__(self, key_item: Any) -> Any:
        if isinstance(key_item, (list, dict, set)):
            raise KeyError("key must be hashable")
        hash_key = hash(key_item)
        for item in self.hash_table:
            if item and item.key == key_item and hash_key == item.hash:
                print(item.value)
                return item.value
        raise KeyError("key not in dict")

    def __len__(self) -> int:
        return self.capacity

    def check_collision(self, index: int) -> int:
        while True:
            if self.hash_table[index] is not None:
                index += 1
                if index >= (Dictionary.size - 1):
                    index = 0
            else:
                break
        return index

    def resize_dict(self) -> None:
        Dictionary.size *= INC_SIZE_TWICE
        new_hash_table = [None] * Dictionary.size
        for ind in self.hash_table:
            if ind:
                index = hash(ind.key) % Dictionary.size
                index = self.check_collision(new_hash_table, index)
                new_hash_table[index] = ind
        self.hash_table = new_hash_table


class Node:
    def __init__(self, hash_: int, key: Any, value: Any) -> None:
        self.hash = hash_
        self.key = key
        self.value = value
