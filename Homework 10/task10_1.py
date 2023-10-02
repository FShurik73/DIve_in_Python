# 📌Создайте класс окружность. 
# 📌Класс должен принимать радиус окружности при создании экземпляра. 
# 📌У класса должно быть два метода, возвращающие длину окружности и её площадь.
from math import pi


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def length_c(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * self.radius ** 2

circ_1 = Circle(5)
print(circ_1.length_c())
print(circ_1.area())





 