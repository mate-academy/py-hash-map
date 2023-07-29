from typing import Any


class Node:
    def __init__(
            self,
            key: Any,
            hash_custom: int,
            value: Any
    ) -> None:
        self.key = key
        self.hash = hash_custom
        self.value = value

    def __repr__(self) -> str:
        return f"{self.key}: {self.value}"
