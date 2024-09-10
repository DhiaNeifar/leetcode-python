def main(original, m, n):
    if len(original) != m * n:
        return []
    return [[original[i * n + j] for j in range(n)] for i in range(m)]


if __name__ == '__main__':
    original_ = [1, 2, 3, 4]
    m_ = 2
    n_ = 2
    print(main(original_, m_, n_))
