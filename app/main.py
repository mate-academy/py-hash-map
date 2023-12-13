from abc import ABC

from app.point import Point


class DictionaryMember:
    def __init__(
            self,
            key: int | str | tuple | float,
            value: any
    ) -> None:
        self.key = key
        self.value = value
        # self.next = None


class Dictionary:

    def __init__(
            self,
            capacity: int = 10,
            load_factor: float = 0.75
    ) -> None:

        self.size = 0
        self.capacity = capacity
        self.load_factor = load_factor
        self.table = [None] * self.capacity

    def _index(
            self,
            key: int | str | tuple | float
    ) -> int:
        return hash(key) % self.capacity

    def __len__(self):
        return self.size

    def _resize(self):
        pass

    def __setitem__(
            self,
            key: int | str | tuple | float,
            value: any
    ) -> None:

        key_index = self._index(key)

        if self.table[key_index] is None:
            self.table[key_index] = DictionaryMember(key=key, value=value)
            self.size += 1
            print("Data wrote")

        else:
            current = self.table[key_index]

            if current.key == key:
                current.value = value
                print("Data rewrote")

            if current.key != key:

                while (
                        self.table[key_index] is not None
                        and self.table[key_index].key != key
                ):
                    key_index += 1

                if current is None:
                    self.table[key_index] = DictionaryMember(key=key, value=value)
                    self.size += 1
                    print("Data wrote")

                if self.table[key_index].key == key:
                    self.table[key_index].value = value
                    print("Data rewrote")

        if self.size / self.capacity > self.load_factor:
            self._resize()

    def __getitem__(
            self,
            key: int | str | tuple | float
    ) -> any:

        index = self._index(key)
        current = self.table[index]

        try:
            if current.key == key:
                return current

            else:
                try:
                    while self.table[index].key != key:
                        index += 1
                    return self.table[index]

                except AttributeError:
                    raise

        except AttributeError:
            print("There no such element")

    def _clear(self) -> None:
        self.table = [None] * self.capacity
        print("All data in this dict was deleted")

    # def __delitem__(self, key: any) -> None:
    #     self.data.__delitem__(key)
    #     print(f"Item with key {key} was destroyed")

    # def pop(self, key: any) -> any:
    #     poped = self.data.pop(key)
    #     return poped
