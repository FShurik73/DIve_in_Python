# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

from random import randint

max_weight = int(input('Введите грузоподъемность рюкзака:>  '))
things = ['палатка', 'удочка', 'котелок', 'лодка', 'мангал', 'гитара', 'пила', 'чайник', 'ложка', 'вилка', 'спальник', 'топор']

def variants_generator(thigs: list) -> dict:
    result_dict = {}    
    for thig in thigs:
        result_dict[thig] = randint(1, 6)
    return result_dict

items = variants_generator(things)
print(items)

 
current_weight = 0 
backpack = {} 

for item, weight in items.items():
    if current_weight + weight <= max_weight:
        backpack[item] = weight
        current_weight += weight
        
print(f'В рюкзак вместительностью {max_weight} кг вошли следующие вещи:')
for item, weight in backpack.items():
    print(f'- {item} - {weight} кг')
