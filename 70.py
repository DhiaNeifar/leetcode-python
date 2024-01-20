def main(n):
    if n <= 1:
        return 1
    else:
        l = [1, 1]
        for i in range(n - 1):
            l.append(l[i] + l[i + 1])
        return l[n]


if __name__ == '__main__':
    _n = 5
    main(_n)
