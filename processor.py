from ast import literal_eval


class MatrixDimensionError(Exception):
    def __init__(self, message='The operation cannot be performed.'):
        self.message = message
        super().__init__(self.message)


class Matrix:
    def __init__(self, matrix=None):
        self.matrix = matrix if matrix else self.__input_matrix()
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise MatrixDimensionError
        else:
            result_matrix = list(map(lambda x, y: list(map(lambda i, j: i + j, x, y)), self.matrix, other.matrix))
            return Matrix(result_matrix)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Matrix([[other * j for j in i] for i in self.matrix])
        elif isinstance(other, Matrix):
            if self.cols != other.rows:
                raise MatrixDimensionError
            return Matrix(self.__multiply(other))
        else:
            raise TypeError

    def __rmul__(self, other):
        return self.__mul__(other)

    def __str__(self):
        return '\n'.join([' '.join(map(str, i)) for i in self.matrix])

    def __multiply(self, other):
        def __dot(col, row):
            return sum([i * j for i, j in zip(col, row)])
        rotated_other = [[*r][::1] for r in zip(*other.matrix)]
        return [[__dot(self.matrix[a], rotated_other[b]) for b in range(other.cols)] for a in range(self.rows)]

    @staticmethod
    def __input_matrix():
        rows, cols = map(int, input('Enter size of matrix: ').split())
        print('Enter matrix:')
        return [[literal_eval(i) for i in input().split()] for _ in range(rows)]


def menu():
    while True:
        print('1. Add matrices', '2. Multiply matrix by a constant', '3. Multiply matrices', '0. Exit', sep='\n')
        user_input = input('Your choice: ')
        if user_input == '0':
            exit()
        elif user_input == '1':
            print(Matrix() + Matrix())
        elif user_input == '2':
            print(Matrix() * literal_eval(input()))
        elif user_input == '3':
            print(Matrix() * Matrix())


if __name__ == '__main__':
    menu()
