# Функция получает на вход текст вида: 
# “1-й четверг ноября”, “3я среда мая” и т.п. 
# 📌Преобразуйте его в дату в текущем году. 
# 📌Логируйте ошибки, если текст не соответсвует формату.

import datetime
import logging

# logger = logging.getLogger(__name__)
# my_format = '{levelname:<10} - {asctime:<20} - {funcName} - {msg}'
# logging.basicConfig(filename='mylog.log', filemode='a', encoding='UTF-8',
#                     level=logging.INFO, style='{', format=my_format)


# WEEKDAYS = {
#     'понедельник': 0,
#     'вторник': 1,
#     'среда': 2,
#     'четверг': 3,
#     'пятница': 4,
#     'суббота': 5,
#     'воскресенье': 6
# }

# MOUNTHS = {
#     'январь': 1,
#     'февраль': 2,
#     'март': 3,
#     'апрель': 4,
#     'май': 5,
#     'июнь': 6,
#     'июль': 7,
#     'август': 8,
#     'сентябрь': 9,
#     'октябрь': 10,
#     'ноябрь': 11,
#     'декабрь': 12
# }


# def func(data: str) -> datetime.date:
#     """
#     Функция получает на вход текст вида: “1-й четверг ноября”, “3я среда мая” и т.п.
#     Преобразует его в дату в текущем году.
#     """
#     cnt, weekday_, month_ = data.split(' ')
#     try:
#         cnt = int(cnt.split('-')[0])
#         if 0 < cnt < 6:
#             logger.error(msg='Не верный формат порядкового номера дня недели: {data}')
#     except ValueError as e:
#         logger.error(msg=e)
     

#     for k, v in WEEKDAYS.items():
#         if weekday_[:4] in k:
#             weekday_ = v
#             break
#     else:
#         logger.error(msg='Не верный формат дня недели: {data}')

#     for k, v in MOUNTHS.items():
#         if month_[:3]in k:
#             month_ = v
#             break
#     else:
#         logger.error(msg='Не верный формат месяца: {data}')    

#     cur_year = datetime.datetime.now().year

#     start = 1
#     for i in range(7):
#         first_month_weekday = datetime.date(year=cur_year, month=month_, day=start + i).weekday()
#         if first_month_weekday == weekday_:
#             day_ = first_month_weekday + (7 * (cnt - 1)) - 1
#             return datetime.date(year=cur_year, month=month_, day=day_)   
# print(func('5-й четверг июня'))  


# __________________________________________________________________________________


logger = logging.getLogger(__name__)
my_format = '{levelname:<10} - {asctime:<20} - {funcName} - {msg}'
logging.basicConfig(filename='mylog.log', filemode='a', encoding='UTF-8',
level=logging.INFO, style='{', format=my_format)

WEEKDAYS = {
'понедельник': 0,
'вторник': 1,
'среда': 2,
'четверг': 3,
'пятница': 4,
'суббота': 5,
'воскресенье': 6
}

MONTHS = {
'янв': 1,
'фев': 2,
'мар': 3,
'апр': 4,
'ма': 5,
'июн': 6,
'июл': 7,
'авг': 8,
'сен': 9,
'окт': 10,
'ноя': 11,
'дек': 12
}


def func(data: str) -> datetime.date:
    try:
        cnt, weekday_, month_ = data.split(' ')
    except Exception as e:
        logger.error(f'Неверный формат: {data}')

    try:
        cnt = int(cnt.split('-')[0])
        if 0 < cnt < 6:
            logger.error(msg=f'Неверный формат порядкового номера дня недели в месяце: {data}')
    except ValueError as e:
        logger.error(msg=e)

    for k, v in WEEKDAYS.items():
        if weekday_[:4] in k:
            weekday_ = v
            break
    else:
        logger.error(msg=f'Неверный формат дня недели: {data}')

    for k, v in MONTHS.items():
        if k in month_:
            month_ = v
            break
    else:
        logger.error(msg=f'Неверный формат месяца: {data}')

    cur_year = datetime.datetime.now().year

    first_month_weekday = datetime.date(year=cur_year, month=month_, day=1)
    offset = 1 if weekday_ < first_month_weekday.weekday() else 0

    for i in range(7):
        data_delta = first_month_weekday + datetime.timedelta(days=i)
        if data_delta.weekday() == weekday_:
            day_ = data_delta.replace(day=data_delta.day + (7 * (cnt - 1)))
    return day_


print(func('2-я среда мая'))