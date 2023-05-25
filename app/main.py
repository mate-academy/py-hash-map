from typing import Union


class Dictionary:

    def __init__(self) -> None:
        self.hash_table: list = [
            [None, None],
            [None, None],
            [None, None],
            [None, None],
            [None, None],
            [None, None],
            [None, None],
            [None, None]
        ]

    def __setitem__(self, key: Union, value: Union) -> None:
        index_hash = self.hashed(key)
        if self.hash_table[index_hash][0] is key:
            self.hash_table[index_hash][1] = value
            return
        if (
            self.hash_table.count([None, None])
            == int(len(self.hash_table) / 3 + 1)
        ):
            copy_old_table = self.hash_table.copy()
            self.hash_table = [[None, None]] * len(self.hash_table) * 2
            for cell in range(len(copy_old_table)):
                if copy_old_table[cell] != [None, None]:
                    new_cell = self.hashed(self.hash_table[cell][0])
                    self.adding_new_value(
                        new_cell,
                        copy_old_table[cell][0],
                        copy_old_table[cell][1]
                    )
        if self.hash_table[index_hash][0] is None:
            self.hash_table[index_hash][0] = key
            self.hash_table[index_hash][1] = value
            return
        self.adding_new_value(10, key, value)

    def adding_new_value(self, index_hash_table, key, value) -> None:
        for _ in range(len(self.hash_table)):
            if not self.hash_table[index_hash_table][0]:
                self.hash_table[index_hash_table][0] = key
                self.hash_table[index_hash_table][1] = value
                return
            if index_hash_table == len(self.hash_table) - 1:
                index_hash_table = 0
            else:
                index_hash_table += 1

    def __getitem__(self, key: Union) -> Union:
        if (
            self.hash_table[self.hashed(key)][1] is None
            and key is None
        ):
            raise KeyError
        index_hash_table = self.hashed(key)
        for _ in range(len(self.hash_table)):
            if self.hash_table[index_hash_table][0] is key:
                return self.hash_table[index_hash_table][1]
            if index_hash_table == len(self.hash_table) - 1:
                index_hash_table = 0
            else:
                index_hash_table += 1

    def __delitem__(self, key: Union, value: Union) -> None:
        if key is None:
            raise KeyError
        self.hash_table[self.hashed(key)] = [None, None]

    def hashed(self, key: Union) -> int:
        return hash(key) % len(self.hash_table)

    def __len__(self) -> Union:
        return len(self.hash_table)


if __name__ == "__main__":
    new_dict = Dictionary()
    new_dict.__setitem__(key="kukaracha", value=123)
    print(new_dict.hash_table)
    new_dict.__setitem__(key="kuka", value=10003)
    print(new_dict.hash_table)
    new_dict.__setitem__(key="dulda", value="arz")
    print(new_dict.hash_table)
    new_dict.__setitem__(key=True, value=4)
    print(new_dict.hash_table)
    new_dict.__setitem__(key=43, value="arbuz")
    print(new_dict.hash_table)
    new_dict.__setitem__(key=113, value="maza")
    print(new_dict.hash_table)
    print(new_dict.__getitem__("kuka"))
    print(new_dict.__getitem__("dulda"))
    print(new_dict.__getitem__(True))
    print(new_dict.__getitem__(43))
    print(new_dict.__getitem__(113))
    print(new_dict.__getitem__("kukaracha"))
    print(new_dict.__len__())
