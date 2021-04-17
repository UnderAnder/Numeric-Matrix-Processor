def input_matrix():
    matrix = list()
    rows, cols = map(int, input().split())
    for row in range(rows):
        matrix.append(list(map(int, input().split())))
    return matrix


def matrix_sum(a: list[list[int]], b: list[list[int]]):
    if len(a) != len(b):
        return None
    matrix = list()
    for row_a, row_b in zip(a, b):
        row = list()
        for el_a, el_b in zip(row_a, row_b):
            row.append(el_a+el_b)
        matrix.append(row)
    return matrix


def print_matrix(matrix: list[list[int]]):
    if not matrix:
        print('ERROR')
        return False
    for i in matrix:
        print(' '.join(map(str, i)))


def main():
    print_matrix(matrix_sum(input_matrix(), input_matrix()))


if __name__ == '__main__':
    main()
