from typing import Hashable, Any
#import Staticmothod


class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.capacity = 8
        self.load_factor = 0.66
        self.hash_table: list = [None] * self.capacity

    def __setitem__(self, key: Hashable, value: Any) -> None:
        new_node = (hash(key), key, value)
        self.length += 1
        if self.capacity * self.load_factor >= self.length:
            self.__resize()
        index = self.find_empty_cell(new_node)
        self.hash_table[index] = new_node


    def __resize(self) -> None:
        new_hash_table: list = [None] * self.capacity
        pass

    def __len__(self) -> int:
        return self.length

    def find_empty_cell(self, node: tuple) -> int:
        index = node[0] % self.capacity
        while True:
            if index == self.capacity:
                index = 0
            if self.hash_table[index] is None:
                return index
            index += 1




    # @staticmethod
    # def __get_key_hash(self, key: Hashable) -> Any:
    #     return hash(key)

