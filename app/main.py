from typing import Any


class Dictionary:

    def __setitem__(self, key: Any, item: Any) -> None:
        self.__dict__[key] = item

    def __getitem__(self, key: Any) -> dict:
        return self.__dict__[key]

    def __len__(self) -> int:
        return len(self.__dict__)

    def __delitem__(self, key: Any) -> None:
        del self.__dict__

    def __iter__(self) -> iter:
        return iter(self.__dict__)
