from math import floor


class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.initial_capacity = 8
        self.load_factor = 2 / 3
        self.hash_table = [[] for _ in range(8)]
        self.resize = floor(self.load_factor * self.initial_capacity)

    def __len__(self) -> int:
        return self.length

    def __setitem__(self, key_set: any, value_set: any) -> None:
        key_hash = hash(key_set)
        index_in_hash_table = key_hash % self.initial_capacity
        if self.hash_table[index_in_hash_table]:
            if self.hash_table[index_in_hash_table][0] == key_set:
                self.hash_table[index_in_hash_table][2] = value_set
                return
            else:
                for element in self.hash_table:
                    if element and key_set == element[0]:
                        element[2] = value_set
                        return
        if self.__len__() == self.resize:
            self.__resize_hash_table()
            index_in_hash_table = key_hash % self.initial_capacity
        self.length += 1
        if self.hash_table[index_in_hash_table]:
            index_in_hash_table = self.solve_collision_problem(
                index_in_hash_table,
                self.hash_table
            )
        self.hash_table[index_in_hash_table] = [key_set, key_hash, value_set]

    def __getitem__(self, key_get: any) -> any:
        index_get = hash(key_get) % self.initial_capacity
        try:
            if self.hash_table[index_get][0] == key_get:
                return self.hash_table[index_get][2]
            else:
                for element in self.hash_table:
                    if element and key_get == element[0]:
                        return element[2]
        except IndexError:
            raise KeyError

    def __resize_hash_table(self) -> None:
        self.initial_capacity *= 2
        resized_hash_table = [[] for _ in range(self.initial_capacity)]
        for element in self.hash_table:
            if element:
                key_res, hash_res, value_res = element
                index_res_hash_table = hash_res % self.initial_capacity
                if resized_hash_table[index_res_hash_table]:
                    index_res_hash_table = self.solve_collision_problem(
                        index_res_hash_table,
                        resized_hash_table
                    )
                resized_hash_table[index_res_hash_table] = [
                    key_res,
                    hash_res,
                    value_res
                ]
        self.hash_table = resized_hash_table
        self.resize = floor(self.load_factor * self.initial_capacity)

    @staticmethod
    def solve_collision_problem(index_collision: int,
                                collision_hash_table: list[list]) -> int:
        if [] in collision_hash_table[index_collision + 1:]:
            return (collision_hash_table[index_collision + 1:].index([])
                    + index_collision
                    + 1)
        return collision_hash_table[:index_collision].index([])
