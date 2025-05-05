from typing import List

def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
    if n < 5:
        return 0
    buildings.sort(key=lambda x: x[0])
    i = 0
    x_min = buildings[0][0]
    x_max = buildings[-1][0]
    while i < len(buildings) and buildings[i][0] == x_min:
        i += 1
    if buildings[i][0] == x_max:
        return 0
    result = 0
    while i < len(buildings) and buildings[i][0] != x_max:
        x = buildings[i][0]
        y_min, y_max = buildings[i][1], buildings[i][1]
        min_copy, max_copy = 1, 1
        j = i + 1
        while j < len(buildings) and buildings[j][0] == x:
            y = buildings[j][1]
            if y == y_min:
                min_copy += 1
            if y == y_max:
                max_copy += 1
            if y < y_min:
                y_min = y
                min_copy = 1
            if y > y_max:
                y_max = y
                min_copy = 1
            j += 1
        result += max(0, j - i - min_copy - max_copy)
        i = j
    return result


if __name__ == '__main__':
    buildings_ = [[2,1],[2,3],[3,3],[2,2],[1,3]]
    output = countCoveredBuildings(None, len(buildings_), buildings_)
    print(output)

