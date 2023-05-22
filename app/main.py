from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.capacity = 4
        self.len = 0
        self.container = [None] * self.capacity

    def resize(self, size: int) -> None:
        container = self.container
        self.capacity = size
        self.container = [None] * size
        self.len = 0
        for item in container:
            if item is not None:
                self[item[0]] = item[2]

    def _get_key_position(self, key: Any) -> int:
        key_hash = hash(key) % self.capacity
        position = key_hash
        while \
                (self.container[position] is not None) and \
                (self.container[position][1] > position):
            position += 1
        while \
                (position < self.capacity) and \
                (self.container[position] is not None) and \
                (self.container[position][1] < key_hash):
            position += 1
        if position >= self.capacity:
            position = 0
            while \
                    (self.container[position] is not None) and \
                    (self.container[position][1] < key_hash):
                position += 1
        while \
                (position < self.capacity) and \
                (self.container[position] is not None) and \
                (self.container[position][1] == key_hash) and \
                (self.container[position][0] != key):
            position += 1
        if position >= self.capacity:
            position = 0
            while \
                    (self.container[position] is not None) and \
                    (self.container[position][1] == key_hash) and \
                    (self.container[position][0] != key):
                position += 1
        return position

    def _move_up(self, position: int) -> None:
        move_border = position + 1
        while \
                (move_border < self.capacity) and \
                (self.container[move_border] is not None) and \
                (self.container[move_border][1] < move_border):
            move_border += 1
        self.container[position:move_border - 1] = \
            self.container[position + 1:move_border]
        if \
                (move_border < self.capacity) or \
                (self.container[0] is None) or \
                (self.container[0][1] == 0):
            self.container[move_border - 1] = None
        else:
            self.container[-1] = self.container[0]
            move_border = 1
            while \
                    (self.container[move_border] is not None) and \
                    (self.container[move_border][1] != move_border):
                move_border += 1
            self.container[:move_border - 1] = self.container[1:move_border]
            self.container[move_border - 1] = None
        self.len -= 1

    def _move_down(self, position: int) -> None:
        move_border = position + 1
        while \
                (move_border < self.capacity) and \
                (self.container[move_border] is not None):
            move_border += 1
        if move_border < self.capacity:
            self.container[position + 1:move_border + 1] = \
                self.container[position:move_border]
        else:
            last = self.container[-1]
            self.container[position + 1:move_border + 1] = \
                self.container[position:move_border]
            move_border = 0
            while self.container[move_border] is not None:
                move_border += 1
            self.container[1:move_border + 1] = self.container[:move_border]
            self.container[0] = last
        self.container[position] = None
        self.len += 1

    def __setitem__(self, key: Any, value: Any) -> None:
        key_hash = hash(key) % self.capacity
        new_item = (key, key_hash, value)
        position = self._get_key_position(key)
        if \
                (self.container[position] is not None) and \
                (self.container[position][0] != key):
            self._move_down(position)
        elif self.container[position] is None:
            self.len += 1
        self.container[position] = new_item
        if self.len > self.capacity * 2 / 3:
            self.resize(self.capacity * 2)

    def __getitem__(self, key: Any) -> Any:
        position = self._get_key_position(key)
        if \
                (self.container[position] is not None) and \
                (self.container[position][0] == key):
            return self.container[position][2]
        else:
            raise KeyError(key)

    def __len__(self) -> int:
        return self.len

    def clear(self) -> None:
        self.len = 0
        self.container = [None] * self.capacity

    def __delitem__(self, key: Any) -> None:
        position = self._get_key_position(key)
        if \
                (self.container[position] is not None) and \
                (self.container[position][0] == key):
            self._move_up(position)
        else:
            raise KeyError(key)

    def get(self, key: Any, default: Any = None) -> Any:
        position = self._get_key_position(key)
        if \
                (self.container[position] is not None) and \
                (self.container[position][0] == key):
            return self.container[position][2]
        else:
            return default

    def pop(self, key: Any) -> Any:
        position = self._get_key_position(key)
        if \
                (self.container[position] is not None) and \
                (self.container[position][0] == key):
            value = self.container[position][2]
            self._move_up(position)
            return value
        else:
            raise KeyError(key)

    def update(self, other: dict) -> None:
        for key in other:
            self[key] = other[key]

    def __iter__(self) -> None:
        return iter(item[0] for item in self.container if item is not None)
