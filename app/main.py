class Dictionary:
    def __init__(self):
        self._dict = {}

    def __setitem__(self, key, value):
        self._dict[key] = value

    def __getitem__(self, item):
        return self._dict[item]

    def __len__(self):
        return len(self._dict)

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current >= len(self._dict):
            raise StopIteration

        result = self._dict[self.current]
        self.current += 1

        return result

    def __delitem__(self, key):
        print("Hello", key)

    def get(self):
        return self._dict

    def pop(self, key):
        self._dict.pop(key)

    def update(self, new_dict):
        self._dict.update(new_dict)
