class Dictionary:

    def __init__(self):
        self.__capacity = 8
        self.__size = 0
        self.__memory: list = [None] * 8

    def resize_memory(self):
        if self.__size == int(self.__capacity * (2 / 3)):
            self.__memory += [None] * self.__capacity
            self.__capacity *= 2
            for index in range(len(self.__memory)):
                if self.__memory[index] is not None:
                    items = self.__memory[index]
                    self.__memory[index] = None
                    self.__size -= 1
                    self.__setitem__(*items)

    def __getitem__(self, key):

        memory_place = hash(key) % self.__capacity

        for _ in range(self.__capacity):
            if self.__memory[memory_place] is not None and\
                    self.__memory[memory_place][0] == key:
                return self.__memory[memory_place][1]
            memory_place = (memory_place + 1) % self.__capacity
        else:
            raise KeyError

    def __setitem__(self, key, value):
        self.resize_memory()
        memory_place = hash(key) % self.__capacity
        if self.__memory[memory_place] is not None:
            while True:
                if memory_place == len(self.__memory) - 1:
                    memory_place = 0
                if self.__memory[memory_place] is not None \
                        and key == self.__memory[memory_place][0]:
                    self.__memory[memory_place] = (key, value)
                    break
                if self.__memory[memory_place] is None:
                    self.__memory[memory_place] = (key, value)
                    self.__size += 1
                    break
                memory_place += 1
        else:
            self.__memory[memory_place] = (key, value)
            self.__size += 1

    def __len__(self):
        return self.__size

    def clear(self):
        self.__memory = [None] * self.__capacity
        self.__size = 0

    def __delitem__(self, key):
        memory_place = hash(key) % self.__capacity
        while True:
            if memory_place == len(self.__memory) - 1:
                memory_place = 0
            if self.__memory[memory_place] is None:
                raise KeyError
            if self.__memory[memory_place][0] == key:
                self.__memory[memory_place] = None
                self.__size -= 1
                break
            memory_place += 1

    def get(self, key, value=None):
        try:
            return self[key]
        except KeyError:
            return value

    def pop(self, key, default_value=None):
        try:
            deleted = self[key]
            self.__delitem__(key)
        except KeyError:
            if default_value is None:
                raise
            else:
                return default_value
        else:
            return deleted

    def update(self, items):
        for key, value in items:
            self[key] = value

    def __iter__(self):
        self._iter_count = -1
        self._counter = 0
        return self

    def __next__(self):
        self._iter_count += 1
        print(self.__size)
        print(self._iter_count)
        while self._iter_count < self.__size:
            if self.__memory[self._iter_count + self._counter] is None:
                self._counter += 1
                continue
            return self.__memory[self._iter_count + self._counter]
        raise StopIteration
