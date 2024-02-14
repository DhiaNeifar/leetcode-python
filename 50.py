def main(x, n):
    def my_pow(a, b):
        if b == 0:
            return 1
        if b == 1:
            return a
        if b % 2:
            return a * my_pow(a, b - 1)
        else:
            half = my_pow(a, b // 2)
            return half * half
    if x == 0:
        return 0
    if n == 0:
        return 1
    _sign = 1 if n < 0 else 0
    n = abs(n)
    if _sign:
        return 1 / my_pow(x, n)
    else:
        return my_pow(x, n)



if __name__ == '__main__':
    _x = 2
    _n = -5
    print(main(_x, _n))
