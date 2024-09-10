def main(x):
    # Not the fastest
    # Binary search is faster
    a, b, n = 0, 1, 0
    while a + b <= x:
        n += 1
        a += b
        b += 2
    return n


if __name__ == '__main__':
    x_ = 36
    print(main(x_))
