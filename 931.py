def main(matrix):
    def min_falling_path_sum(position_, matrix_):
        if position_[0] == len(matrix) - 1:
            return matrix_[position_[0]][position_[1]]
        else:
            if position_[1] == 0:
                return matrix_[position_[0]][position_[1]] + min(
                    min_falling_path_sum((position_[0] + 1, position_[1]), matrix_),
                    min_falling_path_sum((position_[0] + 1, position_[1] + 1), matrix_))
            return matrix_[position_[0]][position_[1]] + min(
                min_falling_path_sum((position_[0] + 1, position_[1] - 1), matrix_),
                min_falling_path_sum((position_[0] + 1, position_[1]), matrix_),
                min_falling_path_sum((position_[0] + 1, position_[1] + 1), matrix_))

    if len(matrix) == 1:
        return matrix[0][0]
    _min = -100 * len(matrix)
    for j in range(len(matrix[0])):
        _min = min(_min, min_falling_path_sum((0, j), matrix))
    return _min


if __name__ == '__main__':
    _matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
    main(_matrix)
