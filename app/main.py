from typing import List, Any, Optional


class Dictionary:
    def __init__(self, elements: Optional[List[tuple]] = None) -> None:
        if elements is None:
            elements = []
        self._bucket_size = 8
        self._bucket_resize = self._bucket_size * 2 / 3
        self.__length = 0
        self._creating_buckets(len(elements))
        if len(elements):
            self._assign_buckets(elements)

    def _creating_buckets(self, len_elements: int = 0) -> None:
        while len_elements > self._bucket_resize:
            self._bucket_size *= 2
            self._bucket_resize = self._bucket_size * 2 / 3

        self._buckets = [[] for i in range(self._bucket_size)]

    def _assign_buckets(self, elements: List[tuple]) -> None:
        for _key, _value in elements:

            if isinstance(_key, list | dict | set):
                raise TypeError(
                    f'The key can`t be like this: "{_key}" is "{type(_key)}"'
                )
            hashed_value = hash(_key)
            index = hashed_value % self._bucket_size

            while self._buckets[index]:
                if self._buckets[index][0] == _key:
                    if len(self._buckets[index]) == 1:
                        break
                    self.__length -= 1
                    break
                index = (index + 1) % self._bucket_size

            self._buckets[index] = (_key, _value,)
            self.__length += 1

    def _un_assign_buckets(self, _key: Any) -> None:
        hashed_value = hash(_key)
        index = hashed_value % self._bucket_size

        while self._buckets[index]:
            if self._buckets[index][0] == _key:
                if len(self._buckets[index]) == 1:
                    raise KeyError(f'There is no such key: "{_key}"')
                break
            index = (index + 1) % self._bucket_size
        if not self._buckets[index]:
            raise KeyError(f'There is no such key: "{_key}"')
        self._buckets[index] = (_key,)
        self.__length -= 1

    def _get_buckets_full(self) -> list[Any]:
        return [
            full_bucket for full_bucket in self._buckets
            if len(full_bucket) == 2
        ]

    def _resize(
            self,
            new_element: List[tuple],
    ) -> None:
        current_buckets = self._get_buckets_full()
        current_buckets += new_element

        self._creating_buckets(self.__length + len(new_element))
        self.__length = 0
        self._assign_buckets(current_buckets)

    def __setitem__(self, _key: Any, _value: Any) -> None:
        if self.__length + 1 > self._bucket_resize:
            self._resize([(_key, _value)])
        self._assign_buckets([(_key, _value)])

    def __getitem__(self, input_key: Any) -> Any:
        hashed_value = hash(input_key)
        index = hashed_value % self._bucket_size
        if input_key not in self.keys():
            raise KeyError(f'There is no such key: "{input_key}"')

        while self._buckets[index]:
            _key = self._buckets[index][0]
            if _key == input_key:
                if len(self._buckets[index]) == 1:
                    raise KeyError(f'There is no such key: "{input_key}"')
                return self._buckets[index][1]
            index = (index + 1) % self._bucket_size

    def __delitem__(self, input_key: Any) -> None:
        self._un_assign_buckets(input_key)

    def __str__(self) -> str:
        dict_str = "  {\n"
        for _key, _value in self._get_buckets_full():
            dict_str += f"    {_key}: {_value},\n"
        dict_str += "}"
        return f"{self._buckets}"

    def __repr__(self) -> str:
        dict_repr = "{"
        for _key, _value in self._get_buckets_full():
            dict_repr += f"{_key}: {_value}, "
        dict_repr += "}"
        return dict_repr

    def __len__(self) -> int:
        return self.__length

    def keys(self) -> list[Any]:
        return [_key for _key, _ in self._get_buckets_full()]

    def values(self) -> list[Any]:
        return [_value for _, _value in self._get_buckets_full()]

    def clear(self) -> None:
        self._buckets = [[] for i in range(self._bucket_size)]
        self.__length = 0

    def get(self, _key: Any) -> Any:
        _value = None
        try:
            _value = self[_key]
        except KeyError:
            return None
        return _value

    def update(self, elements: List[tuple]) -> None:
        if self.__length + len(elements) > self._bucket_resize:
            self._resize(elements)
        self._assign_buckets(elements)
