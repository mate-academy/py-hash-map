from __future__ import annotations


class Dictionary:
    def __init__(self, iterable: iter = None, *args, **kwargs: any) -> None:
        self.capacity = 8
        self.hash_table = [[] for _ in range(self.capacity)]
        if iterable:
            for key, value in iterable:
                self[key] = value
        for key, value in kwargs.items():
            self[key] = value

    def items(self):
        return iter([value[0], value[1]] for value in self.hash_table if value)

    def keys(self):
        return iter(value[0] for value in self.hash_table if value)

    def get(self, key):
        try:
            return self[key]
        except KeyError:
            return None

    def pop(self, key):
        value = self.hash_table[self.find_index(key)][1]
        self.hash_table[self.find_index(key)] = []
        return value

    def update(self, iterable: dict | Dictionary = None, **kwargs):
        if iterable:
            for key, value in iterable.items():
                self[key] = value
        else:
            for key, value in kwargs.items():
                self[key] = value

    def clear(self):
        self.capacity = 8
        self.hash_table = [[] for _ in range(self.capacity)]

    def find_index(self, key):
        index = hash(key) % self.capacity
        for _ in range(self.capacity):
            if key not in self.hash_table[index % self.capacity]:
                index = (index + 1) % self.capacity

        if hash(key) not in self.hash_table[index]:
            raise KeyError("Key does not exist")
        return index

    def __setitem__(self, key, value):
        if len(self) >= self.capacity * 0.625:
            self.capacity *= 2
            tempo = Dictionary(self.items())
            self.hash_table = [[] for _ in range(self.capacity)]
            self.update(tempo)

        index = hash(key) % self.capacity
        while self.hash_table[index]:
            index = (index + 1) % self.capacity
        self.hash_table[index] = [key, value, hash(key)]

    def __getitem__(self, item):
        index = self.find_index(item)
        try:
            return self.hash_table[index][1]
        except IndexError:
            raise KeyError("Key does not exist")

    def __delitem__(self, key):
        self.hash_table[self.find_index(key)] = []

    def __iter__(self):
        return iter(value[1] for value in self.hash_table if value)

    def __len__(self):
        return [1 for socket in self.hash_table if socket].__len__()

    def __str__(self):
        return "".join("{}: {}\n".format(socket[0], socket[1]) for socket in self.hash_table if socket)

benedict = Dictionary()
benedict["Ben"] = "LaBravo"
benedict["Artha"] = "Cucumber"
benedict[13] = [144, 354, 3435]

fren_bow = Dictionary(Friren=2022, astle="vania", DMC=2004)

fren_bow.update(benedict)
fren_bow["Aboba"] = "NOPE"
fren_bow.update(kjawr=43566, lklfj_f="gsg454", sfgrhs="345i", afwa="540g")


yare = {"Bob": 1111, "Dog": 13464}

del(fren_bow["Ben"])
print(fren_bow.pop("Artha"))
print(fren_bow, len(fren_bow))

fren_bow.clear()
print(fren_bow.hash_table)