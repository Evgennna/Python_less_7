# 1. ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

from random import choices, randint
from string import ascii_letters, digits


def make_files(extension: str, min_name: int = 6, max_name: int = 30,
            min_size: int = 256, max_size: int = 4096, count: int = 42):
    for _ in range(count):
        name = ''.join(choices(ascii_letters+digits, k=randint(min_name, max_name)))
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        with open(f'{name}.{extension}', 'wb') as f:
            f.write(data)

# 2. ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

from make_files import make_files


def new_make_file(extensions: dict):
    for extension, count in extensions.items():
        make_files(extension=extension, count=count)


# 3. Напишите функцию группового переименования файлов. Она должна:
#* -- принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
#* -- принимать параметр количество цифр в порядковом номере.
#* -- принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
#* -- принимать параметр расширение конечного файла.
#* -- принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из
# исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os


def group_rename(desired_name, num_digits, source_ext, target_ext, name_range=None):
    # Получаем список всех файлов в текущем каталоге
    files = [f.split(source_ext)[0] for f in os.listdir('.')
             if os.path.isfile(f) and f.endswith(source_ext)]

    # Проверяем, что файлы присутствуют
    if not files:
        print("Файлы с заданным расширением не найдены.")
        return

    # Перебираем файлы и переименовываем их
    for i, file in enumerate(files, 1):
        # Извлекаем часть имени в соответствии с диапазоном
        if name_range:
            start, end = name_range
            base_name = file[start - 1:end]

        # Собираем новое имя файла
        new_name = base_name + desired_name + f"{i:0{num_digits}}" + target_ext

        # Переименовываем файл
        os.rename(f'{file}{source_ext}', new_name)
        print(f"Переименован файл {file} в {new_name}")


group_rename("_new", 6, ".txt", ".doc", name_range=[3, 6])