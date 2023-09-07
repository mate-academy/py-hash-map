class Node:
    def __init__(self, key: int or float, value: int or float) -> None:
        self.key = key
        self.value = value
        self.next = None


class Dictionary:
    def __init__(
            self,
            initial_capacity: int = 16,
            load_factor: float = 0.75
    ) -> None:
        # Initialized capacity and load factor to be initialized
        self.initial_capacity = initial_capacity
        self.load_factor = load_factor
        self.size = 0  # Current dictionary size
        self.capacity = initial_capacity
        self.table = [None] * initial_capacity  # Hash table

    def __hash_func(self, key: int or float) -> int:
        # Hash function to calculate the index in the hash table
        return hash(key) % self.capacity

    def __resize(self) -> None:
        # Dictionary resizing on overflow
        self.capacity *= 2
        new_table = [None] * self.capacity
        for node in self.table:
            while node:
                index = self.__hash_func(node.key)
                next_node = node.next
                node.next = new_table[index]
                new_table[index] = node
                node = next_node
        self.table = new_table

    def __setitem__(
            self,
            key: int or float or None,
            value: int or float or None
    ) -> int or None:
        # Adding an element to the dictionary
        index = self.__hash_func(key)
        new_node = Node(key, value)
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value  # If the key already exists
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = new_node
        self.size += 1

        # Load factor check and resize
        if self.size > self.capacity * self.load_factor:
            self.__resize()

    def __getitem__(self, key: int or float) -> int or float:
        # Get value by key
        index = self.__hash_func(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError(key)

    def __len__(self) -> int:
        # Get current dictionary size
        return self.size
