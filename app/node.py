from typing import Any, Hashable
from dataclasses import dataclass


@dataclass
class Node:
    hash_: int
    key: Hashable
    value: Any
