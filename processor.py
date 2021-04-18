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
        return [[sum([self.matrix[i][k] * other.matrix[k][j] for k in range(self.cols)])
                 for j in range(other.cols)] for i in range(self.rows)]

    @staticmethod
    def __input_matrix():
        rows, cols = map(int, input('Enter size of matrix: ').split())
        print('Enter matrix:')
        return [[literal_eval(i) for i in input().split()] for _ in range(rows)]

    def transposition_main_diag(self):
        return [[row[i] for row in self.matrix] for i in range(len(self.matrix))]

    def transposition_side_diag(self):
        self.matrix = [[*r][::-1] for r in zip(*self.matrix)]
        return self.transposition_horz_line()

    def transposition_vert_line(self):
        return [i[::-1] for i in self.matrix]

    def transposition_horz_line(self):
        return [i for i in self.matrix[::-1]]


def transpose_menu():
    print('1. Main diagonal', '2. Side diagonal', '3. Vertical line', '4. Horizontal line', sep='\n')
    user_input = input('Your choice: ')
    if user_input == '1':
        print(Matrix(Matrix().transposition_main_diag()))
    elif user_input == '2':
        print(Matrix(Matrix().transposition_side_diag()))
    elif user_input == '3':
        print(Matrix(Matrix().transposition_vert_line()))
    elif user_input == '4':
        print(Matrix(Matrix().transposition_horz_line()))


def main_menu():
    msg = '1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n' \
          '4. Transpose matrix\n0. Exit\nYour choice: '
    while (user_input := input(msg)) != '0':
        if user_input == '1':
            print(Matrix() + Matrix())
        elif user_input == '2':
            print(Matrix() * literal_eval(input()))
        elif user_input == '3':
            print(Matrix() * Matrix())
        elif user_input == '4':
            transpose_menu()


if __name__ == '__main__':
    main_menu()
