# Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали. Превратите функции в методы класса, а параметры в свойства. 
# Задания должны решаться через вызов методов экземпляра.

from random import randint as RI

class Triangle:
  def __init__(self, a, b, c):
    if a < 0 or b < 0 or c < 0:
       raise ValueError('a, b, c не должны быть отрицательными')
    elif a < b + c and b < a + c and c < a + b:
        self.a = a
        self.b = b
        self.c = c

  def perimeter(self):
    return self.a + self.b + self.c

  def area(self):
    s = (self.a + self.b + self.c) / 2
    return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

triangle = Triangle(6, 7, 10)
print(triangle.perimeter())
print(triangle.area())




class Matrix:
    def __init__(self, m, n):
        self.m = m
        self.n = n

    def create_matrix(self):
        matrix = [[RI(0, 9) for _ in range(self.n)] for __ in range(self.m)]
        return matrix
        
matrix = Matrix(3, 4)    
for row in matrix.create_matrix():
    print(row)
