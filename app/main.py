class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.nodes = [[]] * 8

    def __setitem__(self, key: any, value: any) -> None:

        if self.__len__() >= self.capacity * 2 / 3:
            self.capacity *= 2
            old_nodes = self.nodes
            self.nodes = [[]] * self.capacity

            for node in old_nodes:
                if node:
                    if not self.nodes[node[2] % self.capacity]:
                        self.nodes[node[2] % self.capacity] = node
                    else:
                        for i in range(0, self.capacity):
                            if not self.nodes[i]:
                                self.nodes[i] = node
                                break

        node = self.nodes[hash(key) % self.capacity]
        if node:
            if not node[0] == key:
                for i in range(0, self.capacity):
                    if not self.nodes[i] or self.nodes[i][0] == key:
                        self.nodes[i] = [key, value, hash(key)]
                        break
            else:
                self.nodes[hash(key) % self.capacity] = [key, value, hash(key)]
        else:
            self.nodes[hash(key) % self.capacity] = [key, value, hash(key)]

    def __getitem__(self, key: any) -> any:
        node = self.nodes[hash(key) % self.capacity]
        if node:
            if node[0] != key:
                for i in range(0, self.capacity):
                    if self.nodes[i] and self.nodes[i][0] == key:
                        return self.nodes[i][1]
            return node[1]
        raise KeyError("There is no such key in the dictionary")

    def __len__(self) -> int:
        return len(self.nodes) - self.nodes.count([])

    def __delitem__(self, key: any) -> None:
        node = self.nodes[hash(key) % self.capacity]
        if node:
            if node[0] != key:
                for i in range(0, self.capacity):
                    if self.nodes[i] and self.nodes[i][0] == key:
                        self.nodes[i] = []

    def pop(self, key: any) -> any:
        res = self[key]
        self.__delitem__(key)
        return res

    def clear(self) -> None:
        self.capacity = 8
        self.nodes = [[]] * 8

    def get(self, key: any) -> any:
        try:
            self[key]
        except KeyError:
            return None
