# 📌Объедините функции из прошлых задач. 
# 📌Функцию угадайку задекорируйте: ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и ○ декоратором для многократного запуска. 
# 📌Выберите верный порядок декораторов

from task9_4 import outer as counter
from task9_2 import decor as param_control_decor
from task9_3 import decor as json_decor 


@json_decor
@counter(2)
@param_control_decor
def guess_number(a:int, b:int):
        print(f'У тебя {b} попыток угадать число!')
        while b:
            guess = int(input('Введи число: '))
            if guess > a:
                print(f'Загаданное число меньше чем {guess}')
            elif guess < a:
                print(f'Загаданное число больше чем {guess}')
            else:
                print(f'Ты угадал! Загаданное число {a}!')
                return f'Угадал за {b} попыток! Загаданное число {a}'
            b -= 1
        
        print(f'Ты не угадал! Загаданное число {a}!')
        return f'Не угадал! Загаданное число {a}'
            

guess_number(321, 2)
