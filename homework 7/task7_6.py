# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

from pathlib import Path
import os
from task7_5 import create_dif_files

def create_dir(name_dir: str):
    name = Path(Path.cwd() / name_dir)
    if not name.exists():
        name.mkdir()

    os.chdir(name)


if __name__ == '__main__':
    create_dif_files(txt = 3, bin = 2, png = 3, pdf = 4)
    create_dir('new')




