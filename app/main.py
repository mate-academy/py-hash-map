from typing import Any


class Dictionary(dict):
    def __getitem__(self, key: str | int | float) -> Any:
        return self.__dict__[key]

    def __setitem__(self, key: str | int | float, value: Any) -> None:
        self.__dict__[key] = value

    def __len__(self) -> int:
        return len(self.__dict__)
