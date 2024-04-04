from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.hash_table = [[] for _ in range(self.capacity)]

    def __repr__(self) -> str:
        return f'{self.__dict__["hash_table"]}'

    def _get_node_index(self, key: Any) -> int:
        """ Computes node index based on the key hash """
        return hash(key) % self.capacity

    def _get_node_content(self, key: Any) -> list:
        """ Returns a single node content """
        node_index = self._get_node_index(key)
        return self.hash_table[node_index]

    def __setitem__(self, key: Any, value: Any) -> None:
        """ Stores a new key-value pair or update existing. """
        node_content = self._get_node_content(key)
        for i, (k, *_) in enumerate(node_content):
            if k == key:
                del node_content[i]
                node_content.insert(i, (key, hash(key), value))
                return
        node_content.append((key, hash(key), value))

    def __getitem__(self, key: Any) -> str | int:
        """ Looks up a value with the specified key """
        node_content = self._get_node_content(key)
        for k, _, v in node_content:
            if key == k:
                return v
        raise KeyError(f"Key {key} doesn't exist.")

    def __delitem__(self, key: Any) -> None:
        node_content = self._get_node_content(key)
        for i, (k, _, v) in enumerate(node_content):
            if k == key:
                del node_content[i]
                return
        raise KeyError(f"Key {key} doesn't exist.")

    def __len__(self) -> int:
        return sum(len(node) for node in self.hash_table)

    def get(self, key: Any, default: Any = None) -> Any:
        """ Returns a value of the specified key, otherwise default value """
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    def pop(self, key: Any, default: Any = None) -> Any:
        """ Removes the element with the specified key """
        try:
            value = self[key]
            del self[key]
            return value
        except KeyError:
            return default

    def update(self, other_dict: dict) -> None:
        """ Updates the dictionary with the specified key-value pairs """
        for key, value in other_dict.items():
            self.__setitem__(key, value)

    def __iter__(self) -> None:
        for node in self.hash_table:
            for key, *_ in node:
                yield key

    def clear(self) -> None:
        """ Removes all the elements from the dictionary """
        self.hash_table = [[] for _ in range(self.capacity)]

    def resize(self) -> None:
        self.capacity *= 2
        old_hash_table = self.hash_table
        self.hash_table = [[] for _ in range(self.capacity)]
        for node in old_hash_table:
            for key, _, value in node:
                self[key] = value
