from typing import Any, Union


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
    def hash_func(self, key: Any) -> int:
        return hash(key) % self.capasity

    # пишемо основний функціонал, як вираховується місце елемента в таблиці,
    # як відбувається заповнення таблиці
    # проходить перевірка чи немає колізії(комірка зайнята іншим елементом)
    # чи заміна елемента якщо мають одинакові ключі
    def __setitem__(self, key: Any, value: Any) -> None:
        hash_key = hash(key)
        index_key = self.hash_func(key)
        self.resize(key, value)
        if self.size == 0:
            self.table[index_key].append((key, value, hash_key))
            self.size += 1
        else:
            for elem in range(len(self.table[index_key])):
                if self.table[index_key][elem][0] == key:
                    self.table[index_key][elem][1] = (key, value, hash_key)

            self.table[index_key + 1].append((key, value, hash_key))
            self.size += 1

    # прописуємо розширення таблиці при заповненні на 2/3
    def resize(self, key: Any, value: Any) -> None:
        if self.size >= self.overload:
            self.capasity *= 2

            self.table = [[] for _ in range(self.capasity)]
            self.__setitem__(key, value)

    # повернення значення при запиті по ключу, якщо такого ключа немає, викидає помилку
    def __getitem__(self, item: Union[int, float, str, object]) -> Any:
        index_key = self.hash_func(item)
        for key, value, hash_key in self.table[index_key]:
            if key == item:
                return value
        raise KeyError(f"Key '{item}' not found in the dictionary")

    # довжина таблиці із заповненими елементами
    def __len__(self) -> int:
        return self.size

    # видалення елемента по ключу
    def __delitem__(self, key: Any) -> None:
        del self.table[self.hash_func(key)]
        self.size -= 1

    # очистка таблиці до дефолтних значень
    def clear(self) -> None:
        self.capasity = 8
        self.table = [[] for _ in range(self.capasity)]


if __name__ == "__main__":
    dictionary = Dictionary()

    print(dictionary.table)
    print(dictionary.__len__())
    print(len(dictionary.table))

    dictionary.__setitem__(3, 2)
    print(dictionary.table)
    # print(dictionary.__len__())
    # print(len(dictionary.table))

    dictionary.__setitem__(11, 5)
    print(dictionary.table)
    # print(dictionary.__len__())
    # print(len(dictionary.table))

    dictionary.__setitem__(11, 6)
    print(dictionary.table)
    # print(dictionary.__len__())
    # print(len(dictionary.table))
