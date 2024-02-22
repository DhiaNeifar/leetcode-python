def main(n):
    div = n // 7
    rest = n % 7
    sum_ = rest * (rest + 1) // 2 
    return sum_ + div * rest + 28 * div + 7 * div * (div - 1) // 2


if __name__ == '__main__':
    _n = 10
    print(main(_n))
