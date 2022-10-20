class Dictionary:
    def __setitem__(self, key: str, value: int) -> None:
        self.__dict__[key] = value

    def __getitem__(self, key: str) -> None:
        return self.__dict__[key]

    def __len__(self) -> int:
        return len(self.__dict__)

    def __repr__(self) -> str:
        return repr(self.__dict__)

    def __delitem__(self, key: str) -> None:
        del self.__dict__[key]

    def __contains__(self, value: int) -> int:
        return value in self.__dict__
