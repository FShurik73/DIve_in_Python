# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

from task_1 import checking_date

if __name__ == '__main__':
    my_date = input('Введите дату в формате DD.MM.YYYY: ')
    print('Дата соответствует стандарту' if checking_date(my_date) else 'Такой даты не может быть')