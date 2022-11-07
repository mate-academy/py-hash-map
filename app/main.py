from copy import deepcopy
from dataclasses import dataclass
from typing import Any, Union


@dataclass
class Dictionary:
    def __init__(self) -> None:
        self.nodes = [[], [], [], [], [], [], [], []]

    def resize(self) -> None:
        temp = deepcopy(self.nodes)
        size = len(self.nodes)
        self.nodes = []
        for _ in range(2 * size):
            self.nodes.append([])
        for node in temp:
            for item in node:
                if item:
                    self.__write(item[0], item[1])

    def __setitem__(self,
                    key: Union[int, float, bool, str, tuple],
                    value: Any) -> None:
        if self.nodes.count([]) <= 1 / 3 * len(self.nodes):
            self.resize()
        self.__write(key, value)

    def __write(self,
                key: Union[int, float, bool, str, tuple],
                value: Any) -> None:
        write = True
        for item in self.nodes[hash(key) % len(self.nodes)]:
            if key in item:
                item[1] = value
                write = False
                break
        if write:
            self.nodes[hash(key) % len(self.nodes)].append([key, value])

    def __getitem__(self, key: Union[int, float, bool, str, tuple]) -> Any:
        for node in self.nodes[hash(key) % len(self.nodes)]:
            if key in node:
                return node[1]
        raise KeyError

    def __len__(self) -> int:
        result = 0
        for node in self.nodes:
            for item in node:
                if item:
                    result += 1
        return result

    def clear(self) -> None:
        self.nodes = []

    def __delitem__(self, key: Any) -> None:
        for node in self.nodes[hash(key) % len(self.nodes)]:
            if key in node:
                self.nodes[hash(key) % len(self.nodes)].remove(node)

    def get(self, key: Union[int, float, bool, str, tuple]) -> Any:
        for node in self.nodes[hash(key) % len(self.nodes)]:
            if key in node:
                return node[1]

    def pop(self, key: Union[int, float, bool, str, tuple]) -> Any:
        for node in self.nodes[hash(key) % len(self.nodes)]:
            if key in node:
                temp_value = deepcopy(node[1])
                self.nodes[hash(key) % len(self.nodes)].remove(node)
                return temp_value

    def update(self, other: Any) -> None:
        for node in other.nodes:
            for item in node:
                if item:
                    self.__setitem__(item[0], item[1])

    def __repr__(self) -> str:
        temp_lst = []
        for node in self.nodes:
            for item in node:
                if item:
                    temp_lst.append(f"{item[0]}: {item[1]}")
        result = ", ".join(it for it in temp_lst)
        return f"{{{result}}}"
