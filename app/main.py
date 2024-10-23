# from typing import Any
#
#
# class Dictionary:
#     def __init__(self):
#         self.length: int = 0 # default 0
#         self.capacity: int = 8 # default 8
#         self.hash_table: list[tuple | None] = [None] * self.capacity
#
#     def get_key_value(self, key):
#         # if key.__hash__ is None or self.length <= 0:
#         #     return False
#
#         index = hash(key) % self.capacity
#
#         # if collision
#
#         result = self.hash_table[index]
#
#         return result[2]
#
#     def set_key_value(self, key: Any, value: Any):
#         # if key.__hash__ is None:
#         #     return False
#
#         self._check_extend_memory()
#
#         node = (key, hash(key), value)
#         index = node[1] % self.capacity
#
#         index = self._collision(index)
#
#         self.hash_table[index] = node
#         self.length += 1
#
#     def __getitem__(self, key):
#         # if key.__hash__ is None or self.length <= 0:
#         #     return False
#
#         index = hash(key) % self.capacity
#         original_index = index
#
#         while self.hash_table[index] is not None:
#             if self.hash_table[index][0] == key:
#                 return self.hash_table[index][2]
#             index = (index + 1) % self.capacity
#
#             # Если вернулись к начальному индексу, значит ключа нет
#             if index == original_index:
#                 break
#
#         # if collision
#
#         result = self.hash_table[index]
#
#         if key == result[0]:
#             return result[2]
#         else:
#             index += 1
#
#     def __setitem__(self, key: Any, value: Any):
#         # if key.__hash__ is None:
#         #     return False
#
#         self._check_extend_memory()
#
#         node = (key, hash(key), value)
#         index = node[1] % self.capacity
#
#         index = self._collision(index)
#
#         self.hash_table[index] = node
#         self.length += 1
#
#     def __len__(self):
#         return self.length
#
#     def my_len(self):
#         return self.length
#
#     def _index(self):
#         pass
#
#     def _collision(self, index) -> int:
#         # check index is free
#         # return index free cell
#
#         count = index
#         while True:
#             if self.hash_table[count] is not None:
#                  count += 1
#
#             if count == self.capacity:
#                 count = 0
#
#             if self.hash_table[count] is None:
#                  return count
#
#
#     def _re_sort_memory(self):
#         pass
#
#     def _check_extend_memory(self):
#         if self.length > (2 / 3) * self.capacity:
#             self.hash_table += ([None] * 8)
#             self.capacity *= 2




# print((2 / 3 ) * 8)

# my_dict = Dictionary()
# print(my_dict.__dict__)

# my_dict.set_key_value(0, 5)
# my_dict.set_key_value(1, 5)
# my_dict.set_key_value(6, 5)

# my_dict.set_key_value(7, 7)
# my_dict.set_key_value(8, 7)
# my_dict.set_key_value(9, 7)

# my_dict.set_key_value(1, 8)
# my_dict.set_key_value(1, 8)
# my_dict.set_key_value(1, 8)
# my_dict.set_key_value(1, 8)
# my_dict.set_key_value(1, 8)
# my_dict.set_key_value(1, 9)

# my_dict.set_key_value(1, 10)

# print(my_dict.__dict__)

# print("length: ", my_dict.my_len())
# print(my_dict.hash_table)

# print(my_dict.get_key_value(1))
# print(my_dict.__dict__)
# print("length: ", my_dict.my_len())


# working
# print("-"*30)
# my_dict = Dictionary()
# my_dict.set_key_value(1, 5)
# print("length: ", my_dict.my_len())
# print(my_dict.hash_table)
# print(my_dict.get_key_value(1))
# print("length: ", my_dict.my_len())

# print("-"*30)
# my_dict.set_key_value("greetings", "Hello World!")
# print("length: ", my_dict.my_len())
# print(my_dict.hash_table)
# print(my_dict.get_key_value("greetings"))
# print(my_dict.hash_table)
# print("length: ", my_dict.my_len())

#-----------------------------------------------------
# print(1 % 8)
# print(dir(1))
# print([1, 2, 3].__hash__)


from typing import Any, Optional


class Dictionary:
    def __init__(self):
        self.length: int = 0
        self.capacity: int = 8
        self.hash_table: list[Optional[tuple]] = [None] * self.capacity

    def get_key_value(self, key: Any) -> Optional[Any]:
        index = hash(key) % self.capacity
        original_index = index

        while self.hash_table[index] is not None:
            if self.hash_table[index][0] == key:
                return self.hash_table[index][2]
            index = (index + 1) % self.capacity

            if index == original_index:
                break

        return None

    def set_key_value(self, key: Any, value: Any):
        self._check_extend_memory()

        index = hash(key) % self.capacity
        original_index = index

        while self.hash_table[index] is not None:
            if self.hash_table[index][0] == key:
                self.hash_table[index] = (key, hash(key), value)
                return
            index = (index + 1) % self.capacity

            if index == original_index:
                break

        self.hash_table[index] = (key, hash(key), value)
        self.length += 1

    def __getitem__(self, key: Any) -> Any:
        value = self.get_key_value(key)
        if value is None:
            raise KeyError
        return value

    def __setitem__(self, key: Any, value: Any):
        self.set_key_value(key, value)

    def __len__(self):
        return self.length

    def my_len(self) -> int:
        return self.length

    def _check_extend_memory(self):
        if self.length >= (2 / 3) * self.capacity:
            old_table = self.hash_table
            self.capacity *= 2
            self.hash_table = [None] * self.capacity
            self.length = 0

            for entry in old_table:
                if entry is not None:
                    self.set_key_value(entry[0], entry[2])
