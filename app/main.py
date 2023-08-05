from typing import Any, Optional, List, Tuple


class Node:
    def __init__(self, key: Any, value: Any) -> Any:
        self.key = key
        self.value = value
        self.next: Optional[Node] = None


class Dictionary:
    def __init__(
            self,
            initial_capacity: int = 10,
            load_factor: float = 0.75
    ) -> None:
        self._capacity: int = initial_capacity
        self._load_factor: float = load_factor
        self._size: int = 0
        self._table: List[Optional[Node]] = [None] * self._capacity

    def __setitem__(self, key: Any, value: Any) -> None:
        hash_code: int = self._get_hash_code(key)
        index: int = hash_code % self._capacity

        new_node: Node = Node(key, value)

        if self._table[index] is None:
            self._table[index] = new_node
        else:
            current: Node = self._table[index]
            prev: Optional[Node] = None
            while current is not None:
                if current.key == key:
                    current.value = value
                    return
                prev = current
                current = current.next
            prev.next = new_node

        self._size += 1
        if self._size >= self._capacity * self._load_factor:
            self._resize_table()

    def __getitem__(self, key: Any) -> Any:
        hash_code: int = self._get_hash_code(key)
        index: int = hash_code % self._capacity

        current: Optional[Node] = self._table[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next

        raise KeyError(f"Key '{key}' not found.")

    def __len__(self) -> int:
        return self._size

    def __delitem__(self, key: Any) -> None:
        hash_code: int = self._get_hash_code(key)
        index: int = hash_code % self._capacity

        prev: Optional[Node] = None
        current: Optional[Node] = self._table[index]
        while current is not None:
            if current.key == key:
                if prev is None:
                    self._table[index] = current.next
                else:
                    prev.next = current.next
                self._size -= 1
                return
            prev = current
            current = current.next

        raise KeyError(f"Key '{key}' not found.")

    def _get_hash_code(self, key: Any) -> int:
        return hash(key)

    def _resize_table(self) -> None:
        new_capacity: int = self._capacity * 2
        new_table: List[Optional[Node]] = [None] * new_capacity

        for i in range(self._capacity):
            current: Optional[Node] = self._table[i]
            while current is not None:
                new_index: int = current.key.__hash__() % new_capacity
                new_node: Node = Node(current.key, current.value)

                if new_table[new_index] is None:
                    new_table[new_index] = new_node
                else:
                    temp: Node = new_table[new_index]
                    while temp.next is not None:
                        temp = temp.next
                    temp.next = new_node

                current = current.next

        self._table = new_table
        self._capacity = new_capacity

    def __repr__(self) -> str:
        items: List[Tuple[Any, Any]] = []
        for i in range(self._capacity):
            current: Optional[Node] = self._table[i]
            while current is not None:
                items.append((current.key, current.value))
                current = current.next
        return f"Dictionary({', '.join([f'{k}: {v}' for k, v in items])})"
