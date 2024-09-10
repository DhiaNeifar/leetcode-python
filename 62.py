def main(m, n):
    grid = [[1 for _ in range(m)] for _ in range(n)]
    for i in range(1, m):
        for j in range(1, n):
            grid[j][i] = grid[j][i - 1] + grid[j - 1][i]
    return grid[n - 1][m - 1]
    pass


# Works but Time Limit Exceeded
def main1(m, n):
    def backtrack(position):
        x, y = position
        if x < 0 or y < 0:
            return
        grid[y][x] += 1
        backtrack((x - 1, y))
        backtrack((x, y - 1))

    grid = [[0 for _ in range(m)] for _ in range(n)]
    backtrack((m - 1, n - 1))
    return grid[0][0]
    pass


if __name__ == '__main__':
    m_ = 7
    n_ = 3
    print(main(m_, n_))
