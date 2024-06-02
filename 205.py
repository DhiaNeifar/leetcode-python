def isIsomorphic(s, t):
    d_s, d_t = {}, {}
    for index, char in enumerate(s):
        iso_s = d_s.get(char, 0)
        iso_t = d_t.get(t[index], 0)
        if iso_s and iso_s != t[index] or iso_t and iso_t != char:
            return False
        else:
            d_s[char] = t[index]
            d_t[t[index]] = char
    return True



if __name__ == '__main__':
    str1 = 'badc'
    str2 = 'baba'
    print(isIsomorphic(str1, str2))
