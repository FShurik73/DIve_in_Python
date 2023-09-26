# 📌Дорабатываем задачу 1. 
# 📌Превратите внешнюю функцию в декоратор. 
# 📌Он должен проверять входят ли переданные в функцию угадайку числа в диапазоны [1, 100] и [1, 10]. 
# 📌Если не входят, вызывать функцию со случайными числами из диапазонов.

from typing import Callable
import random as rnd
from functools import wraps



def decor(func:Callable):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        a, b, *_ = args
        if a not in range(1, 101):
            print(f'Введенное число {a} не входит в диапазон [1, 100]'
                  f'Будем играть по моим правилам!')
            a = rnd.randint(1, 100)
        if b not in range(1, 11):
            print(f'Введенное число {b} не входит в диапазон [1, 10]'
                  f'Будем играть по моим правилам!')
            b = rnd.randint(1, 10)
        return func(a, b)

    return wrapper


@decor
def inner(a:int, b:int):
        print(f'У тебя {b} попыток угадать число!')
        while b:
            guess = int(input('Введи число: '))
            if guess > a:
                print(f'Загаданное число меньше чем {guess}')
            elif guess < a:
                print(f'Загаданное число больше чем {guess}')
            else:
                print(f'Ты угадал! Загаданное число {a}!')
                break
            b -= 1
        else:
            print(f'Ты не угадал! Загаданное число {a}!')

inner(202, 6)
















