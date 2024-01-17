def main(arr):
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    return len(set(freq.values())) == len(freq)


if __name__ == '__main__':
    _arr = [1, 2, 3, 4, 4]
    main(_arr)
