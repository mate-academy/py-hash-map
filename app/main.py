class Dictionary:
    def __init__(self):
        self._data = {}

    def __getitem__(self, item):
        return self._data[item]

    def __setitem__(self, key, value):
        self._data[key] = value

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"{self._data}"

    def clear(self):
        self._data = {}

    def __delitem__(self, key):
        del self._data[key]

    def get(self, key, defolt_valye):
        return self._data[key] if key in self._data.keys() else defolt_valye

    def pop(self, key):
        self._data.pop(key)

    def update(self, dictionary):
        self._data.update(dictionary)

    def __iter__(self):
        return iter(self._data)
