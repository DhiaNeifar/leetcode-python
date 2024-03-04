def main(s):
    num_ones = 0
    bits = []
    for bit in s:
        if bit == '1':
            num_ones += 1
    for i in range(num_ones - 1):
        bits.append('1')
    for i in range(len(s) - num_ones):
        bits.append('0')
    bits.append('1')
    print(bits)
    return ''.join(bits)
    # return '1' * (num_ones - 1) + '0' * (len(s) - num_ones) + '1'


if __name__ == '__main__':
    s_ = '010'
    main(s_)
