from typing import Iterable, Hashable, Any, Generator


class Dictionary:
    min_size = 8
    load_fac = 0.65

    def __init__(self, iterable: Iterable = (),) -> None:
        self.capacity = (max(self.min_size,
                             int(len([iterable]) / self.load_fac)))
        self.indices: list = [None] * self.capacity
        self.content = []
        if iterable:
            self._add_from_iterable(iterable)

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.capacity * self.load_fac < len(self) + 1:
            self._resize()
        for catalog_ind, link_to_content in self._indices_generator(key):
            if link_to_content is None:
                self._add_to_content_list(key, value, catalog_ind)
                return
            if self._same_hash_and_key(key, link_to_content):
                self.content[link_to_content] = "_deleted_item_"
                self._add_to_content_list(key, value, catalog_ind)
                return

    def __getitem__(self, key: Hashable) -> Any:
        for catalog_ind, link_to_content in self._indices_generator(key):
            if link_to_content is None:
                raise KeyError(f"there is no {key} record in this Dictionary")
            elif (isinstance(link_to_content, int)
                  and self._same_hash_and_key(key, link_to_content)):
                return self.content[link_to_content][2]

    def __delitem__(self, key: Hashable) -> None:
        if key not in set(trio[1] for trio in self.content
                          if trio != "_deleted_item_"):
            raise KeyError(f"there is no {key} record in this Dictionary")
        for catalog_ind, link_to_content in self._indices_generator(key):
            if self._same_hash_and_key(key, link_to_content):
                self.indices[catalog_ind] = None
                self.content[link_to_content] = "_deleted_item_"
                return

    def __len__(self) -> int:
        return sum(1 for ind in self.indices if ind is not None)

    def __iter__(self) -> Iterable:
        current_pairs = [(trio[1], trio[2]) for trio in self.content
                         if trio != "_deleted_item_"]
        return iter(current_pairs)

    def __str__(self) -> str:
        return "\n".join([f"key {pair[0]}: value {pair[1]}" for pair in self])

    def _indices_generator(self, key: Hashable) -> Generator:
        catalog_ind = hash(key) % self.capacity
        link_to_content = self.indices[catalog_ind]
        yield catalog_ind, link_to_content
        while True:
            catalog_ind = (catalog_ind + 1) % self.capacity
            link_to_content = self.indices[catalog_ind]
            yield catalog_ind, link_to_content

    def _resize(self) -> None:
        self.capacity *= 2
        self.indices: list = [None] * self.capacity
        copy_content = self.content[:]
        self.content.clear()
        for i in range(len(copy_content)):
            if copy_content[i] != "_deleted_item_":
                self.__setitem__(copy_content[i][1], copy_content[i][2])

    def _add_from_iterable(self, iterable: Iterable) -> None:
        for key, value in iterable:
            self.__setitem__(key, value)

    def _same_hash_and_key(self,
                           key: Hashable,
                           link_to_content: int) -> bool:
        return (hash(key) == self.content[link_to_content][0]
                and key == self.content[link_to_content][1])

    def _add_to_content_list(self,
                             key: Hashable,
                             value: Any,
                             catalog_ind: int) -> None:
        self.content.append([hash(key), key, value])
        self.indices[catalog_ind] = len(self.content) - 1

    def get(self, key: Hashable, default: Any = None) -> Any:
        try:
            value = self.__getitem__(key)
        except KeyError:
            value = default
        return value

    def clear(self) -> None:
        self.indices: list = [None] * self.capacity
        self.content = []
