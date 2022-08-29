class Dictionary:

    def __init__(self):
        self.capacity = 8
        self.threshold = int(self.capacity * (2 / 3))
        self.length = 0
        self.base_data = [None for i in range(self.capacity)]

    def __setitem__(self, key, value):

        if self.length >= self.threshold:
            self.resize()
        hash_ = hash(key)
        index_ = int(hash_ % self.capacity)

        while self.base_data[index_] is not None:

            if self.base_data[index_][1] == hash_ and\
                    self.base_data[index_][0] == key:
                self.base_data[index_] = [key, hash_, value]
                self.length -= 1
                break
            index_ = (index_ + 1) % self.capacity

        self.base_data[index_] = [key, hash_, value]
        self.length += 1

    def __getitem__(self, key):
        hash_ = hash(key)
        index_ = hash_ % self.capacity
        while self.base_data[index_] is not None:
            if self.base_data[index_][0] == key and \
                    self.base_data[index_][1] == hash_:
                return self.base_data[index_][2]

            index_ = (index_ + 1) % self.capacity

        raise KeyError(f"Not Key {key} ")

    def __len__(self):
        return self.length

    def resize(self):
        self.capacity *= 2
        self.threshold = int(self.capacity * (2 / 3))
        data_ = []
        for member in self.base_data:
            if member is not None:
                data_.append(member)
        self.base_data = [
            None for _ in range(self.capacity)]
        self.length = 0
        for member in data_:
            self.__setitem__(member[0], member[2])

    def clear(self):
        self.init()

    def __delitem__(self, item):
        i = hash(item) % self.capacity
        while self.base_data[i] is not None:
            if self.base_data[i][0] == item:
                self.base_data[i] = None
            i = (i + 1) % self.capacity

    def pop(self, key):
        self.delitem(key)

    def get(self, key):
        self.getitem(key)
        return None

    def update(self, **kwargs):
        for member in kwargs:
            member.setitem()
        return self.base_data

    def __iter__(self):
        if self.length != 0:
            counter = 0
            while counter <= self.length:
                yield self.base_data[counter]


if __name__ == "__main__":
    pass
