def main(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if t[j] == s[i]:
            i += 1
        j += 1
    return i == len(s)