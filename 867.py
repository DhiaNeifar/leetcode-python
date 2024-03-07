def main(matrix):
    n = len(matrix)
    m = len(matrix[0])
    new_matrix = [[0 for _ in range(n)] for _ in range(m)]
    for j in range(m):
        for i in range(n):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix
