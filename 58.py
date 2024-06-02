def lengthOfLastWord1(s: str) -> int:
    i = 0
    count = 0
    while i < len(s):
        while i < len(s) and s[i] == ' ':
            i += 1
        j = i
        while j < len(s) and s[j] != ' ':
            j += 1
        if j > i:
            count = j - i
        i = j
    return count


def lengthOfLastWord(s: str) -> int:
    i = len(s) - 1
    while i > 0 and s[i] == ' ':
        i -= 1
    j = i
    while j > -1 and s[j] != ' ':
        j -= 1
    print(i - j)
    return i - j


if __name__ == '__main__':
    s = "a"
    lengthOfLastWord(s)
