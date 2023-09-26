# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
# Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса

import csv
import datetime
import json
import os.path
from random import randint as ri
from typing import Callable


NUM1,NUM2 = -100, 100

def solve_quadr_equat_csv(func:Callable):
    generate_csv_file()

    def wrapper():
        with open('numbers.csv', "r", encoding='utf-8') as file:
            reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
            for row in reader:
                if row and row[0] != 0:
                    func(*row)
                
    return wrapper


def result_json(func: Callable):
    result = {}
    if os.path.exists('result_quadr_equat.json'):
        with open('result_quadr_equat.json', 'r', encoding='utf-8') as file:
            result = json.load(file)
    
    def wrapper(*args):
        roots = func(*args)
        result_dict = {'a': args[0], 'b': args[1], 'c': args[2], 'roots': roots}
        result_key = f'{datetime.datetime.now()}'[:-7]
        result[result_key] = result.get(result_key) + [result_dict] if result.get(result_key) else [result_dict]
        with open('result_quadr_equat.json', 'w', encoding='UTF-8') as file:
            json.dump(result, file)
        return roots
    
    return wrapper      


def generate_csv_file():
        with open('numbers.csv', "w", encoding='UTF-8') as file:
            writer = csv.writer(file)
            for _ in range(ri(100, 1000)):
                row = [ri(NUM1, NUM2) for _ in range(3)]
                writer.writerow(row)


@solve_quadr_equat_csv
@result_json
def quadr_equat(*args) -> float | None | tuple:
    a, b, c = args
    d = b ** 2 - 4 * a * c
    if d < 0:
        return None
    elif d == 0:
        x = -b / (2 * a)
        return round(x, 2)
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return round(x1, 2), round(x2, 2)

quadr_equat()

