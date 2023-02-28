from typing import Iterable, Hashable, Any, Generator, List
from dataclasses import dataclass


@dataclass
class Node:
    key_hash: int
    key: Hashable
    value: Any
    deleted = False


class Dictionary:
    min_size = 8
    load_fac = 0.65

    def __init__(self, iterable: Iterable = (), ) -> None:
        self.capacity = (max(self.min_size, len([iterable]) * 2))
        self.indices: list = [None] * self.capacity
        self.content = []
        self.length = 0
        if iterable:
            self._add_from_iterable(iterable)

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.capacity * self.load_fac < len(self) + 1:
            self._resize()
        for catalog_ind, link_to_content in self._indices_generator(key):
            if link_to_content is None or link_to_content.deleted:
                self._add_to_content_list(key, value, catalog_ind)
                return
            if hash(key) == link_to_content.key_hash and key == link_to_content.key:
                link_to_content.deleted = True
                self.length -= 1
                self._add_to_content_list(key, value, catalog_ind)
                return

    def __getitem__(self, key: Hashable) -> Any:
        if not self._key_exist(key):
            raise KeyError(f"{key} key doesn't exist in this Dictionary")
        for catalog_ind, link_to_content in self._indices_generator(key):
            if not link_to_content.deleted and key == link_to_content.key:
                return link_to_content.value

    def __delitem__(self, key: Hashable) -> None:
        if not self._key_exist(key):
            raise KeyError(f"{key} key doesn't exist in this Dictionary")
        for catalog_ind, link_to_content in self._indices_generator(key):
            if hash(key) == link_to_content.key_hash and key == link_to_content.key:
                link_to_content.deleted = True
                self.length -= 1
                return

    def __len__(self) -> int:
        return self.length

    def __iter__(self) -> Iterable:
        return iter([(node.key, node.value)
                     for node in self.content if not node.deleted])

    def __str__(self) -> str:
        return "\n".join([f"key {node.key}: value {node.value}"
                          for node in self.content if not node.deleted])

    def _key_exist(self, key: Hashable) -> bool:
        return key in set(node.key for node in self.content if not node.deleted)

    def _indices_generator(self, key: Hashable) -> Generator:
        catalog_ind = hash(key) % self.capacity
        while True:
            yield catalog_ind, (self.content[self.indices[catalog_ind]]
                                if self.indices[catalog_ind] is not None else None)
            catalog_ind = (catalog_ind + 1) % self.capacity

    def _add_to_content_list(self,
                             key: Hashable,
                             value: Any,
                             catalog_ind: int) -> None:
        self.content.append(Node(hash(key), key, value))
        self.indices[catalog_ind] = len(self.content) - 1
        self.length += 1

    def _resize(self) -> None:
        self.length = 0
        self.capacity *= 2
        self.indices: list = [None] * self.capacity
        copy_content = self.content[:]
        self.content.clear()
        for i in range(len(copy_content)):
            if not copy_content[i].deleted:
                self.__setitem__(copy_content[i].key, copy_content[i].value)

    def _add_from_iterable(self, iterable: Iterable) -> None:
        for key, value in iterable:
            self.__setitem__(key, value)

    def get(self, key: Hashable, default: Any = None) -> Any:
        try:
            value = self.__getitem__(key)
        except KeyError:
            value = default
        return value

    def clear(self) -> None:
        self.indices: list = [None] * self.capacity
        self.content = []
