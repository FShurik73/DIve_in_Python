# ✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def fibonacci(x: int) :
    lst = [0, 1]
    while x > 0:
        yield lst[-1]
        lst.append(lst[-1] + lst[-2])
        x -= 1

for i in fibonacci(10):
    print(i, end=' ')