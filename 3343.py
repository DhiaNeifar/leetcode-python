def countBalancedPermutations(self, num: str) -> int:
    num = [int(x) for x in num]
    total_sum = sum(num)
    if total_sum % 2 == 1:
        return 0
    half_sum = total_sum // 2
    half_length = len(num) // 2
    solutions = []

    def backtracking(index, local_solution, local_sum):
        if len(local_solution) == half_length:
            if local_sum == half_sum:
                solutions.append(list(local_solution))
            return
        if index >= len(num):
            return

        # Include num[index]
        local_solution.append(num[index])
        backtracking(index + 1, local_solution, local_sum + num[index])
        local_solution.pop()

        # Exclude num[index]
        backtracking(index + 1, local_solution, local_sum)

    backtracking(0, [], 0)

    solutions = [list(t) for t in set(tuple(sorted(sublist)) for sublist in solutions)]

    result = 0
    const = pow(10, 9) + 7

    def NumberPermutations(dictionary):
        def factorial(n):
            if n < 2:
                return 1
            return n * factorial(n - 1) % const

        denom = 1
        for count in dictionary.values():
            denom *= factorial(count)

        return factorial(sum(dictionary.values())) // denom

    num_counter = {}
    for number in num:
        num_counter[number] = num_counter.get(number, 0) + 1
    for solution in solutions:
        solution_counter = {}
        for number in solution:
            solution_counter[number] = solution_counter.get(number, 0) + 1
        rest_solution_counter = {}
        for key in num_counter:
            rest_solution_counter[key] = num_counter[key] - solution_counter.get(key, 0)

        result += NumberPermutations(solution_counter) * NumberPermutations(rest_solution_counter) % const

    return result



if __name__ == '__main__':
    num_ = "5353"
    output = countBalancedPermutations(None, num_)
    print(output)
