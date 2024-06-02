def main(n):
    x = n * (n + 1) // 2
    i = 1
    while i * i < x:
        i += 1
    if i * i == x:
        return i
    return -1



if __name__ == '__main__':
    n_ = 8
    main(n_)
