# 📌Создайте декоратор с параметром. 
# 📌Параметр - целое число, количество запусков декорируемой функции.

from typing import Callable
from functools import wraps


def outer(count:int):

    def decor(func:Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = []
            for _ in range(count):
                res.append(func(*args, **kwargs))
            return res
        
        return wrapper
    
    return decor

@outer(5)
def some_func(a:str, b: str):
    return a +'_'+ b

print(some_func('Первая', 'Вторая'))


