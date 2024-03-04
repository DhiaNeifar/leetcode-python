def main(matrix):
    n = len(matrix)
    for i in range(1, n):
        for j in range(n):
            first_index = max(0, j - 1)
            min_value = matrix[i - 1][first_index]
            for t in range(first_index + 1, min(j + 2, n)):
                min_value = min(min_value, matrix[i - 1][t])
            matrix[i][j] += min_value
    return min(matrix[n - 1])


if __name__ == '__main__':
    _matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
    main(_matrix)
