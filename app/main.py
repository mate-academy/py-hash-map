from typing import Any, Union, Hashable


class Dictionary:
    # визначаємо основні аргументи таблиці: розмір початкової табли, коеф. загруженості, розмір наповнення
    def __init__(
            self,
            capasity: int = 8,
            load_factor: float = 2 / 3,
            size: int = 0,
    ) -> None:
        self.load_factor = load_factor
        self.capasity = capasity
        self.size = size
        # створюємо дефолтну пусту таблицю
        self.table = [[] for _ in range(self.capasity)]
        self.overload = round(self.capasity * self.load_factor)

    # в цьому методі вираховуємо індекс елемента, за формулою, щоб не поіторювати цю формулу в інших методах
    def hash_func(self, key: Hashable) -> int:
        return hash(key) % self.capasity

    # пишемо основний функціонал, як вираховується місце елемента в таблиці,
    # як відбувається заповнення таблиці
    # проходить перевірка чи немає колізії(комірка зайнята іншим елементом)
    # чи заміна елемента якщо мають одинакові ключі
    def __setitem__(self, key: Hashable, value: Any) -> None:
        hash_key = hash(key)
        index_key = self.hash_func(key)
        if self.size >= self.overload:
            self.resize(key, value)
        while True:
            if self.table[index_key]:
                if self.table[index_key][0] == key:
                    self.table[index_key][1] = value
                    break
                index_key = (index_key + 1) % self.capasity
                self.table[index_key] = [key, value, hash_key]
                self.size += 1
            else:
                self.table[index_key] = [key, value, hash_key]
                self.size += 1

    # прописуємо розширення таблиці при заповненні на 2/3
    def resize(self, key: Hashable, value: Any) -> None:
        self.capasity *= 2
        new_table = [[] for _ in range(self.capasity)]

        for item in self.table:
            if item:
                self.__setitem__(key, value)

        self.table = new_table

    # повернення значення при запиті по ключу, якщо такого ключа немає, викидає помилку
    def __getitem__(self, key: Hashable) -> list:
        hash_key = hash(key)
        index_key = self.hash_func(key)
        while True:
            if not self.table[index_key]:
                raise KeyError(f"Key '{key}' not found in the dictionary")
            elif self.table[index_key][0] == key:
                return self.table[index_key][1]
            index_key = (index_key + 1) % self.capasity

    # довжина таблиці із заповненими елементами
    def __len__(self) -> int:
        return self.size

    # видалення елемента по ключу
    def __delitem__(self, key: Any) -> None:
        index_key = self.hash_func(key)
        if self.table[index_key][0] == key:
            del self.table[index_key]
            self.size -= 1

    # очистка таблиці до дефолтних значень
    def clear(self) -> None:
        self.capasity = 8
        self.table = []
        self.size = 0
