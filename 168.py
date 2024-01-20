def main(columnNumber):
    output = []
    while columnNumber:
        columnNumber -= 1
        digit = columnNumber % 26
        output.append(chr(digit + 65))
        columnNumber = (columnNumber - digit) // 26
    result = ''.join(output[::-1])
    return result


if __name__ == '__main__':
    _columnNumber = 1008
    main(_columnNumber)
