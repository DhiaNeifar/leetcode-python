def main(s):
    frequency = {}
    for letter in s:
        frequency[letter] = frequency.get(letter, 0) + 1
    for index, letter in enumerate(s):
        if frequency[letter] == 1:
            return index
    return -1


if __name__ == '__main__':
    _s = 'leetcode'
    main(_s)
