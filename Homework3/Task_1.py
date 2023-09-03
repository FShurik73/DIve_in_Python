# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами. Код должен расширяться
# на любое большее количество друзей

from random import randint


def variants_generator(thigs: list, freinds: list) -> dict:
    result_dict = {}
    index_men = 0

    while len(result_dict) != len(freinds):
        man_things = []
        for i in range(3):
            man_things.append(thigs[randint(0, len(thigs)-1)])
        result_dict[freinds[index_men]] = tuple(man_things)
        index_men += 1

    for name in result_dict.keys():
        result_dict[name] = set(result_dict[name])

    return result_dict


def result_1(freinds: dict) -> str:
    kase = set()
    flag = True
    for i in freinds.values():
        if flag:
            kase = i
            flag = False
        elif len(kase) <= 0:
            kase.clear()
        else:
            kase &= i
    if len(kase):
        return f'Вещь {kase} - взяли все друзья'
    else:
        return 'Нет общих вещей'


def result_2(freinds: dict) -> str:
    result = []
    count = 0

    for name in freinds.keys():
        freinds2 = freinds.copy()
        kids = freinds.get(name)
        res = 0
        for i in freinds2.keys():
            x = freinds2.get(i)
            if i == name:
                 continue
            else:
                print(count, x)
                count += 1
                res = kids - x
        if len(res) != 0:
            result.append(str(f'Только у {name} есть {res}'))
    print(result)


things = ['палатка', 'удочка', 'котелок', 'лодка', 'мангал', 'гитара', 'пила', 'чайник', 'ложка', 'вилка', 'спальник', 'топор']
freinds_list = ['Ваня', 'Саша', 'Петя']

freinds = variants_generator(things, freinds_list)
print(freinds)
print(result_1(freinds.copy()))
result_2(freinds.copy())
















