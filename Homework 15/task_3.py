# 📌Доработаем задачу 2. 
# 📌Сохраняйте в лог файл раздельно: ○ уровень логирования, ○ дату события,
# ○ имя функции (не декоратора), ○ аргументы вызова, ○ результат.

import logging
from functools import wraps
from typing import Callable

logger = logging.getLogger(__name__)
my_format = '{levelname:<10} - {asctime:<20} - {funcName} - {msg}'
logging.basicConfig(filename='mylog.log', filemode='a', encoding='UTF-8',
level=logging.INFO, style='{', format=my_format)


def decor(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        delimiter = ', ' if args and kwargs else ''
        args_kwargs = f'{delimiter}'.join([f'args: {args}' if args else '',
                    f'kwargs: {kwargs}' if kwargs else ''])

        logger.info(msg=f'result: {result}, {args_kwargs}')
        return result

    return wrapper


@decor
def some_func(a: str, b: str):
    return a + '_' + b


some_func('первая', 'вторая')
some_func('первая', b='вторая')
some_func(b='вторая', a='первая')

