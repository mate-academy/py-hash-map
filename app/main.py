from abc import ABC

from app.point import Point


class Dictionary:

    def __init__(self) -> None:
        self.data = {}

    def __setitem__(self, key, value) -> None:

        if key not in self.data:
            self.data.__setitem__(key, value)
            print(f"Set ({key}) as a key with value ({value}) to dictionary")

        if key in self.data:
            self.data.__setitem__(key, value)
            print(f"Value of key ({key}) was rewritten to ({value})")

    def __getitem__(self, item) -> any:

        try:
            self.data.__getitem__(item)

        except KeyError:
            print("There is no such key in this dictionary")
            raise KeyError(f"Key ({item}) not found in the dictionary")

    def __len__(self) -> int:
        print("Len of this dict:")
        return len(self.data)

    def clear(self) -> None:
        self.data.clear()
        print("All data in this dict was deleted")

    def __delitem__(self, key: any) -> None:
        self.data.__delitem__(key)
        print(f"Item with key {key} was destroyed")

    def pop(self, key: any) -> any:
        poped = self.data.pop(key)
        return poped

