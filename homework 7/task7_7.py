# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

import os

DCT = { 'Видео': ('avi', 'mkv', 'mp4'), 
       'Изображения': ('jpg', 'jpeg', 'png', 'gif'),    
        'Текст': ('txt', 'doc', 'docx', 'pdf') }

def group(dir):
    files = [file for file in os.listdir() if os.path.isfile(file)]
    for fold, exts in DCT.items():
        if fold not in os.listdir():
            os.mkdir(fold)
        for file in files:
            if file.split('.')[1] in exts:
                os.replace(file, os.path.join(os.getcwd(), fold, file))


if __name__ == '__main__':
    group(os.getcwd())
