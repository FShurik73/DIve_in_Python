# 📌Создайте класс Сотрудник. 
# 📌Воспользуйтесь классом человека из прошлого задания. 
# 📌У сотрудника должен быть: ○ шестизначный идентификационный номер ○ уровень доступа вычисляемый 
# как остаток от деления суммы цифр id на семь

from task10_3 import Person

class Worker(Person):

    def __init__(self, id_number: str, first_name: str, last_name: str, age: int, second_name: str = None):
        super().__init__(first_name, last_name, age, second_name)
        self.id_number = id_number
        self.lvl = sum(list(map(int, id_number))) % 7

work_1 = Worker('965872', 'Петров', 'Петр', 36)
print(work_1.full_name())
print(work_1.id_number)
print(work_1.lvl)










