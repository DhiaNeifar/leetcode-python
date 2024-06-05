def main(s):
    x = int(s, 2)
    count = 0
    while x != 1:
        if not x % 2:
            x //= 2
        else:
            x += 1
        count += 1
    return count


if __name__ == '__main__':
    s_ = "1101"
    print(main(s_))
