def main(n):
    def calc(n):
        if n < 2:
            return 0
        if n % 2:
            return (n - 1) // 2 + calc((n - 1) // 2 + 1)
        else:
            return n // 2 + calc(n // 2)

    return calc(n)