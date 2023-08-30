# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата. 

HEX_FACTOR = 16
hex_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']



enter = int(input('Input any integer number > 0: '))
num = enter
res: str = ''
while enter > 0:
    res = str(hex_data[enter % HEX_FACTOR]) + res
    enter //= HEX_FACTOR
print('Ox' + res)
  
print(hex(num))





