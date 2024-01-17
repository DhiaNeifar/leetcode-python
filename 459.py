def main(s):
    n = len(s)
    div = []
    for i in range(1, n // 2 + 1):
        if not n % i:
            div.append(i)
    for i in div:
        if s == s[:i] * (n // i):
            return True
    return False


def main1(s):
    return s in (s + s)[1: -1]


if __name__ == '__main__':
    _s = 'abab'
    print(main(_s))
