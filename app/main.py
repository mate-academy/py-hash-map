from typing import Any


class Dictionary:
    def __setitem__(self, key: Any, value: Any) -> None:
        self.__dict__[key] = value

    def __getitem__(self, key: Any) -> Any:
        return self.__dict__[key]

    def __len__(self) -> int:
        return len(self.__dict__)
