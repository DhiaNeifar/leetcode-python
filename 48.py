import numpy as np


def main(matrix):
    n = len(matrix)
    if n == 1:
        return matrix
    matrix = np.array(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i, j], matrix[j, i] = matrix[j, i], matrix[i, j]

    for i in range(n):
        for j in range(i, n):
            matrix[i, j], matrix[i, n - 1 - j] = matrix[i, n - 1 - j], matrix[i, j]

    print(matrix)


if __name__ == '__main__':
    _matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    main(_matrix)
