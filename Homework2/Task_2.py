# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение дробей. 
# Для проверки своего кода используйте модуль fractions.

import fractions

str1 = str(input('Введите дробь вида x/x : '))
str2 = str(input('Введите еще одну дробь вида x/x : '))
fract1 = str1.split('/')
fract2 = str2.split('/')
summa = str(int(fract1[0]) * int(fract2[1]) + int(fract1[1]) * int(fract2[0])) + '/' + str(int(fract2[1]) * int(fract1[1]))
mult = str(int(fract1[0]) * int(fract2[0])) + '/' + str(int(fract1[1]) * int(fract2[1]))
print(f'Сумма {summa}, Произведение {mult}')
f1 = fractions.Fraction(int(fract1[0]), int(fract1[1]))
f2 = fractions.Fraction(int(fract2[0]), int(fract2[1]))
print(f'Проверка с помощью функции -  сумма {f1+f2}, произведение {f1*f2}')

