def main(word1, word2):
    i, j, k, l = 0, 0, 0, 0
    while i < len(word1) and j < len(word2) and word1[i][k] == word2[j][l]:
        k += 1
        l += 1
        if k == len(word1[i]):
            i += 1
            k = 0
        if l == len(word2[j]):
            j += 1
            l = 0
    if i == len(word1) and j == len(word2):
        return True
    return False


if __name__ == '__main__':
    _word1 = ["ab", "c"]
    _word2 = ["a", "bc"]
    main(_word1, _word2)
