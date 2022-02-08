from dataclasses import dataclass


class Dictionary:
    _DEFAULT_LENGTH = 8
    _LENGTH_RESIZE_COEF = 1 / 2
    _RESIZE_MULT_COEF = 2

    @dataclass
    class _Node:
        key: int
        value: object
        key_hash: int

    def __init__(self):
        self._container = [None] * self._DEFAULT_LENGTH
        self._length = 0
        self._alloc_length = len(self._container)

    def update(self, key, value):
        self._get_node_by_key(key).value = value

    def _resize(self):
        self._alloc_length *= self._RESIZE_MULT_COEF

        old_nodes = self._container
        self._container = [None] * self._alloc_length
        self._length = 0

        for node in old_nodes:
            if node is not None:
                self[node.key] = node.value

    def __setitem__(self, key, value):
        if self._length + 1 == int(self._alloc_length * self._LENGTH_RESIZE_COEF):
            self._resize()

        position = hash(key) % self._alloc_length
        if self._container[position] is not None:
            # if we are trying to add element by the same key
            if self._container[position].key == key:
                self.update(key, value)
            else:
                # trying to find next empty cell and set element there
                index = position + 1
                while self._container[index % self._alloc_length] is not None:
                    index += 1
                self._container[index % self._alloc_length] = self._Node(key, value, hash(key))
                self._length += 1
        else:
            self._container[position] = self._Node(key=key, value=value,key_hash=hash(key))
            self._length += 1

    def __len__(self):
        return self._length

    def _get_node_by_key(self, key):
        position = hash(key)
        index = 0
        while index < self._alloc_length:
            if (node := self._container[position % self._alloc_length]).key == key:
                return node
            position += 1
            index = 1
        raise KeyError

    def __getitem__(self, item):
        return self._get_node_by_key(item).value

    def __repr__(self):
        return str(self._container)
