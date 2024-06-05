def main(s, t):
    i, j = 0, 0
    while i < len(s):
        if s[i] == t[j]:
            j += 1
            if j == len(t):
                return 0
        i += 1
    return len(t) - j


if __name__ == '__main__':
    s_ = "z"
    t_ = "abcde"
    print(main(s_, t_))
