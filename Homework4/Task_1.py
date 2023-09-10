# Напишите функцию для транспонирования матрицы
import random

# создать матрицу n x m
def create_matrix(count_rows: int, count_columns: int) -> list[list]:
        new_matrix = []
        for _ in range(count_rows):
            row = []
            for _ in range(count_columns):
                row.append(random.randint(0, 9))
            new_matrix.append(row)
        return new_matrix

# печатать матрицу
def print_matrix(matrix):
    for row in matrix:
        for item in row:
            print(f'{item:>3}', end='\t')
        print()

# транспонировать матрицу

def transpose(matrix):
    return list(map(list, zip(*matrix)))

matrix = create_matrix(4, 5)
print_matrix(matrix)
print()
print(print_matrix(transpose(matrix)))