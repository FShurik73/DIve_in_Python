# ✔ Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

import os
import random
import string


def create_files_with_extension(extension: str, min_name_length = 6, max_name_length = 30, min_file_size = 256, max_file_size = 4096, num_files = 1):
    for i in range(num_files):
        name_length = random.randint(min_name_length, max_name_length)
        file_name = ''.join(random.choices(string.ascii_letters + string.digits, k=name_length)) + '.' + extension
        file_size = random.randint(min_file_size, max_file_size)
        random_bytes = os.urandom(file_size)

        with open(file_name, 'wb') as file:
            file.write(random_bytes) 

create_files_with_extension('png')











