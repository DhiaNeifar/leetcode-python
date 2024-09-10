def main(dictionary, sentence):
    dictionary.sort(key=len)
    dictionary.sort()
    indexation = [0 for _ in range(28)]
    print(dictionary)
    for word in dictionary:
        indexation[ord(word[0]) - 96] += 1
    for i in range(1, len(indexation)):
        indexation[i] += indexation[i - 1]
    print(indexation)
    i = 0
    while i < len(sentence):
        j = i + 1
        while j < len(sentence) and sentence[j] != ' ':
            j += 1
        # start = indexation[ord(sentence[i]) - 97] - 1
        # end = indexation[ord(sentence[i]) - 96]
        # print(start, end)

        i = j + 1

    pass


if __name__ == '__main__':
    dictionary_ = ["aab", "b", "za", "a", "c"]
    sentence_ = "aadsfasf absbs bbab cadsfafs"
    main(dictionary_, sentence_)
