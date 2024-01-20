def main(dividend, divisor):

    # TIME LIMIT EXCEEDED
    def sign(x):
        return 1 if x < 0 else 0

    def absolute(x, _sign):
        return -x if _sign else x

    if not dividend:
        return 0

    sign_dividend, sign_divisor = sign(dividend), sign(divisor)

    dividend = absolute(dividend, sign_dividend)
    divisor = absolute(divisor, sign_divisor)

    quotient = 0
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1
    if sign_dividend ^ sign_divisor:
        return -quotient
    return quotient


if __name__ == '__main__':
    _dividend, _divisor = -10, 3
    print(main(_dividend, _divisor))
