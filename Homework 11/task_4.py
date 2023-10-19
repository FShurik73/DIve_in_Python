class Matrix:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]


    def __add__(self, other):  
        if isinstance(other, Matrix):
            if all((self.rows == other.rows,
                    self.cols == other.cols)):
                new_matrix = Matrix(self.rows, self.cols)
                new_matrix.data = self.data
                for i in range(self.rows):
                    for j in range(self.cols):
                        new_matrix.data[i][j] += other.data[i][j]
                return new_matrix
            else:
                raise AttributeError('Матрицы должны быть одинаковой размерности')
        else:
            raise AttributeError('Складывать матрицу можно только с матрицей')


    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.cols == other.rows:
                new_matrix = Matrix(self.rows, other.cols)
                for i in range(new_matrix.rows):
                    for j in range(self.cols):
                        for k in range(other.rows):
                            new_matrix.data[i][j] += self.data[i][k] * other.data[k][j]

                return new_matrix
            else:
                raise AttributeError('Матрицы должны быть согласованными')

        elif isinstance(other, int):
            new_matrix = Matrix(self.rows, self.cols)
            new_matrix.data = self.data
            for i in range(self.rows):
                for j in range(self.cols):
                    new_matrix.data[i][j] *= other

            return new_matrix

        else:
            raise ValueError('Умножать матрицу можно только на другую матрицу, либо целое число')

    def __eq__(self, other):
        if isinstance(other, Matrix):
            if all((self.rows == other.cols,
                    self.cols == other.rows)):
                for i in range(self.rows):
                    for j in range(self.cols):
                        if self.data[i][j] == other.data[i][j]:
                            return True
                    else:
                        return False
            else:
                return False
        else:
            return False
        
    def __str__(self):
        return '\n'.join([' '.join([str(i) for i in row]) for
                        row in self.data])
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.rows},{self.cols})"
        
matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]] 

matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]

print(matrix1)
print(matrix2)

print(matrix1 == matrix2)

matrix_sum = matrix1 + matrix2
print(matrix_sum)

matrix3 = Matrix(3, 2)
matrix3.data = [[1, 2], [3, 4], [5, 6]]

matrix4 = Matrix(2, 2)
matrix4.data = [[7, 8], [9, 10]]

result = matrix3 * matrix4
print(result)