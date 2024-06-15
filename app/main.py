class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.size = 0
        self.dictionary = [-1] * self.capacity

    def hash_func(self, key: any) -> int:
        return hash(key) % self.capacity

    def resize_dict(self) -> None:
        self.capacity = self.capacity * 2
        temp_list = self.dictionary[:]
        self.dictionary = [-1] * self.capacity
        self.size = 0
        for item in temp_list:
            if item != -1:
                self.__setitem__(item[0], item[2])

    def __setitem__(self, key: any, value: any) -> None:
        if self.size + 1 > self.capacity * 2 / 3:
            self.resize_dict()
        hash_for_key = self.hash_func(key)

        if (self.dictionary[hash_for_key] == -1
                or self.dictionary[hash_for_key] == "deleted"):
            self.dictionary[hash_for_key] = [key, hash_for_key, value]
            self.size += 1
            return
        elif self.dictionary[hash_for_key][0] == key:
            self.dictionary[hash_for_key][2] = value
            return
        else:
            temp_counter = hash_for_key
            while ((self.dictionary[temp_counter] != -1
                    or self.dictionary[hash_for_key] == "deleted")
                   and self.dictionary[temp_counter][0] != key):
                temp_counter = (temp_counter + 1) % self.capacity

            if (self.dictionary[temp_counter] == -1
                    or self.dictionary[temp_counter] == "deleted"):
                self.dictionary[temp_counter] = [key, hash_for_key, value]
                self.size += 1
            else:
                self.dictionary[temp_counter][2] = value

    def __getitem__(self, item: any) -> any:
        hash_for_key = self.hash_func(item)
        if self.dictionary[hash_for_key] == -1:
            raise KeyError

        temp_counter = hash_for_key

        while ((self.dictionary[temp_counter] != -1
               or self.dictionary[temp_counter] != "deleted")
               and self.dictionary[temp_counter][0] != item):
            temp_counter = (temp_counter + 1) % self.capacity

        if (self.dictionary[temp_counter] == -1
                or self.dictionary[temp_counter] == "deleted"):
            raise KeyError
        return self.dictionary[temp_counter][2]

    def __delitem__(self, key: any) -> None:
        hash_for_key = self.hash_func(key)
        if self.dictionary[hash_for_key] == -1:
            raise KeyError

        temp_counter = hash_for_key
        while ((self.dictionary[temp_counter] != -1
               or self.dictionary[temp_counter] != "deleted")
               and self.dictionary[temp_counter][0] != key):
            temp_counter = (temp_counter + 1) % self.capacity

        if self.dictionary[temp_counter] == -1:
            raise KeyError

        self.dictionary[temp_counter] = "deleted"

    def clear(self) -> None:
        self.capacity = 8
        self.size = 0
        self.dictionary = [-1] * self.capacity

    def __len__(self) -> int:
        return self.size
