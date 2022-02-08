from math import ceil


class Dictionary:
    def __init__(self):
        self.len = 8
        self.list = [[] for _ in range(self.len)]

    def __setitem__(self, key, value):
        self.resize()  # Check if necessary to change list length

        if isinstance(key, int):
            element_cell = key % self.len
        else:
            element_cell = hash(key) % self.len

        if self.list[element_cell]:
            for i in range(self.len):
                if element_cell == self.len:
                    element_cell = 0

                element_cell += 1
                if not self.list[element_cell]:
                    break

        self.list[element_cell] = [key, hash(key), value]

    def __getitem__(self, key):
        for lst in self.list:
            if key in lst:
                return lst

    def __len__(self):
        len_dict = 0

        for value in self.list:
            if value:
                len_dict += 1
        return len_dict

    def resize(self):
        capacity = ceil((2 * self.len) / 3)

        if self.__len__() >= capacity:
            self.len *= 2
            new_list = self.list.copy()                # Save main list

            self.list = [[] for _ in range(self.len)]  # Change length main list

            for value in new_list:
                if value:                                          # Check value is not empty
                    if isinstance(value[0], int):
                        element_cell = value[0] % self.len
                    else:
                        element_cell = hash(value[0]) % self.len

                    if self.list[element_cell]:                    # If main list[index] not empty - get next index
                        if element_cell != self.len:
                            self.list[element_cell + 1] = value
                        else:
                            element_cell = 0
                            self.list[element_cell] = value
                    else:
                        self.list[element_cell] = value
