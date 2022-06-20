class Dictionary:

    def __init__(self, init=None):
        if init is not None:
            self.__dict__.update(init)

    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __getitem__(self, key):
        return self.__dict__[key]

    def __len__(self):
        return len(self.__dict__)

    def clear(self):
        return self.__dict__.clear()

    def __delitem__(self, key):
        del self.__dict__[key]

    def pop(self, *args):
        return self.__dict__.pop(*args)

    def __iter__(self):
        return iter(self.__dict__)
