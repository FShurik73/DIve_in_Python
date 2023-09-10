# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление. 

def my_func(**kwargs) -> dict:
    res = {}
    for key, value in kwargs.items():
        try:
            res[value] = key
        except:
            res[str(value)] = key
    return res
        
print(my_func(a=1, b=2, c=3))











