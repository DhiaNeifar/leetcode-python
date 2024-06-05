def main(words):
    intersection = set(words[0])
    frequency = {}
    for char in words[0]:
        frequency[char] = frequency.get(char, 0) + 1
    for i in range(1, len(words)):
        intersection = intersection & set(words[i])
        new_frequency = {}
        for char in words[i]:
            if char in intersection:
                new_frequency[char] = new_frequency.get(char, 0) + 1
        for char in intersection:
            frequency[char] = min(frequency[char], new_frequency[char])
    results = []
    for char in intersection:
        results.extend([char for _ in range(frequency[char])])
    print(results)
    return results


if __name__ == '__main__':
    words_ = ["bbddabab", "cbcddbdd", "bbcadcab", "dabcacad", "cddcacbc", "ccbdbcba", "cbddaccc", "accdcdbb"]
    main(words_)

