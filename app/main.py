class Dictionary:
    def __init__(self):

        self._values = [None for item in range(256)]
        self._keys = []

    def __getitem__(self, key):

        if self._values[self.hashfunc(key)] is not None:
            return self._values[self.hashfunc(key)]

        else:
            return self.__missing__(key)

    def __setitem__(self, key, value):

        if value is None:
            raise ValueError('None is not permitted as a value.')

        if self._values[self.hashfunc(key)] is None:
            self._keys.append(key)
            self._values[self.hashfunc(key)] = value

            if float(len(self._keys)) / len(self._values) > 0.1:
                self.__resize__()

        else:
            if key in self._keys:
                self._values[self.hashfunc(key)] = value

            else:
                self.__resize__()
                self.__setitem__(key, value)

    def __missing__(self, not_key):

        raise KeyError('{0} is not a valid key'.format(not_key))

    def __repr__(self):

        list_repr = ['{0}:{1}'.format(key, self._values[self.hashfunc(key)])
                     for key in self._keys]
        return 'HashMap({0})'.format(list_repr)

    def __contains__(self, key):

        if key in self._keys:
            return True
        else:
            return False

    def __len__(self):

        return len(self._keys)

    def __iter__(self):

        return (key for key in self._keys)

    def hashfunc(self, key):
        return hash(key) % len(self._values)

    def __resize__(self, **kwargs):
        old_values = kwargs.get('values', [self._values[self.hashfunc(key)]
                                           for key in self._keys])

        self._values = [None for item in range(2 * len(self._values))]

        for key, value in zip(self._keys, old_values):

            if self._values[self.hashfunc(key)] is None:
                self._values[self.hashfunc(key)] = value

            else:
                self.__resize__(values=old_values)
