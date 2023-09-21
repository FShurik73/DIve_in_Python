# Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами

import os
from task7_1 import func
from task7_4 import create_files_with_extension
from task7_5 import create_dif_files
from task7_6 import create_dir
from task7_7 import group
from task7_3 import whatever 
from task7_2 import write_names_to_file
from task_1hw import group_rename_files

if __name__ == '__main__':
    func('task_1_file.txt', 8)
    write_names_to_file('task_2_file.txt', 10)
    whatever()
    create_files_with_extension('png')
    create_dif_files(txt = 4, bin = 2, png = 3, pdf = 3)
    create_dir('new')
    group(os.getcwd())
    group_rename_files("_fn_", ".txt", path="./Текст")






