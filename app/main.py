from typing import Union, Any, Iterable, Tuple


# Linear Probing
class Dictionary:
    def __init__(self,
                 initial_capacity: int = 8,
                 load_factor: float = 0.75) -> None:
        # Cells will store (key, value) or None
        self.table: list[Tuple[Any, Any]] = \
            [None] * initial_capacity
        self.size: int = 0
        self.load_factor = load_factor
        self.capacity = initial_capacity

    def _hash(self, key: Any) -> int:
        return hash(key) % self.capacity

    def __setitem__(self, key: Any, value: Any) -> None:
        index = self._hash(key)

        # Linear probing: find an empty slot or replace the existing value
        original_index = index
        while self.table[index] is not None and self.table[index][0] != key:
            index = (index + 1) % self.capacity
            # We have returned to the starting point (table is full)
            if index == original_index:
                raise Exception("Dictionary is full")

        # If the key already exists, update the value
        if self.table[index] is not None:
            self.table[index] = (key, value)
        else:
            self.table[index] = (key, value)
            self.size += 1

        # If the load factor exceeds the threshold, resize the table
        if self.size / self.capacity > self.load_factor:
            self._resize()

    def __getitem__(self, key: Any) -> Any:
        index = self._hash(key)
        original_index = index

        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.capacity
            if index == original_index:
                break

        raise KeyError(f"Key '{key}' not found.")

    def __len__(self) -> int:
        return self.size

    def __delitem__(self, key: Any) -> None:
        index = self._hash(key)
        original_index = index

        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                self.size -= 1
                # After removing an element,
                # we need to rehash the remaining elements
                self._rehash(index)
                return
            index = (index + 1) % self.capacity
            if index == original_index:
                break

        raise KeyError(f"Key '{key}' not found.")

    def __iter__(self) -> Iterable[Any]:
        for item in self.table:
            if item is not None:
                yield item[0]

    def __contains__(self, key: Any) -> bool:
        index = self._hash(key)
        original_index = index

        while self.table[index] is not None:
            if self.table[index][0] == key:
                return True
            index = (index + 1) % self.capacity
            if index == original_index:
                break
        return False

    def _resize(self) -> None:
        new_capacity = self.capacity * 2
        new_table: list[Tuple[Any, Any]] = [None] * new_capacity

        # Rehash all elements into the new table
        for item in self.table:
            if item is not None:
                key, value = item
                index = hash(key) % new_capacity
                while new_table[index] is not None:
                    index = (index + 1) % new_capacity
                new_table[index] = (key, value)

        self.table = new_table
        self.capacity = new_capacity

    def clear(self) -> None:
        self.table = [None] * self.capacity
        self.size = 0

    def get(self, key: Any, default: Any = None) -> Any:
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    def pop(self, key: Any) -> Any:
        index = self._hash(key)
        original_index = index

        while self.table[index] is not None:
            if self.table[index][0] == key:
                value = self.table[index][1]
                self.table[index] = None
                self.size -= 1
                self._rehash(index)
                return value
            index = (index + 1) % self.capacity
            if index == original_index:
                break

        raise KeyError(f"Key '{key}' not found.")

    def _rehash(self, deleted_index: int) -> None:
        # After removing an element, shift remaining elements for proper lookup
        index = (deleted_index + 1) % self.capacity
        while self.table[index] is not None:
            key, value = self.table[index]
            self.table[index] = None
            self.size -= 1
            self.__setitem__(key, value)
            index = (index + 1) % self.capacity

    def items(self) -> Iterable[Tuple[Any, Any]]:
        for item in self.table:
            if item is not None:
                yield item

    def _values(self) -> Iterable[Any]:
        for item in self.table:
            if item is not None:
                yield item[1]

    def update(self,
               *args: Union["Dictionary", Iterable[Tuple[Any, Any]]],
               **kwargs: Any) -> None:
        for arg in args:
            if isinstance(arg, Dictionary):
                for key, value in arg.items():
                    self[key] = value
            elif isinstance(arg, Iterable):
                for key, value in arg:
                    self[key] = value
            else:
                raise TypeError(f"Unsupported type: {type(arg)}")

        for key, value in kwargs.items():
            self[key] = value
