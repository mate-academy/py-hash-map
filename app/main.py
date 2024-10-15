from typing import Any

INC_SIZE_TWICE = 2


class Dictionary:
    size = 8

    def __init__(self) -> None:
        self.capacity = 0
        self.hash_table = [None] * Dictionary.size

    def __setitem__(self, key, value):
        if isinstance(key, (list, dict, set)):
            raise KeyError("key must be hashable")
        hash_key = hash(key)
        index = hash_key % Dictionary.size

        # rewrite value
        for item in self.hash_table:
            if item and item.hash == hash_key:
                item.value = value
                return

        # recount dict size
        if self.capacity >= Dictionary.size * 2 // 3:
            self.resize_dict()

        # check collision
        index = self.check_collision(self.hash_table, index)
        self.hash_table[index] = Node(hash_key, key, value)
        self.capacity += 1
        # print(self.hash_table)

    def __getitem__(self, key_item):
        if isinstance(key_item, (list, dict, set)):
            raise KeyError("key must be hashable")
        hash_key = hash(key_item)
        for item in self.hash_table:
            if item and item.hash == hash_key:
                return item.value
        raise KeyError("key not in dict")

    def __len__(self):
        return self.capacity

    def check_collision(self, list_, index):
        while True:
            if list_[index] is not None:
                index += 1
                if index >= (Dictionary.size - 1):
                    index = 0
            else:
                break
        return index

    def resize_dict(self):
        Dictionary.size *= INC_SIZE_TWICE
        new_hash_table = [None] * Dictionary.size
        for ind in self.hash_table:
            if ind:
                index = hash(ind.key) % Dictionary.size
                index = self.check_collision(new_hash_table, index)
                new_hash_table[index] = ind
        self.hash_table = new_hash_table


class Node:
    def __init__(self, hash_: int, key: Any, value: Any):
        self.hash = hash_
        self.key = key
        self.value = value


if __name__ == "__main__":
    # abc = Dictionary()
    # abc["one"] = 1
    # abc["b"] = "two"
    # abc["c"] = 3
    # abc["d"] = 4
    # abc["e"] = 5
    # abc["one"] = 5
    # abc["f"] = 6
    # abc["g"] = 7
    # abc["h"] = 8
    # abc["i"] = 9
    # abc["j"] = 10
    # abc["k"] = 11
    # abc["l"] = 12
    # abc["m"] = 13
    # print(len(abc))
    # print(len(abc.hash_table))
    # print(hash(3))

    items = [(1, "one"), (2, "two"), (3, "tree"), (4, "four")]
    dictionary = Dictionary()
    for key, value in items:
        dictionary[key] = value

    print("dict[1]:", dictionary[1])
    print("dict[2]:", dictionary[2])
    print("dict[3]:", dictionary[3])
    print("dict[4]:", dictionary[4])

    expected_pairs = [(1, "one"), (2, "two"), (3, "tree"), (4, "four")]
    for key, value in expected_pairs:
        print(f"value from key: ({dictionary[key]}) == value: ({value})")
