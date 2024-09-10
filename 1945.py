def main(s, k):
    x = 0
    for letter in s:
        ord_ = ord(letter) - 96
        x += ord_ // 10 + ord_ % 10

    def process_(x_):
        l = 0
        while x_:
            l += x_ % 10
            x_ = x_ // 10
        return l

    for _ in range(k - 1):
        x = process_(x)

    return x


if __name__ == '__main__':
    s_ = "iiii"
    k_ = 1
    print(main(s_, k_))
