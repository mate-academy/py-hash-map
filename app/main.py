from typing import Any

INC_SIZE_TWICE = 2


class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.hash_table = [None] * 8

    def __setitem__(self, key, value):

        hash_key = hash(key)
        index = hash_key % len(self.hash_table)
        if self.hash_table[index] and self.hash_table[index].key == key:
            self.hash_table[index].value = value
            return
        if self.length >= len(self.hash_table) * 2 // 3:
            self.resize()

        index = self.check_collisions(self.hash_table, index)
        self.hash_table[index] = Node(hash_key, key, value)
        self.length += 1
        # print(self.hash_table)

    def __getitem__(self, item):
        index = hash(item) % len(self.hash_table)
        if self.hash_table[index]:
            return self.hash_table[index].value
        # return None

    def __len__(self):
        return self.length

    def check_collisions(self, list_, index, increase=1):
        while True:
            if list_[index] is not None:
                index += 1
                if index >= (len(self.hash_table) - 1) * increase:
                    index = 0
            else:
                break
        return index

    def resize(self):
        new_hash_table = [None] * len(self.hash_table) * INC_SIZE_TWICE
        for ind in range(len(self.hash_table)):
            if self.hash_table[ind] is not None:

                index = hash(self.hash_table[ind]) % len(new_hash_table)

                index = self.check_collisions(new_hash_table, index, INC_SIZE_TWICE)
                new_hash_table[index] = self.hash_table[ind]
        self.hash_table = new_hash_table


class Node:
    def __init__(self, hash_: int, key: Any, value: Any):
        self.hash = hash_
        self.key = key
        self.value = value


if __name__ == "__main__":
    abc = Dictionary()
    abc["one"] = 1
    abc["b"] = "two"
    abc["c"] = 3
    abc["d"] = 4
    abc["e"] = 5
    # abc["one"] = 5
    abc["f"] = 6
    abc["g"] = 7
    abc["h"] = 8
    abc["i"] = 9
    abc["j"] = 10
    # abc["k"] = 11
    # abc["l"] = 12
    # abc["m"] = 13
    print(len(abc))
    print(len(abc.hash_table))
