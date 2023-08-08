from typing import Any, Union


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

    def resize(self) -> None:
        self.initial_capacity *= 2
        self.threshold = round(self.load_factor * self.initial_capacity)
        self.current_len_of_dict = 0
        prev_hash_table = self.hash_table.copy()
        self.hash_table = [[] for i in range(self.initial_capacity)]

        for cell in prev_hash_table:
            if cell:
                for key, value, hash_k in cell:
                    # Обчислюю хеш введеного ключа
                    hash_key = hash(key)
                    # Обчислюю індекс комірки словника в яку записуватиму ключ-значення-хеш
                    index = hash_key % self.initial_capacity
                    self.hash_table[index].append((key, value, hash_key))
                    self.current_len_of_dict += 1

    # 6. Метод додавання пари ключ-значення-хеш до хеш-таблиці.
    def __setitem__(
            self,
            input_key: Union[int, float, str, object],
            input_value: Any
    ) -> None:
        """ x.__getitem__(y) <==> x[y] """
        # 7. Якщо поточний розмір словника менший порогу заповнення.
        if self.current_len_of_dict < self.threshold:
            # Обчислюю хеш введеного ключа
            hash_input_key = hash(input_key)
            # Обчислюю індекс комірки словника в яку записуватиму ключ-значення-хеш
            index = hash_input_key % self.initial_capacity
            # Якщо ж комірка словника не порожня
            if len(self.hash_table[index]) != 0:
                # для всіх відерець у комірці словника
                for i in range(len(self.hash_table[index])):
                    # якщо перше значення (нульове) у кортежі відерця (ключ) рівне введеному ключу
                    if list(self.hash_table[index][i])[0] == input_key:
                        # то значення відерця рівне введеному ключу, введеному значенню, хешу введеного ключа
                        self.hash_table[index][i] = input_key, input_value, hash_input_key
                        # Якщо знайшла у якомусь із відерець комірки з номером index ключ рівний введеному ключу, то припиняю пошук і виходжу з циклу
                        break
                #Якщо всі ключі у відерцях не рівні введеному ключу
                else:
                    # то просто додаю до порожньої комірки
                    self.hash_table[index].append(
                        # кортеж ключ-значення-хеш
                        (input_key, input_value, hash_input_key)
                    )
                    # далі збільшую довжину словника на одиницю
                    self.current_len_of_dict += 1
            # Якщо ж комірка словника порожня
            if len(self.hash_table[index]) == 0:
                # то просто додаю до порожньої комірки
                self.hash_table[index].append(
                    # кортеж ключ-значення-хеш
                    (input_key, input_value, hash_input_key)
                )
                # далі збільшую довжину словника на одиницю
                self.current_len_of_dict += 1

        # Якщо поточний розмір словника менший чи рівний порогу заповнення.
        else:
            # змінюю розмір словника(хеш-таблиці)
            self.resize()

    def __getitem__(self, input_key: Union[int, float, str, object]) -> Any:
        """ Set self[key] to value. """
        # Обчислюю хеш введеного ключа
        hash_input_key = hash(input_key)
        # Обчислюю індекс комірки словника в яку записуватиму ключ-значення-хеш
        index = hash_input_key % self.initial_capacity
        for key, value, hash_k in self.hash_table[index]:
            if key == input_key:
                return value
        raise KeyError("Dictionary missing key")

    def __len__(self) -> int:
        return self.current_len_of_dict

    def __delitem__(self, input_key: Union[int, float, str, object]) -> None:
        """ Delete self[key]. """
        # Обчислюю хеш введеного ключа
        hash_input_key = hash(input_key)
        # Обчислюю індекс комірки словника в яку записуватиму ключ-значення-хеш
        index = hash_input_key % self.initial_capacity
        for i in range(len(self.hash_table[index])):
            if list(self.hash_table[index][i])[0] == input_key:
                del self.hash_table[index][i]
                self.current_len_of_dict -= 1
                break

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

    dictionary.__setitem__(16, 16)
    print(dictionary.hash_table)
    print(dictionary.__len__())
    print(len(dictionary.hash_table))

    dictionary.__setitem__(32, 32)
    print(dictionary.hash_table)
    print(dictionary.__len__())
    print(len(dictionary.hash_table))

    dictionary.__setitem__(64, 64)
    print(dictionary.hash_table)
    print(dictionary.__len__())
    print(len(dictionary.hash_table))

    dictionary.__delitem__(16)
    print(dictionary.hash_table)
    print(dictionary.__len__())
    print(len(dictionary.hash_table))

    dictionary.__setitem__(2, 55)
    print(dictionary.hash_table)
    print(dictionary.__len__())
    print(len(dictionary.hash_table))

    dictionary.__delitem__(64)
    print(dictionary.hash_table)
    print(dictionary.__len__())
    print(len(dictionary.hash_table))
