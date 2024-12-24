from typing import Any, Tuple, Union, Iterable


# Two Lists With Linear Probing
class Dictionary:
    def __init__(self,
                 initial_capacity: int = 8,
                 load_factor: float = 0.75) -> None:
        self.capacity: int = initial_capacity
        self.size: int = 0
        self.load_factor = load_factor

        # Two lists. One for keys and another for values
        self.keys: list[Union[Any, None]] = [None] * self.capacity
        self.values: list[Union[Any, None]] = [None] * self.capacity
        # Status list. None - empty. False - deleted
        self.status: list[Union[None, bool]] = [None] * self.capacity

    def _hash(self, key: Any) -> int:
        return hash(key) % self.capacity

    def __setitem__(self, key: Any, value: Any) -> None:
        index = self._hash(key)
        # Search if any empty space
        while self.status[index] is not None:
            # If we have deleted slot - override
            if self.status[index] is False:
                break
            if self.keys[index] == key:  # If key exists
                self.values[index] = value
                return
            index = (index + 1) % self.capacity  # Linear Probing

        self.keys[index] = key
        self.values[index] = value
        self.status[index] = True
        self.size += 1

        if self.size / self.capacity > self.load_factor:
            self._resize()

    def __getitem__(self, key: Any) -> Any:
        index = self._hash(key)
        while self.status[index] is not None:
            if self.status[index] is False:
                index = (index + 1) % self.capacity
                continue
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.capacity
        raise KeyError(f"Key '{key}' not found.")

    def __len__(self) -> int:
        return self.size

    def _resize(self) -> None:
        new_capacity = self.capacity * 2
        new_keys = [None] * new_capacity
        new_values = [None] * new_capacity
        new_status = [None] * new_capacity
        old_keys = self.keys
        old_values = self.values
        old_status = self.status

        # Re-hash
        for i in range(self.capacity):
            if old_status[i] is not None:
                key = old_keys[i]
                value = old_values[i]
                index = hash(key) % new_capacity
                while new_status[index] is not None:
                    index = (index + 1) % new_capacity
                new_keys[index] = key
                new_values[index] = value
                new_status[index] = True

        self.keys = new_keys
        self.values = new_values
        self.status = new_status
        self.capacity = new_capacity

    def clear(self) -> None:
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        self.status = [None] * self.capacity
        self.size = 0

    def __delitem__(self, key: Any) -> None:
        index = self._hash(key)
        while self.status[index] is not None:
            if self.status[index] is False:
                index = (index + 1) % self.capacity
                continue
            if self.keys[index] == key:
                self.status[index] = False  # Delete pointer
                self.size -= 1
                return
            index = (index + 1) % self.capacity
        raise KeyError(f"Key '{key}' not found.")

    def get(self, key: Any, default: Any = None) -> Any:
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    def pop(self, key: Any) -> Any:
        index = self._hash(key)
        while self.status[index] is not None:
            if self.status[index] is False:
                index = (index + 1) % self.capacity
                continue
            if self.keys[index] == key:
                self.status[index] = False  # Delete pointer
                self.size -= 1
                return self.values[index]
            index = (index + 1) % self.capacity
        raise KeyError(f"Key '{key}' not found.")

    def items(self) -> Iterable[Tuple[Any, Any]]:
        for i in range(self.capacity):
            if self.status[i] is not None and self.status[i] is not False:
                yield self.keys[i], self.values[i]

    def values(self) -> Iterable[Any]:
        for i in range(self.capacity):
            if self.status[i] is not None and self.status[i] is not False:
                yield self.values[i]

    def __iter__(self) -> Iterable[Any]:
        for i in range(self.capacity):
            if self.status[i] is not None and self.status[i] is not False:
                yield self.keys[i]

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

    def __contains__(self, key: Any) -> bool:
        index = self._hash(key)
        while self.status[index] is not None:
            if self.status[index] is False:
                index = (index + 1) % self.capacity
                continue
            if self.keys[index] == key:
                return True
            index = (index + 1) % self.capacity
        return False
