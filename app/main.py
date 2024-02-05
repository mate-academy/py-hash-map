from typing import Hashable, Any


class Node:
    def __init__(self, key: Hashable, value: Any) -> None:
        self.key = key
        self.value = value
        self.next: None | Node = None


class Dictionary:
    def __init__(self) -> None:
        self.__length: int = 0
        self.__capacity: int = 8
        self.__data: list = [None] * self.__capacity
        self.__load_factor: float = 0.7

    def __hash(self, key: Hashable) -> int:
        return hash(key) % self.__capacity

    def __resize(self) -> None:
        new_capacity = self.__capacity * 2
        new_data = [None] * new_capacity

        for i in range(self.__capacity):
            current = self.__data[i]

            while current:
                key, value = current.key, current.value
                index = hash(key) % new_capacity

                if new_data[index] is None:
                    new_data[index] = Node(key, value)
                else:
                    new_node = Node(key, value)
                    new_node.next = new_data[index]
                    new_data[index] = new_node
                current = current.next

        self.__data = new_data
        self.__capacity = new_capacity

    def __setitem__(self, key: Hashable, value: Any) -> None:
        index = self.__hash(key)

        if self.__data[index] is None:
            self.__data[index] = Node(key, value)

        else:
            current = self.__data[index]

            while current:
                if key == current.key:
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next

            current.next = Node(key, value)

        self.__length += 1
        if (self.__length / self.__capacity) > self.__load_factor:
            self.__resize()

    def __getitem__(self, key: Hashable) -> Any:
        index = self.__hash(key)
        current = self.__data[index]

        while current:
            if key == current.key:
                return current.value

            current = current.next

        raise KeyError(f'Key "{key}" not found in the dictionary.')

    def __len__(self) -> int:
        return self.__length

    def clear(self) -> None:
        self.__length = 0
        self.__capacity = 8
        self.__data = [None] * self.__capacity

    def __delitem__(self, key: Hashable) -> None:
        index = self.__hash(key)
        current = self.__data[index]
        previous = None

        while current:
            if key == current.key:
                if previous is None:
                    self.__data[index] = current.next
                else:
                    previous.next = current.next

                self.__length -= 1
                return

            previous = current
            current = current.next

        raise KeyError(f'Key "{key}" not found in the dictionary.')

    def pop(self, key: Hashable) -> Any:
        try:
            value = self.__getitem__(key)
            self.__delitem__(key)
            return value
        except KeyError:
            raise KeyError(
                f'Key "{key}" not found in the dictionary.') from None

    def get(self, key: Hashable, default_value: Any = None) -> Any | None:
        try:
            return self.__getitem__(key)
        except KeyError:
            return default_value
