# 📌Доработайте задачу 5. 
# 📌Вынесите общие свойства и методы классов в класс Животное. 
# 📌Остальные классы наследуйте от него. 
# 📌Убедитесь, что в созданные ранее классы внесены правки.

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


pet_1 = Dog('Bars', 5, 'Гав')
pet_2 = Cat('Barsik', 5, 'Мур')
pet_3 = Bird('Chizik', 1, 'Поет')

for pet in [pet_1, pet_2, pet_3]:
    print(f'{pet.name}', pet.get_spec())



