from typing import Any, Hashable, Iterable


class Node:
    def __init__(self, key: int | float | bool | str | tuple | Hashable, value: Any) -> None:
        self.key = key
        self.value = value
        self.hash = hash(self.key)


class Dictionary:
    def __init__(
            self,
            capacity: int = 8,
            load_factor: float = 2/3,
            size_of_dict: int = 0
    ) -> None:
        self.capacity = capacity
        self.load_factor = load_factor
        self.size_of_dict = size_of_dict
        self.resize = int(self.capacity * self.load_factor)
        self.hash_table = [None for _ in range(self.capacity)]

    def set_element(self, item: Node):
        index = item.hash % self.capacity
        while True:
            if self.hash_table[index] is None:
                self.hash_table[index] = item
                self.size_of_dict += 1
                break
            if self.hash_table[index].key == item.key:
                self.hash_table[index].value = item.value
                break

            if index + 1 <= self.capacity:
                index += 1
                # index = index % self.capacity
            else:
                index = 0

    def __setitem__(
            self,
            key: int | float | bool | str | tuple | Hashable,
            value: Any
    ) -> None:
        item = Node(key=key, value=value)

        if self.size_of_dict == self.resize:
            self.capacity *= 2
            elements_to_shift = [
                element for element in self.hash_table if element is not None
            ]
            self.hash_table = [None for _ in range(self.capacity)]
            self.size_of_dict = 0
            for element in elements_to_shift:
                self.set_element(element)
            self.set_element(item)
        else:
            self.set_element(item)

    def find_index_of_item(
            self,
            index: int,
            item: int | float | bool | str | tuple | Hashable
    ) -> None:

        while True:
            if (
                    self.hash_table[index] is not None
                    and self.hash_table[index].key == item
            ):
                break
            if index + 1 < self.capacity:
                index += 1
            else:
                index = 0
        return index

    def __getitem__(
            self,
            item: int | float | bool | str | tuple | Hashable
    ) -> Any:
        item_hash = hash(item)
        index = item_hash % self.capacity
        if self.hash_table[index] is not None:
            index = self.find_index_of_item(index=index, item=item)
            return self.hash_table[index].value
        raise KeyError(f"No such key:'{item}' in dictionary")

    def __len__(self) -> int:
        return self.size_of_dict

    def clear(self) -> None:
        self.capacity = 8
        self.size_of_dict = 0
        self.hash_table = [None for _ in range(self.capacity)]

    def __delitem__(
            self,
            key: int | float | bool | str | tuple | Hashable
    ) -> None:
        key_hash = hash(key)
        index = key_hash % self.capacity
        if self.hash_table[index] is not None:
            self.find_index_of_item(index=index, item=key)
            self.hash_table[index] = None
            self.size_of_dict -= 1

    def get(
            self,
            key: int | float | bool | str | tuple | Hashable,
            value: Any = None
    ) -> Any:
        key_hash = hash(key)
        index = key_hash % self.capacity
        if self.hash_table[index] is not None:
            self.find_index_of_item(index=index, item=key)
            return self.hash_table[index].value
        return value

    def pop(
            self,
            keyname: int | float | bool | str | tuple | Hashable,
    ) -> Any:
        key_hash = hash(keyname)
        index = key_hash % self.capacity
        if self.hash_table[index] is not None:
            self.find_index_of_item(index=index, item=keyname)
            return_value = self.hash_table[index].value
            self.hash_table[index] = None
            self.size_of_dict -= 1
            return return_value



    # def __iter__(self):
    #     self.list_of_elements = [
    #         element for element in self.hash_table if element is not None
    #     ]
    #     return self
    #
    # def __next__(self):
    #
    #     # Store current value ofx
    #     x = self.list_of_elements
    #
    #     return x


#     def update(
#             self,
#             iterable: Iterable
#     ):
#
#
#
# dict.update()
#
#
# point = Point(1.2, 2.0)
# new_dict = Dictionary()
#
# new_dict["AAA"] = "value_1"
#
# del new_dict["E"]
#
# new_dict[point] = "value_2"
# print("Hash % 8:", hash(point) % 8)
#
# new_dict[True] = "value_3"
# print("Hash % 8:", hash(True) % 8)
#
# new_dict[4] = "value_4"
#
# new_dict[5] = "value_5"
#
# new_dict[True] = "value_6"
# print("Hash % 8:", hash(True) % 8)
#
# print(new_dict.hash_table)
# print(len(new_dict))
# print(new_dict[True])
#
# print(new_dict.get(5))
# print(new_dict.pop(5))
# print(len(new_dict))
#
# print(new_dict.hash_table)
#
# a = iter(new_dict)
# print(a)
# items = [(f"Element {i}", i) for i in range(1000)]
# dictionary = Dictionary()
# for key, value in items:
#     dictionary[key] = value





