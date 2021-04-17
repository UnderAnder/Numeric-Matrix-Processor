class MatrixDimensionError(Exception):
    pass


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
        return Matrix([[other * j for j in i] for i in self.matrix])

    def __rmul__(self, other):
        return self.__mul__(other)

    def __str__(self):
        return '\n'.join([' '.join(map(str, i)) for i in self.matrix])

    def __input_matrix(self):
        rows, cols = map(int, input().split())
        return [[int(i) for i in input().split()] for _ in range(rows)]


def main():
    matrix = Matrix()
    scalar = int(input())
    print(matrix * scalar)

if __name__ == '__main__':
    main()
