# from functools import total_ordering

# @total_ordering
# class Rectangle:
#     '''
#     Класс прямоугольник
#     '''
#     def __init__(self, a: int, b: int):
#         self.a = a
#         self.b = b

#     def area(self):
#         return self.a * self.b

#     def perimetr(self):
#         return (self.a + self.b) * 2

    
#     def __add__(self, other):
#         ''' Сложение сторон прямоугольника и создание нового прямоугольника '''
#         if isinstance(other, Rectangle):
#             return Rectangle(self.a + other.a, self.b + other.b)
#         raise TypeError
    
#     def __sub__(self, other):
#         ''' Вычитание сторон прямоугольника и создание нового прямоугольника '''
#         if self.a > other.a and self.b > other.b:
#             return Rectangle(self.a - other.a, self.b - other.b)
    
#     def __eq__(self, other):
#         if isinstance(other, Rectangle):
#             return self.area() == other.area()
    
#     def __lt__(self, other):
#         if isinstance(other, Rectangle):
#             return self.area() < other.area()

#     def __str__(self) -> str:
#         return f'Прямоугольник со сторонами {self.a} и {self.b}'


# rect_1 = Rectangle(6, 15)
# rect_2 = Rectangle(5, 10)
# print(rect_1.perimetr()) 
# print(rect_1 - rect_2) 
# print(rect_1 + rect_2)
# print(rect_1 < rect_2)
# print(rect_1 == rect_2)
# print(rect_1 > rect_2)
# print(rect_1 != rect_2)
# print(rect_1 >= rect_2)
# print(rect_1 <= rect_2)


class Rectangle:
    
    def __init__(self, wight: float, height=None):
        self.wight = wight
        if height is None:
            self.height = wight
        if self.wight < 0:
            raise NegativeValueError(wight, height)
        self.wight = wight
        if self.height < 0:
            raise NegativeValueError(wight, height)
        self.height = height

    def perimeter(self):
        return (self.height + self.wight) * 2
    
    def area(self):
        return (self.height * self.wight)
    
    def __add__(self, other):
        per = self.perimeter() + other.perimeter()
        wight = self.wight + other.wight
        height = per / 2 - wight
        return Rectangle(wight, height)
    
    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        wight = abs(self.wight - other.wight)
        per = self.perimeter() - other.perimeter()
        height = per / 2 - wight
        return Rectangle(wight, height)
    
    def __lt__(self, other):
        return self.area() < other.area()
    
    def __eq__(self, other):
        return self.area() == other.area()
    
    def __le__(self, other):
        return self.area() <= other.area()
                        
    def __str__(self):
        return f"Прямоугольник со сторонами {self.wight} и {self.height}"  
    
    def __repr__(self):
       return f"Rectangle({self.wight}, {self.height})"
    
class NegativeValueError(Exception):
    def __init__(self, wigth, height):
        self.wigth = wigth
        self.height = height

    def __str__(self):
        if self.wigth < 0:
            return f"Ширина должна быть положительной, а не {self.wigth}"
        if self.height < 0:
            return f"Высота должна быть положительной, а не {self.height}"
        


rect = Rectangle(-2)
rect1 = Rectangle(4, 5)
rect2 = Rectangle(3, 3)

print(rect1)
print(rect2)

print(rect1.perimeter())
print(rect1.area())
print(rect2.perimeter())
print(rect2.area())

rect_sum = rect1 + rect2
rect_diff = rect1 - rect2

print(rect_sum)
print(rect_diff)

print(rect1 < rect2)
print(rect1 == rect2)
print(rect1 <= rect2)

print(repr(rect1))
print(repr(rect2))






