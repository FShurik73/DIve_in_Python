class Rectangle:
    
    def __init__(self, wight: float, height=None):
        if wight <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {wight}')
        self._wight = wight
        if height is None:
            self._height = wight
        else:
            if height <= 0:
                raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
            self.height = height

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise NegativeValueError(f'Высота должна быть положительной, а не {value}')    

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
   pass
        
if __name__ == '__main__':    
    r = Rectangle(4, 4) 
# r.height = -4