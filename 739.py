def main(temperatures):
    # Optimal version Does not work yet!
    output = [0 for _ in range(len(temperatures))]
    i = 0
    while i < len(temperatures) - 1:
        j = i + 1
        while j < len(temperatures) and temperatures[j] <= temperatures[i]:
            j += 1
        if j < len(temperatures):
            while i != j:
                output[i] = j - i
                i += 1
    print(output)
    return output


def main1(temperatures):
    # Naive Version
    output = [0 for _ in range(len(temperatures))]
    i = 0
    while i < len(temperatures) - 1:
        j = i + 1
        while j < len(temperatures) and temperatures[j] <= temperatures[i]:
            j += 1
        if j == len(temperatures):
            output[i] = 0
        else:
            output[i] = j - i
        i += 1
    return output


if __name__ == '__main__':
    _temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    main(_temperatures)
