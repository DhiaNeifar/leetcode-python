import numpy as np

def knapsack(number_items, weights, prices, max_weight):
    table = np.zeros((number_items + 1, max_weight + 1), dtype=int)

    for i in range(1, number_items + 1):
        for j in range(1, max_weight + 1):
            if weights[i - 1] <= j:
                table[i, j] = max(table[i - 1, j], table[i - 1, j - weights[i - 1]] + prices[i - 1])
            else:
                table[i, j] = table[i - 1, j]

    print(table)
    print("Maximum value:", table[number_items, max_weight])

if __name__ == '__main__':
    number_items_ = 4
    weights_ = [2, 3, 4, 5]
    prices_ = [1, 2, 5, 6]
    max_weight_ = 8
    knapsack(number_items_, weights_, prices_, max_weight_)
