# 📌Изменяем класс прямоугольника. 
# 📌Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.

class Value:
    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)
    
    def __set__(self, instance, value):
        setattr(instance, self.param_name, self._validate(value))

    def _validate(self, value: int):
        if not (self.min_value < value < self.max_value):
            raise ValueError
        return value
    
class Rectangle:
    # __slots__ = ['width', 'height']
    width = Value(10, 100)
    height = Value(10, 100)
     
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

a = Rectangle(11, 12)

print(a.area)
# a.color = 'Green'
# print(a.__dict__)
        









