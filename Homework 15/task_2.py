# 📌На семинаре про декораторы был создан логирующий декоратор. 
# Он сохранял аргументы функции и результат её работы в файл. 
# 📌Напишите аналогичный декоратор, но внутри используйте модуль logging.

import logging

from typing import Callable
from functools import wraps

def decor(func: Callable) -> Callable:
    logger = logging.getLogger(__name__)
    my_format = '{msg}'
    logging.basicConfig(filename='mylog.log', filemode='a', encoding='UTF-8',
                        level=logging.INFO, style='{', format=my_format) 
    
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        
        result = func(*args, **kwargs)
        str_args, str_kwargs = '', ''
        if args:
            str_args = 'args: ' + ', '.join(args)
        if kwargs:
            str_kwargs = 'kwargs: ' + ', '.join([f"{key}={value}" for key, value in kwargs.items()])
        logger.info(msg=f'result: {result}, {str_args}' + (', ' if str_args and str_kwargs else '') + f'{str_kwargs}')
        
        return result
    
    return wrapper

@decor
def some_func(a:str, b: str):
    return a + '_' + b

some_func('первая', 'вторая')
some_func('первая', b='вторая')
some_func(a='первая', b='вторая')       