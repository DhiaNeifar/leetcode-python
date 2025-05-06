from typing import List

def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    # Step 1: Create the 2D table
    num_vehicles = len(position)
    table = [[0 for _ in range(target + 1)] for _ in range(num_vehicles)]
    paired = list(zip(position, speed))
    paired.sort(reverse=True)
    position, speed = zip(*paired)

    # Step 2: Fill the 2D table
    for vehicle in range(num_vehicles):
        table[vehicle][0] = position[vehicle]

    for t in range(1, target + 1):
        # Treating the first vehicle
        table[0][t] = table[0][t - 1] + speed[0]
        for vehicle in range(1, num_vehicles):
            table[vehicle][t] = min(table[vehicle][t - 1] + speed[vehicle], table[vehicle - 1][t])

    # Step 4: Find the number of fleet
    fleet = 0
    i = 0
    print(table)
    for j in range(target + 1):
        if table[i][j] == target:
            fleet += 1
        while i < num_vehicles and table[i][j] == target:
            i += 1
    return fleet


if __name__ == '__main__':
    target_ = 12
    position_ = [10, 8, 0, 5, 3]
    speed_ = [2, 4, 1, 1, 3]
    output = carFleet(None, target_, position_, speed_)
    print(output)
