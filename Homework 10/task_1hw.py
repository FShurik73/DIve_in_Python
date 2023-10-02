# Доработаем задания 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики. 



class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.spec = None

    def get_spec(self):
        return self.spec


class Dog(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec
        

class Cat(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec


class Bird(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec

class Fabric:

    def __init__(self, animal_type: str, *args):
        self._animal_type = animal_type
        self.args = args

    def make_animal(self):
        if self._animal_type == 'Dog':
            return Dog(*self.args)
        elif self._animal_type == 'Cat':
            return Cat(*self.args)
        elif self._animal_type == 'Bird':
            return Bird(*self.args)
        else:
            raise ValueError

if __name__ == '__main__':
    fabric = Fabric('Cat', 'Barsik', 5, 'мур-мур')
    fabric.make_animal()
    