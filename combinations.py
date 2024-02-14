from itertools import combinations
def generate_combinations(n, k, combination=[], combinations=[]):
    # Base case: if the length of the combination is n, add it to the results
    if len(combination) == n:
        combinations.append(combination[:])  # Use a copy of the combination
        return

    # Recursive case: try all possible values for the next element
    for i in range(k):
        # Add the next value
        combination.append(i)

        # Recurse with the updated combination
        generate_combinations(n, k, combination, combinations)

        # Backtrack: remove the last element before the next iteration
        combination.pop()

    return combinations


# Example usage:
n = 4  # Dimension of the combinations
k = 3  # Range for each element in the combination
combinations = generate_combinations(n, k)
for combo in combinations:
    print(combo)
