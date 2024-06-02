def main(points):
    points.sort(key=lambda x: x[0])
    max_ = 0
    for i in range(len(points) - 1):
        max_ = max(max_, points[i + 1][0] - points[i][0])
    return max_


if __name__ == '__main__':
    points_ = [[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]
    main(points_)
