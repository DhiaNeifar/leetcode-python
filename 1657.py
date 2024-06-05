def main(word1, word2):
    def extract(string):
        l = [0 for _ in range(26)]
        for char in string:
            l[ord(char) - ord('a')] += 1
        l.sort()
        return set(string), l
    set1, l1 = extract(word1)
    set2, l2 = extract(word2)
    return set1 == set2 and l1 == l2



if __name__ == '__main__':
    word1_ = "abc"
    word2_ = "bca"
    print(main(word1_, word2_))
