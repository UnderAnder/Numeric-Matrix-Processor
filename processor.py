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

    def transposition_main_diag(self):
        return Matrix([[row[i] for row in self.matrix] for i in range(self.rows)])

    def transposition_side_diag(self):
        return Matrix(list([*zip(*self.matrix[::-1])][::-1]))

    def transposition_vert_line(self):
        return Matrix([i[::-1] for i in self.matrix])

    def transposition_horz_line(self):
        return Matrix([i for i in self.matrix[::-1]])

    def determinant(self):
        if self.cols != self.rows:
            raise MatrixDimensionError
        return Matrix.__calc_determinant(self.matrix)

    def inverse(self):
        m = self.matrix
        if self.rows != self.cols:
            raise MatrixDimensionError
        if self.cols == 1:
            return 1 / m[0][0]
        elif self.rows == 2:
            det = self.determinant()
            if det == 0:
                raise MatrixDimensionError("The inverse matrix can’t be found, determinant is 0")
            return [[m[1][1] / det, -1 * m[0][1] / det], [-1 * m[1][0] / det, m[0][0] / det]]
        elif (det := self.determinant()) != 0:
            cofactors = [[(-1 if (x + y) % 2 else 1) * self.__calc_determinant(self.__minor(m, x, y))
                          for y in range(self.rows)] for x in range(self.rows)]
            cofactor_matrix = Matrix(cofactors).transposition_main_diag()
            return cofactor_matrix * (1 / det)
        else:
            return "This matrix doesn't have an inverse."

    @staticmethod
    def __minor(matrix, i, j):
        return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]

    @staticmethod
    def __calc_determinant(matrix):
        if len(matrix) == 1:
            return matrix[0][0]
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        determinant = 0
        for c in range(len(matrix)):
            determinant += ((-1) ** c) * matrix[0][c] * Matrix.__calc_determinant(Matrix.__minor(matrix, 0, c))
        return determinant

    @staticmethod
    def __input_matrix():
        rows, cols = map(int, input('Enter size of matrix: ').split())
        print('Enter matrix:')
        return [[literal_eval(i) for i in input().split()] for _ in range(rows)]


def transpose_menu():
    print('1. Main diagonal', '2. Side diagonal', '3. Vertical line', '4. Horizontal line', sep='\n')
    user_input = input('Your choice: ')
    if user_input == '1':
        print(Matrix().transposition_main_diag())
    elif user_input == '2':
        print(Matrix().transposition_side_diag())
    elif user_input == '3':
        print(Matrix().transposition_vert_line())
    elif user_input == '4':
        print(Matrix().transposition_horz_line())


def main_menu():
    msg = '1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n' \
          '4. Transpose matrix\n5. Calculate a determinant\n6. Inverse matrix\n0. Exit\nYour choice: '
    while (user_input := input(msg)) != '0':
        if user_input == '1':
            print(Matrix() + Matrix())
        elif user_input == '2':
            print(Matrix() * literal_eval(input()))
        elif user_input == '3':
            print(Matrix() * Matrix())
        elif user_input == '4':
            transpose_menu()
        elif user_input == '5':
            print(Matrix().determinant())
        elif user_input == '6':
            print(Matrix().inverse())


if __name__ == '__main__':
    main_menu()
