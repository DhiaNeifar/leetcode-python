def main(arr, k):
    frequencies = {}
    for number in arr:
        frequencies[number] = frequencies.get(number, 0) + 1
    frequencies = sorted(frequencies.values())
    i = 0
    count = 0
    while i < len(frequencies) and count + frequencies[i] <= k:
        count += frequencies[i]
        i += 1
    return len(frequencies) - i


if __name__ == '__main__':
    _arr = [4,5, 5]
    _k = 1
    print(main(_arr, _k))
