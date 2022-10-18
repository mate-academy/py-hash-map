from typing import Any


class Dictionary:
    def __init__(self, init: Any = None) -> None:
        if init is not None:
            self.__dict__.update(init)

    def __getitem__(self, key: Any) -> dict:
        return self.__dict__[key]

    def __setitem__(self, key: Any, value: Any) -> None:
        self.__dict__[key] = value

    def __delitem__(self, key: Any) -> None:
        del self.__dict__[key]

    def __contains__(self, key: Any) -> bool:
        return key in self.__dict__

    def __len__(self) -> int:
        return len(self.__dict__)

    def __repr__(self) -> str:
        return repr(self.__dict__)
