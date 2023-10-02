# 📌Создайте класс прямоугольник. 
# 📌Класс должен принимать длину и ширину при создании экземпляра. 
# 📌У класса должно быть два метода, возвращающие периметр и площадь. 
# 📌Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.


class Rectangle:

    def __init__(self, side_a, side_b=None):
        self.length = side_a
        self.width = side_b if side_b else side_a

    def perimeter(self):
        return self.length * 2 + self.width * 2
        
    def square(self):
        return self.length * self.width 

rect = Rectangle(4, 5)
print(rect.perimeter())
print(rect.square())  
rect_1 = Rectangle(4)
print(rect_1.perimeter())
print(rect_1.square())









