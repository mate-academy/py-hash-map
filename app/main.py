from typing import Any, Hashable


class Dictionary:
    load_factor = 2 / 3

    def __init__(self) -> None:
        self.length = 0
        self.capacity = 8
        self.hash_table = [None] * self.capacity

    def __setitem__(
            self,
            key: Hashable,
            value: Any
    ) -> None:
        key_hash = hash(key)
        items = [key, key_hash, value]
        if self.length >= round(self.capacity * self.load_factor):
            self.__hash_table_resize()

        self.__put_key_value_to_a_hash_table(items)

    def __hash_table_resize(self) -> None:
        template_hash_table = self.hash_table
        self.capacity *= 2
        self.hash_table = [None] * self.capacity
        for items in template_hash_table:
            if items:
                self.__put_key_value_to_a_hash_table(
                    items,
                    ignore_counter_of_length=True
                )

    def __put_key_value_to_a_hash_table(
        self,
        items: list[Hashable | int | Any],
        ignore_counter_of_length: bool = False
    ) -> Any:

        key, key_hash, value = items
        index_in_hash_table = key_hash % self.capacity

        while True:
            cell = self.hash_table[index_in_hash_table]
            if not cell:
                break
            if key_hash == cell[1]:
                if key == cell[0]:
                    cell[2] = value
                    return
            index_in_hash_table = (index_in_hash_table + 1) % self.capacity

        self.hash_table[index_in_hash_table] = items
        if not ignore_counter_of_length:
            self.length += 1

    def __getitem__(self, item: Hashable) -> Any:
        index_in_hash_table = hash(item) % self.capacity

        while True:
            cell = self.hash_table[index_in_hash_table]

            if not cell:
                raise KeyError("No such key found in this dictionary")
            if item == cell[0]:
                return cell[2]

            index_in_hash_table = (index_in_hash_table + 1) % self.capacity

    def __len__(self) -> int:
        return self.length

    def __delitem__(self, key: Hashable) -> None:
        index_in_hash_table = hash(key) % self.capacity
        times = 0
        while times <= self.capacity:
            cell = self.hash_table[index_in_hash_table]
            if cell:
                if key == cell[0]:
                    self.hash_table[index_in_hash_table] = None
                    break
            times += 1

            index_in_hash_table = (index_in_hash_table + 1) % self.capacity
