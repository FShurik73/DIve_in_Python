# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов. 

import random

first_list = [random.randint(1,11) for i in range(15)]
result_list = []

for number in first_list:
    if first_list.count(number) >= 2 and number not in result_list:
        result_list.append(number)

print(f'{first_list = }\n{result_list =}')