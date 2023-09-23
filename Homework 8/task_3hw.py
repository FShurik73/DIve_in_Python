# Соберите из созданных на уроке и в рамках домашнего задания функций
# пакет для работы с файлами разных форматов.

from task8_2 import create_users
from task8_4 import export_csv_to_json
from task8_6 import create_csv_table
from task8_5 import json_to_pickle
from task_2hw import inspect_folder
from task_1hw import convert_csv

if __name__ == '__main__':
    create_users()
    export_csv_to_json('user_db.csv', 'new_user_db.json')
    create_csv_table()
    json_to_pickle()
    inspect_folder()
    convert_csv()