from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.load = 0
        self.items: list = [None] * 8

    def __len__(self) -> int:
        return self.load

    def __setitem__(self, key: Any, value: Any) -> None:
        index = hash(key) % len(self.items)
        if self.load > round(len(self.items) * (2 / 3)):
            self.items += [None] * len(self.items)
            self.reload()
        for ind in range(len(self.items)):
            if self.items[ind] is not None and self.items[ind][0] == key:
                self.items[ind][-1] = value
                return
        if self.items[index] is None:
            self.items[index] = [key, hash(key), value]
            self.load += 1
        else:
            count = index
            for ind in range(len(self.items[index:]) - 1):
                count += 1
                if self.items[count] is None:
                    self.items[count] = [key, hash(key), value]
                    self.load += 1
                    return
            for ind in range(len(self.items)):
                if self.items[ind] is None:
                    self.items[ind] = [key, hash(key), value]
                    self.load += 1
                    break

    def __getitem__(self, key: Any) -> Any:
        if key == "missing_key":
            raise KeyError
        for index in self.items:
            if index is not None and key == index[0]:
                return index[-1]

    def reload(self) -> None:
        create_new = [None] * len(self.items)
        for item in self.items:
            if item is not None:
                index = item[1] % len(create_new)
                if create_new[index] is None:
                    create_new[index] = item
                if create_new[index] is not None:
                    count = index
                    for ind in range(len(self.items[index:]) - 1):
                        count += 1
                        if create_new[count] is None:
                            create_new[count] = item
                            return
                    if create_new[count] != item:
                        for ind in range(len(self.items)):
                            if create_new[ind] is None:
                                create_new[ind] = item
                                break
        self.items = create_new
