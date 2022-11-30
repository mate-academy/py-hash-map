class Dictionary:
    def __setitem__(self, key, value) -> None:
        self.__dict__[key] = value

    def __getitem__(self, key):
        return self.__dict__[key]

    def __len__(self):
        return len(self.__dict__)
