# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.


from task7_4 import create_files_with_extension

# def gen_files(data: dict):
#     for key, value in data.items():
#         create_files_with_extension(key, num_files=value)

def create_dif_files(**kwargs):
    for ext, num in kwargs.items():
        create_files_with_extension(ext, num_files = num)

if __name__ == '__main__':  
    create_dif_files(txt = 4, bin = 2, png = 3, pdf = 3) 












