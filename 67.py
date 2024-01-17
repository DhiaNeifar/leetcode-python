def main(a, b):
    def string_int(x):
        int_ = 0
        pow_ = 1
        for i in range(len(x) - 1, -1, -1):
            int_ += pow_ * (ord(x[i]) - 48)
            pow_ *= 2
        return int_

    def int_string(x):
        l = []
        while x:
            l.append(chr(x % 2 + 48))
            x //= 2
        return ''.join(l[::-1])

    results = int_string(string_int(a) + string_int(b))
    print(results)
    return results


if __name__ == '__main__':
    _a, _b = '0', '0'
    main(_a, _b)
