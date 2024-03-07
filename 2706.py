def main(prices, money):
    prices.sort()
    rest = prices[0] + prices[1]
    if prices[0] >= money or rest > money:
        return money
    return money - rest


if __name__ == '__main__':
    prices_ = [98, 54, 6, 34, 66, 63, 52, 39]
    money_ = 62
    main(prices_, money_)
