def main(s):
    l = []
    for char in s:
        if char in "0123456789":
            l.append(char)
        if 65 <= ord(char) <= 90:
            l.append(chr(ord(char) + 32))
        if 97 <= ord(char) <= 122:
            l.append(char)
    print(l)
    i, j = 0, len(l) - 1
    while i <= j and l[i] == l[j]:
        i += 1
        j -= 1
    return i >= j


if __name__ == '__main__':
    s_ = "Marge, let's \"[went].\" I await {news} telegram."
    print(main(s_))
