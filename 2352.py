from typing import List

def equalPairs(self, grid: List[List[int]]) -> int:
    n = len(grid)
    result = 0
    for i in range(n):
        row = grid[i]
        for j in range(n):
            column = []
            for k in range(n):
                column.append(grid[k][j])
            if row == column:
                result += 1
    return result


if __name__ == "__main__":
    grid_ = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
    output = equalPairs(None, grid_)
    print(output)
