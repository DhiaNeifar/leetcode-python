def main(grid):
    n = len(grid)
    generated = [[0 for _ in range(n - 2)] for _ in range(n - 2)]
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            local_max = 0
            for k in range(i - 1, i + 2):
                for l in range(j - 1, j + 2):
                    local_max = max(local_max, grid[k][l])
            generated[i - 1][j - 1] = local_max
    return generated
    pass


if __name__ == '__main__':
    grid_ = [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]
    print(main(grid_))
