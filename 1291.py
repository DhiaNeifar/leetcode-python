def main(low, high):
    def power(x):
        pow_ = 0
        while x:
            x //= 10
            pow_ += 1
        return pow_

    def baselines(n):
        add_, base_ = 1, 1
        for j in range(n - 1):
            add_ *= 10
            add_ += 1
            base_ *= 10
            base_ += j + 2
        return add_, base_
        pass

    pow_low, pow_high = power(low), power(high)
    results = []
    for i in range(pow_low, pow_high + 1):
        add, base = baselines(i)
        k = 0
        while k < 10 - i:
            if low <= base <= high:
                results.append(base)
            base += add
            k += 1
    return results


if __name__ == '__main__':
    low_ = 58
    high_ = 155
    print(main(low_, high_))
