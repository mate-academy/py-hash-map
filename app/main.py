from typing import Any, Union
from app.point import Point


class Dictionary:
    def __init__(self) -> None:
        # 1. Поточний розмір словника рівний нулю.
        self.current_len_of_dict = 0
        # 2. Початкова ємність словника рівна восьми
        # (виділено вісім комірок для запису даних у словник).
        self.initial_capacity = 8
        # 3. Коефіцієнт заповнення словника рівний двом третім.
        self.load_factor = 2 / 3
        # 4. Поріг заповнення словника рівний добутку коефіцієнту
        # заповнення та початкової ємності.
        self.threshold = round(self.load_factor * self.initial_capacity)
        # 5. Хеш-таблиця рівна порожнім спискам у кількості рівній
        # початковій ємності.
        self.hash_table = [[] for i in range(self.initial_capacity)]

    # 6. Метод додавання пари ключ-значення до хеш-таблиці.
    def resize(self) -> None:
        self.initial_capacity *= 2
        self.threshold = round(self.load_factor * self.initial_capacity)
        self.current_len_of_dict = self.current_len_of_dict
        prev_hash_table = self.hash_table.copy()
        self.hash_table = [[] for i in range(self.initial_capacity)]
        for cell in prev_hash_table:
            if cell is not None:
                for key, value, hash_k in cell:
                    hash_key = hash(key)
                    new_index = hash_key % self.initial_capacity
                    self.hash_table[new_index] = [(key, value, hash_key)]

    def __setitem__(
            self,
            input_key: Union[int, float, str, object],
            input_value: Any
    ) -> None:
        """ x.__getitem__(y) <==> x[y] """
        # 7. Якщо поточний розмір словника менший чи рівний порогу заповнення.
        if self.current_len_of_dict < self.threshold:

            hash_input_key = hash(input_key)
            index = hash_input_key % self.initial_capacity
            self.hash_table[index].append(
                (input_key, input_value, hash_input_key)
            )
            self.current_len_of_dict += 1

        elif self.current_len_of_dict >= self.threshold:
            self.resize()

    def __getitem__(self, input_key: Union[int, float, str, object]) -> Any:
        """ Set self[key] to value. """
        hash_key = hash(input_key)
        index = hash_key % self.initial_capacity
        for key, value, hash_k in self.hash_table[index]:
            if key == input_key:
                return value
            raise KeyError("Dictionary missing key")

    def __len__(self) -> int:
        return self.current_len_of_dict

    def __delitem__(self, input_key: Union[int, float, str, object]) -> None:
        """ Delete self[key]. """
        hash_key = hash(input_key)
        index = hash_key % self.initial_capacity
        self.hash_table[index] = []
        self.current_len_of_dict -= 1

    def clear(self) -> None:
        # 1. Поточний розмір словника рівний нулю.
        self.current_len_of_dict = 0
        # 2. Початкова ємність словника рівна восьми
        # (виділено вісім комірок для запису даних у словник).
        self.initial_capacity = 8

        # 5. Хеш-таблиця рівна порожнім спискам у кількості
        # рівній початковій ємності.
        self.hash_table = [[] for i in range(self.initial_capacity)]


if __name__ == "__main__":
    dictionary = Dictionary()

    print(dictionary.hash_table)
    print(dictionary.__len__())
    print(len(dictionary.hash_table))

    dictionary.__setitem__("ioi", 23)
    print(dictionary.hash_table)
    print(dictionary.__len__())
    print(len(dictionary.hash_table))

    dictionary.__setitem__(1, 55)
    print(dictionary.hash_table)
    print(dictionary.__len__())
    print(len(dictionary.hash_table))

    dictionary.__setitem__("ioi", 30)
    print(dictionary.hash_table)
    print(dictionary.__len__())
    print(len(dictionary.hash_table))

    dictionary.__setitem__(Point(0, 0), "origin")
    print(dictionary.hash_table)
    print(dictionary.__len__())
    print(len(dictionary.hash_table))

    dictionary.__setitem__(2.8, "origin")
    print(dictionary.hash_table)
    print(dictionary.__len__())
    print(len(dictionary.hash_table))

    dictionary.__setitem__(Point(2, 0), "2origin")
    print(dictionary.hash_table)
    print(dictionary.__len__())
    print(len(dictionary.hash_table))

    dictionary.__setitem__("ioi", 30)
    print(dictionary.hash_table)
    print(dictionary.__len__())
    print(len(dictionary.hash_table))

    dictionary.__delitem__("ioi")
    print(dictionary.hash_table)
    print(dictionary.__len__())
    print(len(dictionary.hash_table))

    print(dictionary.__getitem__(2.8))

    dictionary.clear()
    print(dictionary.hash_table)
    print(dictionary.__len__())
    print(len(dictionary.hash_table))
