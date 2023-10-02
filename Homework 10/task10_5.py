# 📌Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п. 
# 📌У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса. 
# 📌Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.

class Dog:
    def __init__(self, name, age, command = 'run'):
        self.name = name
        self.age = age
        self.command = command

    def show_info(self):
        return (f'{self.name} can {self.command}')
        

class Cat:
    def __init__(self, name, age, sleep_time = 10):
        self.name = name
        self.age = age
        self.sleep_time = sleep_time

    def show_info(self):
        return (f'{self.name} sleeps {self.sleep_time} hours')


class Bird:
    def __init__(self, name, age, volume):
        self.name = name
        self.age = age
        self.volume = volume

    def show_info(self):
        return (f'{self.name} sing {self.volume} dB')

pet_1 = Dog('Bars', 5)
pet_2 = Cat('Barsik', 5)
pet_3 = Bird('Chizik', 1, 3)

print(pet_1.show_info())
print(pet_2.show_info())
print(pet_3.show_info())