import math


class Dictionary:
    def __init__(self):
        self.__storage = [None] * 8
        self.__capacity = 8
        self.__load_factor = 2 / 3
        self.__key_index = []
        self.__length = 0

    def __setitem__(self, key, value):
        for element in self.__key_index:
            if element[0] == key:
                for index, item in enumerate(self.__storage):
                    if element[1] == index:
                        self.__storage[index] = value
                        return

        count = 0
        for char in self.__storage:
            if char:
                count += 1

        if count == math.floor(self.__capacity * self.__load_factor):
            self.__resize_dict()

        self.__add_to_dict(key, value)

    def __resize_dict(self):
        self.__length = 0
        values = self.__storage
        self.__capacity *= 2
        self.__storage = [None] * self.__capacity

        for index, value in enumerate(values):
            if value is not None:
                for item_link in self.__key_index:
                    if index == item_link[1]:
                        self.__add_to_dict(item_link[0], value)
                        self.__key_index.remove(item_link)
                        break

    def __add_to_dict(self, key, value):
        index = hash(key) % self.__capacity

        while True:
            if index >= self.__capacity:
                index = 0

            if self.__storage[index] is None:
                self.__storage[index] = value
                self.__key_index.append((key, index))
                self.__length += 1
                break
            index += 1

    def __getitem__(self, key):
        index = 0
        flag = False
        for elem in self.__key_index:
            if key in elem:
                index = elem[1]
                flag = True
                break
        if flag:
            return self.__storage[index]
        raise KeyError("No keys!")

    def __len__(self):
        return self.__length

    def __repr__(self):
        result = []

        for index in range(len(self.__key_index)):
            result.append((self.__key_index[index][0],
                           self.__storage[self.__key_index[index][1]]))

        return f"{result}"
