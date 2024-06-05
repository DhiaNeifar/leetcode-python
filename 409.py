def main(s):
    frequency = {}
    for char in s:
        x = frequency.get(char, 0)
        frequency[char] = x + 1
    count, a = 0, 0
    for value in frequency.values():
        if value % 2:
            count += value - 1
            a = 1
        else:
            count += value
    return count + a


if __name__ == '__main__':
    s_ = 'a'
    print(main(s_))

